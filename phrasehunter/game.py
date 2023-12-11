import random
from phrasehunter.phrase import Phrase

class Game():

    def __init__(self):
        self.missed = 0
        self.phrases = ['hello world', 'there is no trying', 'may the force be with you', 
        'you have to see the matrix for yourself', 'life is like a box of chocolates']
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ']

    def start(self):
        self.welcome()

        while self.missed < 5  and self.active_phrase.check_complete(self.guesses) == False:
            print(f'Number missed: {self.missed}\n\n')
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            if user_guess:
                self.guesses.append(user_guess)
                if not self.active_phrase.check_guess(user_guess):
                    self.missed += 1
        self.game_over()
        print('\n\n')
            

    def get_random_phrase(self):
        phrase = Phrase(random.choice(self.phrases))
        return phrase

    def welcome(self):
        print('''
        ____________________

        Welcome to the game.
        ____________________
        ''')

    def get_guess(self):
        guess = input('\n\nGuess a letter:   ')
        try:
            if guess.isalpha() and len(guess) == 1:
                return guess
            if not guess.isalpha():
                raise Exception(f'that is not a letter. Please try again.')
            if len(guess) > 1:
                raise Exception(f'you may only guess one letter at a time. Please try again.')
        except Exception as e:
            print(f"\nError: {e}")


    def game_over(self):
        if self.missed == 5:
            print('\nBummer... you lose.\n')
        else:
            print(f"\nWhoop whoop. You guess it. \n\n The phrase is '{self.active_phrase.phrase.upper()}'!\n")

        again = input('Would you like to play again?  Y/N'   )
        if again.upper() == 'Y':
            self.missed = 0
            self.active_phrase = self.get_random_phrase()
            self.guesses = [' ']
            self.start()
        else:
            print('ok, thanks for playing.')
            break



