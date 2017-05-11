"""
The polysemy of a word is the number of senses it has. Using WordNet, we can determine that the noun _dog_ has 7 senses with: `len(wn.synsets('dog', 'n'))`. Compute the average polysemy of nouns, verbs, adjectives and adverbs according to WordNet.
"""

from nltk.corpus import wordnet as wn


def average_polysemy(synsets):
    dico = dict()
    i = 0
    for s in synsets :
        i += 1
        name = s.name().split(".")[0]
        if name in dico :
            dico[name] += 1
        else :
            dico[name] = 1

    total_syn = i
    total_diff_words = len(dico)
    return total_syn/total_diff_words

print("average noun polysemy " + str(average_polysemy(wn.all_synsets(wn.NOUN))))
print("average verb polysemy " + str(average_polysemy(wn.all_synsets(wn.VERB))))
print("average adjective polysemy " + str(average_polysemy(wn.all_synsets(wn.ADJ))))
print("average adverb polysemy " + str(average_polysemy(wn.all_synsets(wn.ADV))))