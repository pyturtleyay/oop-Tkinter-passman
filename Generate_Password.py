import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def generatePassword(length=8):
    generator = LETTERS+NUMBERS+PUNCTUATION
    generator = list(generator)
    random.shuffle(generator)
    password = ''
    for i in range(length):
        password=password+generator[i]
    return password

