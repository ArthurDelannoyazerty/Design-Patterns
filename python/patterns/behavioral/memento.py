from __future__ import annotations
from abc import ABC, abstractmethod 
from typing import Any

import time

# ---------------------------------------------------------------------------- #
#                                Abstract Class                                #
# ---------------------------------------------------------------------------- #
class Memento(ABC):
    @abstractmethod
    def get_save(self) -> Any:
        pass


class Originator(ABC):
    @abstractmethod
    def save(self) -> Memento:
        pass

# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #
class TextEditorSnapshot(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    def get_save(self) -> str:
        return self._state
    


class TextEditor(Originator):
    def __init__(self, state: str) -> None:
        self._state = state

    def write(self, text: str) -> None:
        self._state += text

    def save(self) -> TextEditorSnapshot:
        return TextEditorSnapshot(self._state)

    def restore(self, snapshot: TextEditorSnapshot) -> None:
        self._state = snapshot.get_save()
    
    def display(self) -> None:
        print(self._state)


class History:
    def __init__(self, originator: TextEditor) -> None:
        self._mementos:list[TextEditorSnapshot] = []
        self._originator = originator

    def backup(self) -> None:
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not self._mementos:
            return

        memento = self._mementos.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()


# ---------------------------------------------------------------------------- #
#                                     Main                                     #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    editor = TextEditor("This is the first sentence.")
    editor.display()

    history = History(editor)

    history.backup()
    editor.write(" This is the second.")
    editor.display()

    history.backup()
    editor.write(" And this is the third.")
    editor.display()

    print()
    history.undo()
    editor.display()
    history.undo()
    editor.display()

# ---------------------------------- Output ---------------------------------- #
# This is the first sentence.
# This is the first sentence. This is the second.
# This is the first sentence. This is the second. And this is the third.
#
# This is the first sentence. This is the second.
# This is the first sentence.