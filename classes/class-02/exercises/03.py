import nltk

genres = ['news',  'romance']

loaded_samples=[]

for idx, genre in enumerate(genres) :
    loaded_samples.append(nltk.corpus.brown.words(categories=genre))
    print("genre " + genre + " --> " + str(len(loaded_samples[idx])) + " words") 