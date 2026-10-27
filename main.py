"""
Program: Note Taking App
Author: Caleb Gebrezgi
Purpose: Menu to add and view notes
Date: 10-27-2026
"""

from notes_app.note_management import NoteManager


def show_menu():
    """Print menu options."""
    print("\n--- Note Taking App ---")
    print("1. Add notes")
    print("2. View notes")
    print("3. Exit")


def print_notes(notes):
    """Print a list of notes, or a message if no notes are found."""
    if not notes:
        print("No notes found.")
        return
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note.title}: {note.body}")


def add_note(manager):
    """Asks the user for a title and body, then adds and saves the note."""
    title = input("Title: ")
    body = input("Body (optional): ")
    try:
        manager.add_note(title, body)
    except ValueError as error:
        print(f"Note could not be added: {error}")
        return
    manager.save()
    print("Note added.")


def main():
    """Load saved notes, then run the menu until the user exits."""
    manager = NoteManager()
    manager.load()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_note(manager)
        elif choice == "2":
            print_notes(manager.list_notes())
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please pick 1-3.")


if __name__ == "__main__":
    main()