from __future__ import annotations
from abc import ABC, abstractmethod 
from typing import Any


# ---------------------------------------------------------------------------- #
#                                Abstract class                                #
# ---------------------------------------------------------------------------- #
class Iterator(ABC):
    @abstractmethod
    def __next__(self) -> Any:
        pass

class IterableCollection(ABC):
    @abstractmethod
    def __iter__(self) -> Iterator:
        pass

# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #
class WordIterator(Iterator):
    def __init__(self, word_collection:WordCollection, reversed:bool):
        self._word_collection = word_collection
        self._index = 0
        self._reversed = reversed

    def __next__(self) -> str:
        try:
            if self._reversed:
                word = self._word_collection[len(self._word_collection) - self._index - 1]
            else:
                word = self._word_collection[self._index]

        except IndexError:
            raise StopIteration

        self._index += 1
        return word

class WordCollection(IterableCollection):
    def __init__(self, words: list[str]):
        self._words_collection = words.split(' ') if isinstance(words, str) else words

    def __len__(self) -> int:
        return len(self._words_collection)
    
    def __getitem__(self, index: int) -> str:
        if index < 0 or index >= len(self._words_collection):
            raise IndexError("Index out of range")
        return self._words_collection[index]

    def __iter__(self) -> WordIterator:
        return WordIterator(self, reversed=False)

    def get_reverse_iterator(self) -> WordIterator:
        return WordIterator(self, reversed=True)

# ---------------------------------------------------------------------------- #
#                                     Main                                     #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    words = "hello world this is an iterator !"

    # Normal Iterator
    word_collection = WordCollection(words)
    for word in word_collection:
        print(word)
    
    # Reverse iterator (manually because we can only have one real iterator 'in' function per python object)
    word_reverse_iterator = word_collection.get_reverse_iterator()
    while True:
        try:
            word = next(word_reverse_iterator)
            print(word)
        except StopIteration:
            break

# ---------------------------------- Output ---------------------------------- #
# hello
# world
# this
# is
# an
# iterator
# !
# !
# iterator
# an
# is
# this
# world
# hello