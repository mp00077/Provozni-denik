CREATE TABLE visits (
    id INTEGER PRIMARY KEY,
    person TEXT NOT NULL,
    room TEXT NOT NULL,
    purpose TEXT NOT NULL,
    escort TEXT NOT NULL DEFAULT '',
    arrived_at TEXT NOT NULL,
    departed_at TEXT,
    created_by TEXT NOT NULL
);
CREATE UNIQUE INDEX one_open_visit ON visits(person, room) WHERE departed_at IS NULL;
CREATE TABLE audit_events (
    id INTEGER PRIMARY KEY,
    visit_id INTEGER NOT NULL REFERENCES visits(id),
    event_type TEXT NOT NULL,
    occurred_at TEXT NOT NULL,
    actor TEXT NOT NULL,
    before_json TEXT,
    after_json TEXT NOT NULL,
    reason TEXT NOT NULL DEFAULT ''
);
CREATE TRIGGER audit_no_update BEFORE UPDATE ON audit_events
BEGIN SELECT RAISE(ABORT, 'Audit events cannot be updated'); END;
CREATE TRIGGER audit_no_delete BEFORE DELETE ON audit_events
BEGIN SELECT RAISE(ABORT, 'Audit events cannot be deleted'); END;
