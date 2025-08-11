from __future__ import annotations
from abc import ABC, abstractmethod

# ---------------------------------------------------------------------------- #
#                                Abstract class                                #
# ---------------------------------------------------------------------------- #
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

# ---------------------------------------------------------------------------- #
#                                Concrete class                                #
# ---------------------------------------------------------------------------- #

# --------------------------------- Receiver --------------------------------- #
class Document:
    def __init__(self):
        self.text = ""
        self.cursor_pos = 0

    def insert(self, text_to_insert):
        """Inserts text at the current cursor position."""
        self.text = self.text[:self.cursor_pos] + text_to_insert + self.text[self.cursor_pos:]
        self.cursor_pos += len(text_to_insert)
        print(f'Current Text: "{self.text}"')

    def delete(self, length):
        """Deletes text backwards from the current cursor position."""
        if self.cursor_pos < length:
            length = self.cursor_pos

        # Store the text that will be deleted so we can undo it
        start = self.cursor_pos - length
        end = self.cursor_pos
        deleted_text = self.text[start:end]

        self.text = self.text[:start] + self.text[end:]
        self.cursor_pos -= length
        print(f'Current Text: "{self.text}"')
        return deleted_text # Return the deleted text for the command to store


# --------------------------------- Commands --------------------------------- #
class InsertCommand(Command):
    def __init__(self, document:Document, text:str):
        self._document = document
        self._text = text

    def execute(self):
        self._document.insert(self._text)

    def undo(self):
        # To undo an insert, we delete the text we just inserted.
        self._document.delete(len(self._text))

class DeleteCommand(Command):
    """A concrete command to delete text (like a backspace)."""
    def __init__(self, document:Document, length:int=1):
        self._document = document
        self._length = length
        self._deleted_text = None # Will store the deleted text here

    def execute(self):
        # We must store the deleted text so we can restore it on undo.
        self._deleted_text = self._document.delete(self._length)

    def undo(self):
        # To undo a delete, we re-insert the text we previously deleted.
        if self._deleted_text:
            self._document.insert(self._deleted_text)


# ---------------------------------- Invoker --------------------------------- #
class Editor:
    def __init__(self):
        self._document = Document()
        self._history:list[Command] = []

    def type(self, text):
        """Simulates the user typing text."""
        print(f'>> User types: "{text}"')
        command = InsertCommand(self._document, text)
        self.execute_command(command)

    def backspace(self, count=1):
        """Simulates the user pressing backspace."""
        print(f'>> User hits backspace {count} time(s).')
        command = DeleteCommand(self._document, count)
        self.execute_command(command)

    def execute_command(self, command: Command):
        command.execute()
        self._history.append(command) # Add to our history list

    def undo(self):
        """Undoes the last executed command."""
        if not self._history:
            print("Nothing to undo.")
            return

        print(">> User hits UNDO.")
        last_command = self._history.pop()
        last_command.undo()


# ---------------------------------------------------------------------------- #
#                                 Main / Client                                #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    editor = Editor()

    # Simulate a user writing a sentence
    editor.type("Hello, this is the Command Pattern.")
    editor.type(" It's great!")
    
    # Simulate a mistake and correction
    editor.backspace(7) # Deletes "great!"
    editor.type(" awesome!")

    print("\n--- Final text before undo ---")
    print("\n--- Starting UNDO sequence ---\n")

    # Now, let's undo the actions one by one
    editor.undo() # Undoes typing " awesome!"
    editor.undo() # Undoes backspacing "great!"
    editor.undo() # Undoes typing " It's great!"
    editor.undo() # Undoes typing "Hello, this is the Command Pattern."
    editor.undo() # Tries to undo again, but history is empty


# ---------------------------------- Output ---------------------------------- #
# >> User types: "Hello, this is the Command Pattern."
# Current Text: "Hello, this is the Command Pattern."
# >> User types: " It's great!"
# Current Text: "Hello, this is the Command Pattern. It's great!"  
# >> User hits backspace 7 time(s).
# Current Text: "Hello, this is the Command Pattern. It's"
# >> User types: " awesome!"
# Current Text: "Hello, this is the Command Pattern. It's awesome!"
#
# --- Final text before undo ---
#
# --- Starting UNDO sequence ---
#
# >> User hits UNDO.
# Current Text: "Hello, this is the Command Pattern. It's"
# >> User hits UNDO.
# Current Text: "Hello, this is the Command Pattern. It's great!"  
# >> User hits UNDO.
# Current Text: "Hello, this is the Command Pattern."
# >> User hits UNDO.
# Current Text: ""
# Nothing to undo.