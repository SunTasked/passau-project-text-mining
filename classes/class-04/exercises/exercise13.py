"""
Write code to initialize a two-dimensional array of sets called word_vowels and process a list of words, adding each word to word_vowels[l][v] where l is the length of the word and v is the number of vowels it contains.
"""


from numpy import array
from tabulate import tabulate

sent = "I hope that a study of very long sentences will arm you with strategies that are almost as diverse as the sentences themselves, such as: starting each clause with the same word, tilting with dependent clauses toward a revelation at the end, padding with parentheticals, showing great latitude toward standard punctuation, rabbit-trailing away from the initial subject, encapsulating an entire life, and lastly, as this sentence is, celebrating the list.".strip(',:.').split()

def count_vowels(word):
    return len(list(filter(lambda l: l in 'aeiouy', word.lower())))

counts = [(word, len(word), count_vowels(word)) for word in sent]
print(counts)

word_vowels = array([[set() for x in range(max(list(map(lambda l: l[2], counts))))] for y in range(max(list(map(lambda l: l[1], counts))))])

for c in counts:
    word_vowels[c[1]-1][c[2]-1].add(c[0])

print(tabulate(word_vowels,headers=(x+1 for x in range(len(word_vowels)))))