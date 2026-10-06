import csv
from dataclasses import asdict


def safe_cell(value):
    if isinstance(value, str) and value.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + value
    return value


def export_csv(path, visits):
    from provozni_denik.domain.models import Visit
    with open(path, "w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(Visit.__dataclass_fields__), delimiter=";")
        writer.writeheader()
        for visit in visits:
            writer.writerow({key: safe_cell(value) for key, value in asdict(visit).items()})
