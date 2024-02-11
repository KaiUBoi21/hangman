#file for the hangman game
from utils.valid import word_chooser
from utils.wordlist import words
from utils.visual import lives_visual_dict
import string

def hangman():
    word = word_chooser(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    lives = 7
    used_letters = set()

    #start game
    while  lives > 0:
        print("welcome to Hangman\n")
        print(f"you have {lives} remaining")
        print(f"you have used {used_letters} in your guess")

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print("current word:", word_list)

        user_letter = input("Guess a letter: ").upper()
    #check if user_letter is in alphabet and not in used set
        if user_letter in used_letters:
            print("You have already guessed this, try again")
        elif user_letter in alphabet:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                #word_letters is [x,y]
                #user guessed x
                #remove x from the word_letters
                word_letters.remove(user_letter)
        else:
                lives = lives - 1
                print(f"the letter{user_letter} is not correct")
                print("That is not a valid letter")




    





if __name__ == '__main__':
    hangman()