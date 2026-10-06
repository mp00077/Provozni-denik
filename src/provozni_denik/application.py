def run(app, config):
    from provozni_denik.infrastructure.database.connection import connect
    from provozni_denik.infrastructure.database.repositories import SqliteVisitRepository
    from provozni_denik.infrastructure.identity.local_provider import LocalIdentityProvider
    from provozni_denik.services.access_service import AccessService
    from provozni_denik.services.audit_service import AuditService
    from provozni_denik.services.export_service import ExportService
    from provozni_denik.services.backup_service import BackupService
    from provozni_denik.ui.windows.main_window import MainWindow

    connection = connect(config.database_path)
    try:
        repository = SqliteVisitRepository(connection)
        identity = LocalIdentityProvider()
        access = AccessService(repository, identity)
        window = MainWindow(access, AuditService(repository), ExportService(access),
                            BackupService(connection, config.database_path), identity, config)
        window.show()
        return app.exec()
    finally:
        connection.close()
