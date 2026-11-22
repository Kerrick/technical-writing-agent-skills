"""Store articles: fields in SQLite, bodies as compressed files (ADR 003)."""

import hashlib
from pathlib import Path


def body_path(data_dir: Path, body: bytes) -> Path:
    """Where a body's file goes. The naming is doc/design/storage.md, "File naming"."""
    digest = hashlib.sha256(body).hexdigest()
    return data_dir / "bodies" / digest[:2] / f"{digest}.zst"


def is_past_retention(fetched_at: int, now: int, retention_days: int, starred: bool) -> bool:
    """Whether the nightly cleanup deletes this body (doc/design/storage.md, "Retention")."""
    if starred or retention_days == 0:
        return False
    return now - fetched_at > retention_days * 86400
