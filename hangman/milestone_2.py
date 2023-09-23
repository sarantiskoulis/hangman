import random
from collections import defaultdict

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.num_letters = len(self.word)
        self.word_guessed = ["_" for i in range(self.num_letters)]
        self.num_lives = num_lives
        self.list_letters = []
        self.character_index = self._character_index(self.word)

        print(f"\nThe mistery word has {self.num_letters} characters")
        print(self.word_guessed)
       
        
    
    @staticmethod
    def _character_index(word):
        character_set = defaultdict(list)
        index = 0
        for letter in word:
            character_set[letter].append(index)
            index += 1
        return character_set

    def check_letter(self, letter) -> None:

        if letter in self.character_index:
            for letter_index in self.character_index[letter]:
                self.word_guessed[letter_index] = letter
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'\nLetter does not exist.\n{self.num_lives} remain.')
            
        
        self.list_letters.append(letter)


    def ask_letter(self):
        while "_" in self.word_guessed and self.num_lives !=0:
            letter = input('\n\nEnter a letter ')
            if len(letter) == 1 and letter not in self.list_letters:
                self.check_letter(letter)

            elif letter in self.list_letters: 
                print(f'The letter "{letter}" has already been chosen')

            elif len(letter) != 1:
                print("Please, enter just one character")
        
        if self.num_lives == 0:
            print(f'The correct word was {self.word}')

            

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
