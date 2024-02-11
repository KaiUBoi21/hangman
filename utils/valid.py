import random 
def word_chooser(wordlists):
    """
    chooses random word for worldist.py
    """
    word = random.choice(wordlists)
    while '-' in word or ' ' in word:
         word = random.choice(wordlists)
    return word.upper()