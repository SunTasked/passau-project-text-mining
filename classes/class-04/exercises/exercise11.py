"""
Create a list of words and store it in a variable sent1. Now assign sent2 = sent1. Modify one of the items in sent1 and verify that sent2 has changed.

Now try the same exercise but instead assign sent2 = sent1[:]. Modify sent1 again and see what happens to sent2. Explain.
Now define text1 to be a list of lists of strings (e.g. to represent a text consisting of multiple sentences. Now assign text2 = text1[:], assign a new value to one of the words, e.g. text1[1][1] = 'Monty'. Check what this did to text2. Explain.
Load Python's deepcopy() function (i.e. from copy import deepcopy), consult its documentation, and test that it makes a fresh copy of any object.
"""

from copy import deepcopy

sent1 = "The quick brown fox jumps over the lazy dog".split()
sent2 = sent1    # same object id because same reference
sent3 = sent1[:] # new object  because Python has to slice the initial list.
sent1[1] = "mighty"

print("sent1 : " + " ".join(sent1))
print("sent2 : " + " ".join(sent2))
print("sent3 : " + " ".join(sent3))

text1 = list(map(lambda sent: sent.split(), """This module contains a number of basic clustering algorithms. Clustering
describes the task of discovering groups of similar items with a large
collection. It is also describe as unsupervised machine learning, as the data
from which it learns is unannotated with class information, as is the case for""".split('\n')))

text2 = text1[:]        # list is a new object but sublists are not
text3 = deepcopy(text1) # list and sublists are new objects

text1[1][5] = "CLUSTERS" #replace groups by CLUSTERS

print("text1 : " + ' '.join(list(map(' '.join, text1))))
print("text2 : " + ' '.join(list(map(' '.join, text2))))
print("text3 : " + ' '.join(list(map(' '.join, text3))))