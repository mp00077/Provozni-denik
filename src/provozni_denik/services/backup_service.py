class BackupService:
    def __init__(self, connection, database_path):
        self.connection = connection
        self.database_path = database_path

    def create(self, destination):
        from provozni_denik.infrastructure.backups.sqlite_backup import backup
        backup(self.connection, self.database_path, destination)
