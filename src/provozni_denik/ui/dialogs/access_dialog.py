from PySide6.QtWidgets import QDialog, QDialogButtonBox
from provozni_denik.domain.errors import ValidationError
from provozni_denik.ui.generated.access_dialog import Ui_AccessDialog


class AccessDialog(QDialog):
    def __init__(self, access, parent=None, visit=None, default_room=""):
        super().__init__(parent)
        self.ui = Ui_AccessDialog()
        self.ui.setupUi(self)
        self.access = access
        self.visit = visit
        self.ui.roomEdit.setText(default_room)
        self.ui.reasonLabel.setVisible(visit is not None)
        self.ui.reasonEdit.setVisible(visit is not None)
        if visit:
            self.setWindowTitle(f"Opravit záznam č. {visit.id}")
            for name, value in (("person", visit.person), ("room", visit.room),
                                ("purpose", visit.purpose), ("escort", visit.escort)):
                getattr(self.ui, name + "Edit").setText(value)
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Save).setText("Uložit")
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel).setText("Zrušit")
        self.ui.buttonBox.accepted.connect(self.save)
        self.ui.buttonBox.rejected.connect(self.reject)

    def save(self):
        values = [getattr(self.ui, field + "Edit").text() for field in ("person", "room", "purpose", "escort")]
        try:
            if self.visit:
                self.access.correct(self.visit.id, *values, self.ui.reasonEdit.text())
            else:
                self.access.arrive(*values)
        except ValidationError as error:
            self.ui.errorLabel.setText(str(error))
        except Exception:
            import logging
            logging.exception("Zápis návštěvy selhal")
            self.ui.errorLabel.setText("Záznam nebyl uložen. Zkontrolujte diagnostický log.")
        else:
            self.accept()
