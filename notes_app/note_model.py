"""
Program: Note Taking App
Author: Caleb Gebrezgi
Purpose: Defines the Note class
Date: 10-20-2026
"""

class Note:
    """A singular note with both a title and a body."""

    def __init__(self, title, body=""):
        """Create a note with a title and optional body text.

        Program fails to run if no title is entered.
        """
        if title.strip() == "":
            raise ValueError("Title cannot be empty")
        self.title = title.strip()
        self.body = body

    def to_dict(self):
        """Return notes as a dictionary so they can be saved as JSON."""
        return {"title": self.title, "body": self.body}

    @classmethod
    def from_dict(cls, data):
        """Build a note from a dictionary and load it from JSON."""
        return cls(data["title"], data["body"])