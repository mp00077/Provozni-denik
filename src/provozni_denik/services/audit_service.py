class AuditService:
    def __init__(self, repository):
        self.repository = repository

    def history(self, visit_id=None):
        return self.repository.audit(visit_id)
