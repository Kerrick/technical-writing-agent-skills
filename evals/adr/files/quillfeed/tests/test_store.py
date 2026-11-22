from pathlib import Path

from quillfeed.store import body_path


def test_bodies_go_in_a_two_digit_folder():
    path = body_path(Path("/data"), b"<p>hello</p>")
    assert path.parent.name == path.name[:2] and path.suffix == ".zst"
