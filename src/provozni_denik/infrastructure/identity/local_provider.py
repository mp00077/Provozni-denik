import getpass


class LocalIdentityProvider:
    """Identita OS pro lokální verzi; nejde o ověřené přihlášení aplikace."""

    def current_actor(self) -> str:
        return getpass.getuser()
