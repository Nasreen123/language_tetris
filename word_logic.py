import random
import math

"""sentences = [
['bonne', 'chance'],
['bonne', 'annee'],
['quelle', 'chance'],
['annee', 'prochaine'],
['une', 'annee'],
['une', 'chance']
]
"""
sentences = [
['one', 'two', 'three'],
['four', 'five', 'six']
]

#sentences_sets = [set(l) for l in sentences]

def get_word():
    sentence = sentences[random.randint(0,(len(sentences)-1))]
    word = sentence[random.randint(0,(len(sentence)-1))]
    units = math.floor(len(word)/4)
    #print word, 'LENGTH: ', len(word), 'UNITS: ', units
    return word, units

#def check_if_sentence(word1, word2):
#    return set([word1, word2]) in sentences_sets
