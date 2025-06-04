import datetime
import string
import random

class LetterGuessException(Exception):
    pass

class LetterBeforeException(LetterGuessException):
    pass

class LetterAfterException(LetterGuessException):
    pass

class NotALetterException(LetterGuessException):
    pass

class LetterGuess:

    letter_pool = list(string.ascii_lowercase)

    def __init__(self):
        self.before = 0
        self.after = 0
        self.start_time = datetime.datetime.now()
        self.letter = None

    def entry_point(self):
        guessed = False
        self.generate_letter()
        while guessed is not True:
            guess = input()
            guessed = self.guess_letter(guess)
            if guessed:
                time_passed = datetime.datetime.now() - self.start_time
                print("guessed!")
                print(f"That's correct! Before: {self.before} times, after: {self.after} times, time to guess: {time_passed}")
            



    def generate_letter(self):
        self.letter = random.choice(self.letter_pool)
    
    def guess_letter(self, letter):
        guessed = False
        try:
            if letter not in self.letter_pool:
                raise NotALetterException("Select a valid leter")
            if letter == self.letter:
                guessed = True
            elif self.letter_pool.index(letter) > self.letter_pool.index(self.letter):
                raise LetterAfterException("Go down")
            else:
                raise LetterBeforeException("Go up")
            
        except NotALetterException:
            print("Input must be a letter")
        except LetterAfterException:
            self.after += 1
            print("Go down")
        except LetterBeforeException:
            self.before += 1
            print("Go up")
        finally:
            return guessed
        
lg = LetterGuess()
lg.entry_point()
           