import json
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

class ExecutionMemory:
    def __init__(self, path=".agi_pipeline/memory.sqlite3"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.path) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                goal TEXT NOT NULL,
                summary TEXT NOT NULL,
                trace_json TEXT NOT NULL
            )""")

    def save(self, goal, summary, trace):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                "INSERT INTO runs (created_at, goal, summary, trace_json) VALUES (?, ?, ?, ?)",
                (datetime.now(timezone.utc).isoformat(), goal, summary,
                 json.dumps(trace, ensure_ascii=False)),
            )

    def recent(self, limit=10):
        with sqlite3.connect(self.path) as conn:
            rows = conn.execute(
                "SELECT id, created_at, goal, summary FROM runs ORDER BY id DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [dict(id=r[0], created_at=r[1], goal=r[2], summary=r[3]) for r in rows]
