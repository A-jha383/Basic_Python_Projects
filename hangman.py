import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print('You have ', lives, ' lives left. You have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letters = input('Guess a letter:').upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                lives = lives - 1
                print('Letter is not in the word.')
        elif user_letters in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid Character.Please try it again.')
    if lives == 0:
        print('You died, Sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


hangman()
