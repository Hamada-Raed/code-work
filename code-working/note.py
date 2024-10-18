# import json
# from datetime import datetime

# class Note:
#     """Class to represent a single note with a title, content, and timestamp."""

#     def __init__(self, title: str, content: str):
#         self.title = title
#         self.content = content
#         self.timestamp = datetime.now()

#     def update_content(self, new_content: str):
#         """Update the note's content and refresh the timestamp."""
#         self.content = new_content
#         self.timestamp = datetime.now()

#     def to_dict(self):
#         """Return the note's attributes as a dictionary."""
#         return {
#             'title': self.title,
#             'content': self.content,
#             'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
#         }

#     @staticmethod
#     def from_dict(note_data):
#         """Create a Note instance from a dictionary."""
#         note = Note(note_data['title'], note_data['content'])
#         note.timestamp = datetime.strptime(note_data['timestamp'], '%Y-%m-%d %H:%M:%S')
#         return note

# class NoteManager:
#     """Class to manage a collection of notes."""

#     def __init__(self):
#         self.notes = []

#     def add_note(self, title: str, content: str):
#         """Add a new note to the collection."""
#         note = Note(title, content)
#         self.notes.append(note)
#         print(f"Note '{title}' added.")

#     def get_all_notes(self):
#         """Retrieve all notes."""
#         return self.notes

#     def find_note_by_title(self, title: str):
#         """Find a note by its title."""
#         for note in self.notes:
#             if note.title == title:
#                 return note
#         return None

#     def update_note_by_title(self, title: str, new_content: str):
#         """Update a note's content identified by its title."""
#         note = self.find_note_by_title(title)
#         if note:
#             note.update_content(new_content)
#             print(f"Note '{title}' updated.")
#         else:
#             print(f"Note '{title}' not found.")

#     def delete_note_by_title(self, title: str):
#         """Delete a note identified by its title."""
#         note = self.find_note_by_title(title)
#         if note:
#             self.notes.remove(note)
#             print(f"Note '{title}' deleted.")
#         else:
#             print(f"Note '{title}' not found.")

#     def save_notes_to_file(self, filename: str):
#         """Save all notes to a JSON file."""
#         with open(filename, 'w') as file:
#             json_notes = [note.to_dict() for note in self.notes]
#             json.dump(json_notes, file, indent=4)
#         print(f"Notes saved to '{filename}'.")

#     def load_notes_from_file(self, filename: str):
#         """Load notes from a JSON file."""
#         try:
#             with open(filename, 'r') as file:
#                 json_notes = json.load(file)
#                 self.notes = [Note.from_dict(note_data) for note_data in json_notes]
#             print(f"Notes loaded from '{filename}'.")
#         except FileNotFoundError:
#             print(f"File '{filename}' not found.")

# # Example usage
# if __name__ == "__main__":
#     manager = NoteManager()

#     # Add notes
#     manager.add_note("Shopping List", "Eggs, Milk, Bread")
#     manager.add_note("Work", "Prepare meeting slides")

#     # Get and display all notes
#     notes = manager.get_all_notes()
#     for note in notes:
#         print(note.to_dict())

#     # Update a note
#     manager.update_note_by_title("Shopping List", "Eggs, Milk, Bread, Butter")

#     # Delete a note
#     manager.delete_note_by_title("Work")

#     # Save notes to a file
#     manager.save_notes_to_file("notes.json")

#     # Load notes from a file
#     manager.load_notes_from_file("notes.json") 


import json
from datetime import datetime

# 1. Define a Note class to represent a note

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update(self, new_content):
        """Update the content of the note and reset the timestamp."""
        self.content = new_content
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Convert the note to a dictionary for saving to JSON."""
        return {"title": self.title, "content": self.content, "timestamp": self.timestamp}

    @staticmethod
    def from_dict(data):
        """Create a note from a dictionary."""
        note = Note(data['title'], data['content'])
        note.timestamp = data['timestamp'] # Preserve the original timestamp
        return note

# 2. Create a NoteManager class to manage a collection of notes

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        """Adds a new note with the provided title and content"""
        self.notes.append(Note(title, content))

    def get_notes(self):
        """Retrieve a list of all of the notes."""
        return self.notes

    def find_note_by_title(self, title):
        """Returns a note with the provided title if one exists."""
        for note in self.notes:
            if note.title == title:
                return note
        return None

    def update_note_by_title(self, title, new_content):
        """Updates the content of an existing note by the provided title, if it exists."""
        note = self.find_note_by_title(title)
        if note:
            note.update(new_content)
        else:
            print(f"Note with title '{title}' not found.")

    def delete_note_by_title(self, title):
        """Delete a note by the given title, if it exists."""
        note = self.find_note_by_title(title)
        if note:
            self.notes.remove(note)
        else:
            print(f"Note with title '{title}' not found.")

    def save_to_file(self, filename):
        """Saves all of the notes to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([note.to_dict() for note in self.notes], file)

    def load_from_file(self, filename):
        """Load all the notes from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.notes = [Note.from_dict(item) for item in data]
        except FileNotFoundError:
            print(f"No such file: {filename}")

# 3. Example Usage
if __name__ == "__main__":
    manager = NoteManager()

    # Adding notes
    manager.add_note("Shopping List", "Buy milk, eggs, and bread.")
    manager.add_note("Workout", "Do 30 minutes of cardio.")

    # Retrieving all notes
    print("Current Notes:")
    for note in manager.get_notes():
        print(f"Title: {note.title}, Content: {note.content}, Last Updated: {note.timestamp}")

    # Updating a note
    manager.update_note_by_title("Shopping List", "Buy milk, eggs, bread, and coffee.")
    
    # Deleting a note
    manager.delete_note_by_title("Workout")

    # Saving notes to a file
    manager.save_to_file("notes.json")

    # Loading notes back from the file
    new_manager = NoteManager()
    new_manager.load_from_file("notes.json")
    print("\nNotes after loading from file:")
    for note in new_manager.get_notes():
        print(f"Title: {note.title}, Content: {note.content}, Last Updated: {note.timestamp}")