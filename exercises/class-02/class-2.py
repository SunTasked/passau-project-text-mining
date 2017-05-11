import nltk

# Exercise 1 : Carry out the concordance analysis for the word suprise within the text Emma
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
#emma.concordance("surprize")

# Exercise 2 : Choose a section of the Brown Corpus, and count a selection of wh words, such as what, when, where, who, and why.
news_text = nltk.corpus.brown.words(categories='fiction')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['what', 'when', 'where', 'who', 'why']
print("Count of wh words appearance in brown corpus' fiction: ")
for m in modals:
     print('    - ' + m + ':', fdist[m])
print()


# Exercise 3 : Pick a language of interest in udhr.fileids(), and define a variable raw_text = udhr.raw(Language-Latin1). 
#              Now plot a frequency distribution of the letters of the text using nltk.FreqDist(raw_text).plot().

raw_text = nltk.corpus.udhr.raw("English-Latin1")

cfd = nltk.ConditionalFreqDist(
           ("alphabet", letter)
           for letter in "abcdefghijklmnopqrstuvwxyz"
           for text_letter in raw_text
           if text_letter.lower() == letter)
cfd.tabulate()


# Exercise 4 : Working with the news and romance genres from the Brown Corpus, find out which days of the week are most newsworthy, and which are most romantic. Define a variable called days containing a list of days of the week, i.e. ['Monday', ...]. Now tabulate the counts for these words using cfd.tabulate(samples=days). Now try the same thing using plot in place of tabulate. You may control the output order of days with the help of an extra parameter: samples=['Monday', ...].

from nltk.corpus import brown

genres = ['news',  'romance']
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in genres
        for word in brown.words(categories=genre))
cfd.tabulate(samples=days)


# Exercise 5 : Write down all the senses of the word dish that you can think of. Now, explore this word with the help of WordNet, using the same operations we used above

from nltk.corpus import wordnet as wn

# Uncomment for ugly prints
"""print(wn.lemmas('dish'))
for synset in wn.synsets('dish'):
    print(synset.lemma_names())"""

# Exercise 6 : Try out NLTK's convenient graphical WordNet browser: nltk.app.wordnet(). Explore the WordNet hierarchy by following the hypernym and hyponym links.

# nltk.app.wordnet()


# Exercise 6