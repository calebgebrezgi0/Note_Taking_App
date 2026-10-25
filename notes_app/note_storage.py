"""
Program: Note Taking App
Author: Caleb Gebrezgi
Purpose: Saving and loading notes using JSON
Date: 10-25-2026
"""

import json

from notes_app.note_model import Note


def save_notes(notes, filename="notes.json"):
    """Saves a list of notes to a JSON file. Return true if notes were successfully saved."""
    data = [note.to_dict() for note in notes]
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except OSError as error:
        print(f"Notes could not be saved: {error}")
        return False
    return True


def load_notes(filename="notes.json"):
    """Load notes from a JSON file and return them as a list.

    Returns the list as empty if the file does not exist or cannot be read.
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return [Note.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, KeyError, TypeError):
        print("No notes were loaded due to the note file being damaged.")
        return []