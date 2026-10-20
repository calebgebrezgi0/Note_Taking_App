"""
Program: Note Taking App
Author: Caleb Gebrezgi
Purpose: Testing for the note class
Date: 10-20-2026
"""


from notes_app.note_model import Note


def test_note_stores_title_and_body():
    """A created note retains the title and body that was given to it."""
    note = Note("Homework", "Chapter 1, Chapter 2")
    assert note.title == "Homework"
    assert note.body == "Chapter 1, Chapter 2"