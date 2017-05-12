###############################################################################
##############################  ZIPF'S LAW ####################################
###############################################################################


import nltk
import operator
import matplotlib.pyplot as plt
import math


def get_words_ranks_freqs(text_words=[]):

    # compute word frequencies
    words = dict()
    for word in text_words:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    
    # compute word ranks
    sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_words
    
sorted_ws = get_words_ranks_freqs(nltk.corpus.gutenberg.words('austen-emma.txt'))

words = []
freqs = []
zipf = []
zipf_law_max = sorted_ws[0][1]
ranks = []
rank = 1
for idx, (word, freq) in enumerate(sorted_ws):
    if not(freqs) or freq != sorted_ws[idx-1][1]:
        freqs.append(math.log(freq))
        zipf.append(math.log(zipf_law_max / rank))
        ranks.append(rank)
        rank += 1

plt.plot(ranks, freqs, label="frequencies")
plt.plot(ranks, zipf, label="zipf")
plt.ylabel('frequencies (log10)')
plt.xlabel('rank')
plt.show()

# the curves don't look that similar...
