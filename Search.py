"""
Description: Word/Phrase search functions
Author: Jonathan Spurling
Date Created: February 22, 2024

Updates: none
"""

class Search():
    """Class that holds functions that search phrases/objects"""
    def __init__(self):
        self.letters = ""
        self.phrase = ""


    def search_for_vowels(self, phrase: str) -> set:
        """Return any vowels found in a supplied phrase"""
        vowels = set('aeiou')
        self.phrase = set(phrase.lower())
        return vowels.intersection(self.phrase)

    def search_for_letters(self, phrase:str, letters:str='aeiou') -> set:
        """Return any letters found in a supplied phrase from a set of letters to search"""
        self.letters = set(letters.lower())
        self.phrase = set(phrase.lower())

        return self.letters.intersection(self.phrase)
