import random
import math
import sys


def get_phrases():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'phrases.txt'
    with open(filename) as textfile:
        phrases = [[word for word in line.strip().split(' ')] for line in textfile]
    return phrases

phrases = get_phrases()

print phrases

def get_word():
    phrase = phrases[random.randint(0,(len(phrases)-1))]
    word = phrase[random.randint(0,(len(phrase)-1))]
    units = math.floor(len(word)/4)
    return word, units
