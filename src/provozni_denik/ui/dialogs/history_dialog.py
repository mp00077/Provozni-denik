import json
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QDialogButtonBox
from provozni_denik.ui.generated.history_view import Ui_HistoryDialog
from provozni_denik.ui.models.visits_model import local_time


class HistoryDialog(QDialog):
    def __init__(self, events, parent=None):
        super().__init__(parent)
        self.ui = Ui_HistoryDialog()
        self.ui.setupUi(self)
        from provozni_denik.ui.theme import style_dialog
        style_dialog(self)
        self.events = events
        table = self.ui.eventsTable
        table.verticalHeader().hide()
        table.verticalHeader().setDefaultSectionSize(44)
        table.setAlternatingRowColors(True)
        table.setShowGrid(False)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Čas", "Událost", "Operátor", "Důvod"])
        table.setRowCount(len(events))
        names = {"arrival": "Příchod", "departure": "Odchod", "correction": "Oprava"}
        for row, event in enumerate(events):
            for column, value in enumerate([local_time(event["occurred_at"]),
                                             names.get(event["event_type"], event["event_type"]),
                                             event["actor"], event["reason"]]):
                table.setItem(row, column, QTableWidgetItem(value))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        table.itemSelectionChanged.connect(self.show_details)
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Close).setText("Zavřít")
        self.ui.buttonBox.rejected.connect(self.reject)
        if events:
            table.selectRow(0)

    def show_details(self):
        row = self.ui.eventsTable.currentRow()
        if row >= 0:
            event = self.events[row]
            before = json.loads(event["before_json"]) if event["before_json"] else None
            after = json.loads(event["after_json"])
            fields = {"person": "Osoba", "room": "Serverovna", "purpose": "Účel návštěvy",
                      "escort": "Doprovod", "arrived_at": "Příchod", "departed_at": "Odchod",
                      "created_by": "Zapsal"}
            def describe(values):
                if values is None:
                    return "Nový záznam — původní hodnoty nejsou k dispozici."
                lines = []
                for key, caption in fields.items():
                    value = values.get(key)
                    if key in ("arrived_at", "departed_at"):
                        value = local_time(value)
                    lines.append(f"{caption}: {value or '—'}")
                return "\n".join(lines)
            self.ui.detailsEdit.setPlainText("PŮVODNÍ HODNOTY\n" + describe(before)
                                            + "\n\nNOVÉ HODNOTY\n" + describe(after))
