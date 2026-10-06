from PySide6.QtCore import QObject, QRunnable, Signal, Slot


class TaskSignals(QObject):
    finished = Signal(str)
    failed = Signal(str)


class Task(QRunnable):
    def __init__(self, operation, success_message):
        super().__init__()
        self.operation = operation
        self.success_message = success_message
        self.signals = TaskSignals()

    @Slot()
    def run(self):
        try:
            self.operation()
        except Exception:
            import logging
            logging.exception("Operace na pozadí selhala")
            self.signals.failed.emit("Operace selhala. Zkontrolujte diagnostický log.")
        else:
            self.signals.finished.emit(self.success_message)
