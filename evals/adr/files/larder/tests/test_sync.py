from larder.sync import find_conflict_copies


def test_finds_a_dropbox_conflict_copy(tmp_path):
    db = tmp_path / "larder.db"
    db.touch()
    copy = tmp_path / "larder (conflicted copy).db"
    copy.touch()
    assert find_conflict_copies(db) == [copy]


def test_ignores_other_databases(tmp_path):
    db = tmp_path / "larder.db"
    db.touch()
    (tmp_path / "recipes.db").touch()
    assert find_conflict_copies(db) == []
