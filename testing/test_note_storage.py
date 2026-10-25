"""
Program: Note Taking App
Author: Caleb Gebrezgi
Purpose: Testing for saving and loading notes.
Date: 10-25-2026
"""

from notes_app.note_model import Note
from notes_app.note_storage import save_notes, load_notes


def test_save_and_load_round_trip(tmp_path):
    """Notes that are saved retain the same title and body."""
    filename = tmp_path / "notes.json"
    save_notes([Note("Homework", "Chapter 1")], filename)
    loaded = load_notes(filename)
    assert len(loaded) == 1
    assert loaded[0].title == "Homework"
    assert loaded[0].body == "Chapter 1"


def test_load_missing_file_returns_empty_list(tmp_path):
    """A missing file will return an empty list."""
    assert load_notes(tmp_path / "missing.json") == []


def test_load_damaged_file_returns_empty_list(tmp_path):
    """An invalid file will return an empty list."""
    filename = tmp_path / "notes.json"
    filename.write_text("{this is not valid json")
    assert load_notes(filename) == []