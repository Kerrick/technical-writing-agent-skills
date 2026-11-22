"""Find the copies a file-syncing service leaves when two devices wrote before syncing.

Devices share the database through the user's file-syncing service (ADR 0010).
How the check works is in docs/design/storage.md.
"""

from pathlib import Path

MARKERS = ("conflicted copy", "sync-conflict", " 2.db")


def find_conflict_copies(db: Path) -> list[Path]:
    """Return the conflict copies beside db, oldest first."""
    copies = [p for p in db.parent.glob("*.db") if p != db and any(m in p.name for m in MARKERS)]
    return sorted(copies, key=lambda p: p.stat().st_mtime)


def refuse_if_conflicted(db: Path) -> None:
    copies = find_conflict_copies(db)
    if copies:
        names = ", ".join(p.name for p in copies)
        raise SystemExit(f"larder: found conflict copies beside {db.name}: {names}. Keep one file and delete the others.")
