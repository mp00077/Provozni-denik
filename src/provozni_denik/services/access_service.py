from provozni_denik.domain.rules import required
from provozni_denik.domain.errors import ValidationError
from provozni_denik.ports.identity_provider import IdentityProvider
from provozni_denik.ports.repositories import VisitRepository


class AccessService:
    def __init__(self, repository: VisitRepository, identity: IdentityProvider):
        self.repository = repository
        self.identity = identity

    def list_visits(self):
        return self.repository.list_visits()

    def _fields(self, person, room, purpose, escort):
        if len(escort.strip()) > 150:
            raise ValidationError("Pole Doprovod smí mít nejvýše 150 znaků.")
        return (required(person, "Osoba", 150), required(room, "Serverovna", 150),
                required(purpose, "Účel", 1000), escort.strip())

    def arrive(self, person, room, purpose, escort=""):
        return self.repository.arrive(*self._fields(person, room, purpose, escort),
                                      required(self.identity.current_actor(), "Operátor"))

    def depart(self, visit_id):
        self.repository.depart(visit_id, required(self.identity.current_actor(), "Operátor"))

    def correct(self, visit_id, person, room, purpose, escort, reason):
        self.repository.correct(visit_id, *self._fields(person, room, purpose, escort),
                                required(self.identity.current_actor(), "Operátor"),
                                required(reason, "Důvod opravy", 1000))
