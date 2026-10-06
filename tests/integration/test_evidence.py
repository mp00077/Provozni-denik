import csv
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from provozni_denik.domain.errors import ValidationError
from provozni_denik.infrastructure.database.connection import connect
from provozni_denik.infrastructure.database.repositories import SqliteVisitRepository
from provozni_denik.services.access_service import AccessService
from provozni_denik.infrastructure.backups.sqlite_backup import backup
from provozni_denik.infrastructure.exports.csv_exporter import export_csv


class Identity:
    def current_actor(self):
        return "test-operator"


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.path = Path(self.temporary.name) / "journal.sqlite3"
        self.connection = connect(self.path)
        self.repository = SqliteVisitRepository(self.connection)
        self.service = AccessService(self.repository, Identity())

    def tearDown(self):
        self.connection.close()
        self.temporary.cleanup()

    def arrive(self):
        return self.service.arrive("Jan Novák", "S1", "Údržba")

    def test_arrival_departure_and_reentry(self):
        visit_id = self.arrive()
        self.service.depart(visit_id)
        self.assertIsNotNone(self.service.list_visits()[0].departed_at)
        self.assertEqual([e["event_type"] for e in self.repository.audit(visit_id)], ["departure", "arrival"])
        with self.assertRaises(ValidationError):
            self.service.depart(visit_id)
        self.assertEqual(len(self.repository.audit(visit_id)), 2)
        self.assertNotEqual(self.arrive(), visit_id)

    def test_duplicate_open_visit_is_rejected(self):
        self.arrive()
        with self.assertRaises(ValidationError):
            self.arrive()
        self.assertEqual(len(self.service.list_visits()), 1)
        self.assertEqual(len(self.repository.audit()), 1)

    def test_required_fields(self):
        with self.assertRaises(ValidationError):
            self.service.arrive("  ", "S1", "Údržba")
        self.assertEqual(self.service.list_visits(), [])

    def test_correction_preserves_original_and_requires_reason(self):
        visit_id = self.arrive()
        with self.assertRaises(ValidationError):
            self.service.correct(visit_id, "Jan Novák", "S1", "Oprava", "", " ")
        self.service.correct(visit_id, "Jan Novák", "S1", "Oprava", "", "Upřesnění účelu")
        event = self.repository.audit(visit_id)[0]
        self.assertEqual(json.loads(event["before_json"])["purpose"], "Údržba")
        self.assertEqual(json.loads(event["after_json"])["purpose"], "Oprava")
        self.assertEqual(event["actor"], "test-operator")

    def test_audit_failure_rolls_back_visit(self):
        with patch.object(self.repository, "_event", side_effect=RuntimeError("failure")):
            with self.assertRaises(RuntimeError):
                self.arrive()
        self.assertEqual(self.service.list_visits(), [])

    def test_audit_cannot_be_modified_through_sql(self):
        self.arrive()
        for sql in ("DELETE FROM audit_events", "UPDATE audit_events SET actor='other'"):
            with self.assertRaises(sqlite3.IntegrityError):
                with self.connection:
                    self.connection.execute(sql)
        self.assertEqual(len(self.repository.audit()), 1)

    def test_audit_failure_rolls_back_departure_and_correction(self):
        visit_id = self.arrive()
        with patch.object(self.repository, "_event", side_effect=RuntimeError("failure")):
            with self.assertRaises(RuntimeError):
                self.service.depart(visit_id)
            with self.assertRaises(RuntimeError):
                self.service.correct(visit_id, "Jiná osoba", "S1", "Oprava", "", "Chyba jména")
        visit = self.service.list_visits()[0]
        self.assertIsNone(visit.departed_at)
        self.assertEqual(visit.person, "Jan Novák")
        self.assertEqual(len(self.repository.audit()), 1)

    def test_backup_contains_visits_and_audit(self):
        self.arrive()
        destination = Path(self.temporary.name) / "backup.sqlite3"
        backup(self.connection, self.path, destination)
        other = connect(destination)
        try:
            self.assertEqual(other.execute("SELECT COUNT(*) FROM visits").fetchone()[0], 1)
            self.assertEqual(other.execute("SELECT COUNT(*) FROM audit_events").fetchone()[0], 1)
            self.assertEqual(other.execute("PRAGMA integrity_check").fetchone()[0], "ok")
        finally:
            other.close()
        with self.assertRaises(ValueError):
            backup(self.connection, self.path, self.path)

    def test_csv_formula_cells_are_escaped(self):
        self.service.arrive("=1+1", "S1", "Údržba")
        destination = Path(self.temporary.name) / "export.csv"
        export_csv(destination, self.service.list_visits())
        with destination.open(encoding="utf-8-sig", newline="") as stream:
            row = next(csv.DictReader(stream, delimiter=";"))
        self.assertEqual(row["person"], "'=1+1")

    def test_database_reopens_without_reapplying_migration(self):
        self.arrive()
        other = connect(self.path)
        try:
            self.assertEqual(other.execute("PRAGMA user_version").fetchone()[0], 1)
            self.assertEqual(other.execute("SELECT COUNT(*) FROM visits").fetchone()[0], 1)
        finally:
            other.close()


if __name__ == "__main__":
    unittest.main()
