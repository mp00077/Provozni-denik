from datetime import datetime
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QSortFilterProxyModel


def local_time(value):
    return datetime.fromisoformat(value).astimezone().strftime("%d.%m.%Y %H:%M:%S") if value else "Přítomen"


class VisitsModel(QAbstractTableModel):
    HEADERS = ["ID", "Osoba", "Serverovna", "Účel", "Doprovod", "Příchod", "Odchod", "Zapsal"]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.visits = []

    def replace(self, visits):
        self.beginResetModel()
        self.visits = visits
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        return 0 if parent.isValid() else len(self.visits)

    def columnCount(self, parent=QModelIndex()):
        return 0 if parent.isValid() else len(self.HEADERS)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        visit = self.visits[index.row()]
        values = [visit.id, visit.person, visit.room, visit.purpose, visit.escort,
                  visit.arrived_at, visit.departed_at, visit.created_by]
        if role == Qt.ItemDataRole.ToolTipRole:
            value = values[index.column()]
            if index.column() in (5, 6) and value:
                return datetime.fromisoformat(value).astimezone().isoformat(timespec="seconds")
            return str(value) if value is not None else "Osoba je dosud přítomna"
        if role == Qt.ItemDataRole.UserRole:
            return values[index.column()] if values[index.column()] is not None else ""
        if role == Qt.ItemDataRole.DisplayRole:
            return local_time(values[index.column()]) if index.column() in (5, 6) else values[index.column()]
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.HEADERS[section]
        return None


class VisitsFilter(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.query = ""
        self.open_only = False
        self.setSortRole(Qt.ItemDataRole.UserRole)

    def update_filter(self, query, open_only):
        self.query = query.casefold().strip()
        self.open_only = open_only
        self.invalidate()

    def filterAcceptsRow(self, row, parent):
        visit = self.sourceModel().visits[row]
        return (not self.open_only or visit.departed_at is None) and (
            not self.query or self.query in " ".join([visit.person, visit.room, visit.purpose, visit.escort]).casefold())
