"""
What is the branching factor of the noun hypernym hierarchy? I.e. for every noun synset that has hyponyms — or children in the hypernym hierarchy — how many do they have on average? You can get all noun synsets using `wn.all_synsets('n')`.
"""

from nltk.corpus import wordnet as wn

total = i = 0
for s in wn.all_synsets('n') :
    ln = len(s.hypernyms())
    if ln != 0 :
        total += ln
        i += 1
print("The branching factor of the noun hypernym hierarchy is %f" % (total / i))