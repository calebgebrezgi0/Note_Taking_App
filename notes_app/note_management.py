"""
Program: Note Taking App
Author: Caleb Gebrezgi
Purpose: Creating the NoteManager class, which keeps track of all notes.
Date: 10-24-2026
"""

from notes_app.note_model import Note
from notes_app.note_storage import save_notes, load_notes


class NoteManager:
    """Keeps track of a list of notes."""

    def __init__(self):
        """Create a blank manager without any notes."""
        self.notes = []

    def add_note(self, title, body=""):
        """Create a note and add it to the list."""
        note = Note(title, body)
        self.notes.append(note)
        return note

    def list_notes(self):
        """Return the list of all notes."""
        return self.notes

    def save(self, filename="notes.json"):
        """Save all notes to a JSON file."""
        return save_notes(self.notes, filename)

    def load(self, filename="notes.json"):
        """Replace the current notes with the ones saved in the file."""
        self.notes = load_notes(filename)