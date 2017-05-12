from nltk.corpus import state_union
import nltk

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in state_union.fileids()
    for w in state_union.words(fileid)
    for target in ["people", "men", "women"]
    if w.lower().startswith(target)) 

cfd.plot() # Can't really depict a noticeable evolution.