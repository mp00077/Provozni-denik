class ExportService:
    def __init__(self, access):
        self.access = access

    def csv(self, path):
        from provozni_denik.infrastructure.exports.csv_exporter import export_csv
        export_csv(path, self.access.list_visits())
