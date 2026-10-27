"""
Program: Note Taking App
Author: Caleb Gebrezgi
Purpose: Testing for the NoteManager class.
Date: 10-24-2026
"""

import pytest

from notes_app.note_management import NoteManager


def test_new_manager_has_no_notes():
    """Ensure that a newly created manager starts with an empty list."""
    manager = NoteManager()
    assert manager.list_notes() == []


def test_add_note():
    """When a note is added, ensure it gets put in the list."""
    manager = NoteManager()
    manager.add_note("Homework", "Chapter 1")
    notes = manager.list_notes()
    assert len(notes) == 1
    assert notes[0].title == "Homework"


def test_empty_title_error():
    """A note without a title is not accepted."""
    manager = NoteManager()
    with pytest.raises(ValueError):
        manager.add_note("   ")

def test_save_and_load(tmp_path):
    """Notes saved by one manager can be loaded by another manager."""
    filename = tmp_path / "notes.json"
    manager = NoteManager()
    manager.add_note("Homework", "Chapter 1")
    manager.save(filename)

    new_manager = NoteManager()
    new_manager.load(filename)
    assert len(new_manager.list_notes()) == 1
    assert new_manager.list_notes()[0].title == "Homework"