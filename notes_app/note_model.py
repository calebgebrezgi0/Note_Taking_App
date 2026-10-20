"""
Program: Note Taking App
Author: Caleb Gebrezgi
Purpose: Defines the Note class
Date: 10-20-2026
"""

class Note:
    """A singular note with both a title and a body."""

    def __init__(self, title, body=""):
        """Create a note with a title and optional body text."""
        self.title = title
        self.body = body