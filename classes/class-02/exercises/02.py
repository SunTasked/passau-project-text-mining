import nltk

persuasion = nltk.corpus.gutenberg.words('austen-persuasion.txt')

print("number of word in austen-persuasion.txt : " + str(len(persuasion)))

tags = nltk.pos_tag(persuasion)

cfd = nltk.ConditionalFreqDist(
           ("pos_tags", tag)
           for word, tag in tags)
cfd.plot()