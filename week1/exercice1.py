"""
I want you to write a function that will create an acronym from a sentence.
The function, which I've called "acrobot", takes a string as an argument, and returns a string.
The returned string should be an acronym based on the input string.
I would like your function to take an optional second argument, min_word_length.  If this receives an integer argument,
then it only considers words of at least that length in constructing the acronym.
acrobot("certificate of deposit")
    "COD"
acrobot("certificate of deposit", min_word_length=3)
    "CD"
"""


# sentence = input("enter a word: ")


def acrobot(phrase, min_word_length=2):
    for word in phrase.split():
        # first_letter = list()
        if len(word) >= min_word_length:
            first_letter = [word[0].title()]
            return ''.join(first_letter)


def acrobot(phrase, min_word_length=0):
    answer = [word[0].title() for word in phrase.split() if len(word) >= min_word_length]
    return ''.join(answer)


# CORRECTION LIST COMPREHENSION
def acrobot(sentence, min_word_length=0):
    return ''.join([one_word[0] for one_word in sentence.split() if len(one_word) >= min_word_length]).upper()

# acrobot(sentence, min_word_length=3)
