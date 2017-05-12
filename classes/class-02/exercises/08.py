from nltk.corpus import names
import nltk

cfd = nltk.ConditionalFreqDist(
    (fileid[:4], target)
    for fileid in names.fileids()
    for w in names.words(fileid)
    for target in "abcdefghijklmnopqrstuvwxyz"
    if w.lower().startswith(target)) 

cfd.plot()

