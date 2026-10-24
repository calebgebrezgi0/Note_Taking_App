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