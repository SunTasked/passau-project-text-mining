"""
Write code to print out an index for a lexicon, allowing someone to look up words according to their meanings (or pronunciations; whatever properties are contained in lexical entries).
"""

from collections import Counter
import operator
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

lemmatizer = PorterStemmer()
synsets = wn.all_synsets()
stopw = set(stopwords.words('english'))

# will contain the index
vocabulary=dict()

for synset in synsets:
    definition = set([lemmatizer.stem(word) for word in synset.definition().lower().split() if not(word in stopw)])
    for word in definition:
        if word in vocabulary :
            vocabulary[word].append(synset)
        else :
            vocabulary[word] = [synset]

print("index built")
request = "blue bird north american"
request = set([lemmatizer.stem(word) for word in request.lower().split()])
potential_match = []
for word in request:
    if word in vocabulary:
        for match in vocabulary[word]:
            syn_name = match.name()
            potential_match.append(syn_name)

potential_match=sorted(dict(Counter(potential_match)).items(), key=operator.itemgetter(1), reverse=True)
print(potential_match[:5])

