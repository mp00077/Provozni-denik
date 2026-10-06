from enum import StrEnum


class EventType(StrEnum):
    ARRIVAL = "arrival"
    DEPARTURE = "departure"
    CORRECTION = "correction"
