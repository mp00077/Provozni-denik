import json
import sqlite3
from datetime import datetime, timezone

from provozni_denik.domain.errors import ValidationError
from provozni_denik.domain.models import Visit


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


class SqliteVisitRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def list_visits(self) -> list[Visit]:
        rows = self.connection.execute("SELECT * FROM visits ORDER BY id DESC").fetchall()
        return [Visit(**dict(row)) for row in rows]

    def _get(self, visit_id: int) -> dict:
        row = self.connection.execute("SELECT * FROM visits WHERE id=?", (visit_id,)).fetchone()
        if row is None:
            raise ValidationError("Záznam nebyl nalezen.")
        return dict(row)

    def _event(self, visit_id: int, kind: str, actor: str, before: dict | None,
               after: dict, reason: str = "") -> None:
        self.connection.execute(
            "INSERT INTO audit_events(visit_id,event_type,occurred_at,actor,before_json,after_json,reason) "
            "VALUES(?,?,?,?,?,?,?)",
            (visit_id, kind, now(), actor, json.dumps(before, ensure_ascii=False) if before else None,
             json.dumps(after, ensure_ascii=False), reason))

    def arrive(self, person: str, room: str, purpose: str, escort: str, actor: str) -> int:
        try:
            with self.connection:
                cursor = self.connection.execute(
                    "INSERT INTO visits(person,room,purpose,escort,arrived_at,created_by) VALUES(?,?,?,?,?,?)",
                    (person, room, purpose, escort, now(), actor))
                visit_id = cursor.lastrowid
                self._event(visit_id, "arrival", actor, None, self._get(visit_id))
            return visit_id
        except sqlite3.IntegrityError as error:
            raise ValidationError("Tato osoba má v serverovně již otevřenou návštěvu.") from error

    def depart(self, visit_id: int, actor: str) -> None:
        with self.connection:
            self.connection.execute("BEGIN IMMEDIATE")
            before = self._get(visit_id)
            cursor = self.connection.execute(
                "UPDATE visits SET departed_at=? WHERE id=? AND departed_at IS NULL", (now(), visit_id))
            if cursor.rowcount != 1:
                raise ValidationError("Návštěva je již uzavřena.")
            self._event(visit_id, "departure", actor, before, self._get(visit_id))

    def correct(self, visit_id: int, person: str, room: str, purpose: str,
                escort: str, actor: str, reason: str) -> None:
        try:
            with self.connection:
                self.connection.execute("BEGIN IMMEDIATE")
                before = self._get(visit_id)
                self.connection.execute("UPDATE visits SET person=?,room=?,purpose=?,escort=? WHERE id=?",
                                        (person, room, purpose, escort, visit_id))
                self._event(visit_id, "correction", actor, before, self._get(visit_id), reason)
        except sqlite3.IntegrityError as error:
            raise ValidationError("Oprava by vytvořila duplicitní otevřenou návštěvu.") from error

    def audit(self, visit_id: int | None = None) -> list[dict]:
        query = "SELECT * FROM audit_events"
        parameters = ()
        if visit_id is not None:
            query += " WHERE visit_id=?"
            parameters = (visit_id,)
        return [dict(row) for row in self.connection.execute(query + " ORDER BY id DESC", parameters)]
