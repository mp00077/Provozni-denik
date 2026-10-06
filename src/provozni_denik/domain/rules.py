from .errors import ValidationError


def required(value: str, label: str, limit: int = 500) -> str:
    value = value.strip()
    if not value:
        raise ValidationError(f"Vyplňte pole {label}.")
    if len(value) > limit:
        raise ValidationError(f"Pole {label} smí mít nejvýše {limit} znaků.")
    return value
