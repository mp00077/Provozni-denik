from typing import Protocol


class IdentityProvider(Protocol):
    def current_actor(self) -> str: ...
