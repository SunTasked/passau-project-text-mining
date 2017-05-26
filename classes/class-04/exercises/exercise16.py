"""
Read up on Gematria, a method for assigning numbers to words, and for mapping between words having the same number to discover the hidden meaning of texts (http://en.wikipedia.org/wiki/Gematria,  http://essenes.net/gemcal.htm).
Write a function gematria() that sums the numerical values of the letters of a word, according to the letter values in letter_vals.
Process a corpus (e.g. nltk.corpus.state_union) and for each document, count how many of its words have the number 666.
"""

import nltk

letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
    'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
    'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}

def get_gematria(text): # code golf version
    return list( set( filter( lambda w: sum(map(lambda l: 0 if not (l in letter_vals) else letter_vals[l], w.lower()))==666, text) ) )

for id in nltk.corpus.state_union.fileids():
    text = list(set(nltk.corpus.state_union.words(id)))
    n_gemat_666 = len(get_gematria(text))
    print(id + " : " + str(n_gemat_666))