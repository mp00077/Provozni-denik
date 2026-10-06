class ApplicationSession:
    """Inicializace po krocích v GUI vlákně; import modulu nenačítá Qt ani služby."""

    def __init__(self, config):
        self.config = config
        self.connection = None
        self.window = None

    def initialize(self):
        try:
            yield "Připravuji databázi…"
            from provozni_denik.infrastructure.database.connection import connect
            self.connection = connect(self.config.database_path)

            yield "Načítám služby evidence…"
            from provozni_denik.infrastructure.database.repositories import SqliteVisitRepository
            from provozni_denik.infrastructure.identity.local_provider import LocalIdentityProvider
            from provozni_denik.services.access_service import AccessService
            from provozni_denik.services.audit_service import AuditService
            from provozni_denik.services.export_service import ExportService
            from provozni_denik.services.backup_service import BackupService
            repository = SqliteVisitRepository(self.connection)
            identity = LocalIdentityProvider()
            access = AccessService(repository, identity)

            yield "Načítám hlavní okno a záznamy…"
            from provozni_denik.ui.windows.main_window import MainWindow
            self.window = MainWindow(access, AuditService(repository), ExportService(access),
                                     BackupService(self.connection, self.config.database_path),
                                     identity, self.config)
        except Exception:
            self.close()
            raise

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
