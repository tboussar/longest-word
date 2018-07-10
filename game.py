# game.py
import string
import random

# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

class Game():
    """docstring for ClassName"""
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
