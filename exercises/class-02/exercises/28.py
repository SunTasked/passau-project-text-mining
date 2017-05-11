"""
Use one of the predefined similarity measures to score the similarity of each of the following pairs of words. Rank the pairs in order of decreasing similarity. How close is your ranking to the order given here, an order that was established experimentally by [(Miller & Charles, 1998)][39]:
"""
from nltk.corpus import wordnet as wn
from operator import itemgetter

pairs = ["car-automobile", "gem-jewel", "journey-voyage", "boy-lad", "coast-shore", "asylum-madhouse", "magician-wizard", "midday-noon", "furnace-stove", "food-fruit", "bird-cock", "bird-crane", "tool-implement", "brother-monk", "lad-brother", "crane-implement", "journey-car", "monk-oracle", "cemetery-woodland", "food-rooster", "coast-hill", "forest-graveyard", "shore-woodland", "monk-slave", "coast-forest", "lad-wizard", "chord-smile", "glass-magician", "rooster-voyage", "noon-string"]
pairs = [[pair, 0] for pair in pairs]

for p in pairs :
    word1, word2 = p[0].split('-')
    syn1 = wn.synsets(word1, 'n')
    syn2 = wn.synsets(word2, 'n')
    for s1 in syn1:
        for s2 in syn2:
            p[1] = max(p[1], s1.lch_similarity(s2))


for p in sorted(pairs, key=itemgetter(1), reverse=True) :
    print(p[0] + " : " + str(p[1]))
