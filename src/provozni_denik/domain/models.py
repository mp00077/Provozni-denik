from dataclasses import dataclass


@dataclass(frozen=True)
class Visit:
    id: int
    person: str
    room: str
    purpose: str
    escort: str
    arrived_at: str
    departed_at: str | None
    created_by: str
