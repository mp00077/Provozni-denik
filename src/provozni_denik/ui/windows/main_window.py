import logging
from pathlib import Path
from PySide6.QtCore import QSettings, QThreadPool, Qt
from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox, QFileDialog, QHeaderView
from provozni_denik.ui.generated.main_window import Ui_MainWindow
from provozni_denik.ui.models.visits_model import VisitsModel, VisitsFilter
from provozni_denik.domain.errors import ValidationError


class MainWindow(QMainWindow):
    def __init__(self, access, audit, exports, backups, identity, config):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.access, self.audit, self.exports, self.backups = access, audit, exports, backups
        self.identity, self.config = identity, config
        self.settings = QSettings()
        self.pool = QThreadPool(self)
        self.tasks = []
        self.model = VisitsModel(self)
        self.proxy = VisitsFilter(self)
        self.proxy.setSourceModel(self.model)
        self.ui.visitsTable.setModel(self.proxy)
        self.ui.visitsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.ui.visitsTable.horizontalHeader().setStretchLastSection(True)
        self.ui.visitsTable.sortByColumn(0, Qt.SortOrder.DescendingOrder)
        for button, method in (("arrival", self.arrive), ("departure", self.depart),
                               ("correct", self.correct), ("history", self.history),
                               ("refresh", self.refresh), ("export", self.export),
                               ("backup", self.backup), ("settings", self.settings_dialog)):
            getattr(self.ui, button + "Button").clicked.connect(lambda checked=False, action=method: self.perform(action))
        self.ui.searchEdit.textChanged.connect(self.filter)
        self.ui.openOnlyCheck.toggled.connect(self.filter)
        self.ui.visitsTable.selectionModel().selectionChanged.connect(self.update_actions)
        self.refresh()

    def perform(self, action):
        try:
            action()
        except ValidationError as error:
            QMessageBox.warning(self, "Kontrola záznamu", str(error))
        except Exception:
            logging.exception("Operace GUI selhala")
            QMessageBox.critical(self, "Chyba", "Operace selhala. Zkontrolujte diagnostický log.")

    def refresh(self):
        visits = self.access.list_visits()
        self.model.replace(visits)
        self.ui.statusbar.showMessage(f"Operátor: {self.identity.current_actor()} | Záznamů: {len(visits)} | "
                                      f"Přítomno: {sum(v.departed_at is None for v in visits)}")
        self.update_actions()

    def filter(self, *_):
        self.proxy.update_filter(self.ui.searchEdit.text(), self.ui.openOnlyCheck.isChecked())
        self.update_actions()

    def selected(self):
        rows = self.ui.visitsTable.selectionModel().selectedRows()
        return self.model.visits[self.proxy.mapToSource(rows[0]).row()] if rows else None

    def update_actions(self, *_):
        visit = self.selected()
        self.ui.departureButton.setEnabled(visit is not None and visit.departed_at is None)
        self.ui.correctButton.setEnabled(visit is not None)
        self.ui.historyButton.setEnabled(visit is not None)

    def arrive(self):
        from provozni_denik.ui.dialogs.access_dialog import AccessDialog
        dialog = AccessDialog(self.access, self, default_room=self.settings.value("default_room", "", type=str))
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.refresh()

    def depart(self):
        visit = self.selected()
        if visit and QMessageBox.question(self, "Zapsat odchod", f"Zapsat odchod osoby {visit.person}?") == QMessageBox.StandardButton.Yes:
            self.access.depart(visit.id)
            self.refresh()

    def correct(self):
        from provozni_denik.ui.dialogs.access_dialog import AccessDialog
        visit = self.selected()
        if visit and AccessDialog(self.access, self, visit=visit).exec() == QDialog.DialogCode.Accepted:
            self.refresh()

    def history(self):
        from provozni_denik.ui.dialogs.history_dialog import HistoryDialog
        visit = self.selected()
        if visit:
            HistoryDialog(self.audit.history(visit.id), self).exec()

    def export(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export všech záznamů", "denik.csv", "CSV (*.csv)")
        if path:
            # Snapshot se čte v GUI vlákně; worker nepoužívá jeho SQLite spojení.
            visits = self.access.list_visits()
            from provozni_denik.infrastructure.exports.csv_exporter import export_csv
            self.start_task(lambda: export_csv(path, visits), "Export byl uložen.")

    def backup(self):
        path, _ = QFileDialog.getSaveFileName(self, "Záloha databáze", "denik-zaloha.sqlite3", "SQLite (*.sqlite3)")
        if path:
            if Path(path).resolve() == self.config.database_path.resolve():
                raise ValidationError("Zvolte jinou cestu než provozní databázi.")
            source = self.config.database_path
            def operation():
                import sqlite3
                from provozni_denik.infrastructure.backups.sqlite_backup import backup
                connection = sqlite3.connect(source.as_uri() + "?mode=ro", uri=True)
                try:
                    backup(connection, source, path)
                finally:
                    connection.close()
            self.start_task(operation, "Záloha byla uložena.")

    def start_task(self, operation, message):
        from provozni_denik.ui.workers.tasks import Task
        task = Task(operation, message)
        self.tasks.append(task)
        self.ui.exportButton.setEnabled(False)
        self.ui.backupButton.setEnabled(False)
        task.signals.finished.connect(self.task_finished)
        task.signals.failed.connect(self.task_failed)
        self.pool.start(task)

    def task_finished(self, message):
        self.tasks.clear()
        self.ui.exportButton.setEnabled(True)
        self.ui.backupButton.setEnabled(True)
        QMessageBox.information(self, "Hotovo", message)

    def task_failed(self, message):
        self.tasks.clear()
        self.ui.exportButton.setEnabled(True)
        self.ui.backupButton.setEnabled(True)
        QMessageBox.critical(self, "Chyba", message)

    def settings_dialog(self):
        from provozni_denik.ui.dialogs.settings_dialog import SettingsDialog
        SettingsDialog(self.config, self.identity.current_actor(), self.settings, self).exec()

    def closeEvent(self, event):
        if self.tasks:
            QMessageBox.information(self, "Probíhá operace", "Počkejte na dokončení exportu nebo zálohy.")
            event.ignore()
        else:
            event.accept()
