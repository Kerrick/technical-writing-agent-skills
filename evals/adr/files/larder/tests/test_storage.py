import sqlite3


def test_a_command_leaves_one_file(tmp_path):
    db = tmp_path / "larder.db"
    sqlite3.connect(db).close()
    assert [p.name for p in tmp_path.iterdir()] == ["larder.db"]
