"""
Program: Note Taking App
Author: Caleb Gebrezgi
Purpose: Testing for the note class
Date: 10-20-2026
"""

import pytest

from notes_app.note_model import Note


def test_note_stores_title_and_body():
    """A created note retains the title and body that was given to it."""
    note = Note("Homework", "Chapter 1, Chapter 2")
    assert note.title == "Homework"
    assert note.body == "Chapter 1, Chapter 2"

def test_empty_title_raises_error():
    """A title with only spaces is not accepted."""
    with pytest.raises(ValueError):
        Note("   ")

def test_note_to_dict_and_back():
    """Notes that are turned into a dictionary can be recreated with the same data."""
    note = Note("Homework", "Chapter 1")
    rebuilt = Note.from_dict(note.to_dict())
    assert rebuilt.title == note.title
    assert rebuilt.body == note.body