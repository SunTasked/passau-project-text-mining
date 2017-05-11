'''
    1. Store the _n_ most likely words in a list `words` then randomly choose a word from the list using `random.choice()`. (You will need to `import random` first.)
    2. Select a particular genre, such as a section of the Brown Corpus, or a genesis translation, one of the Gutenberg texts, or one of the Web texts. Train the model on this corpus and get it to generate random text. You may have to experiment with different start words. How intelligible is the text? Discuss the strengths and weaknesses of this method of generating random text.
    3. Now train your system using two distinct genres and experiment with generating text in the hybrid genre. Discuss your observations.
'''
import nltk
from nltk.corpus import brown
import random

def get_rand_word(category, n_words):
    cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in [category]
        for word in brown.words(categories=genre))
    most_common_words = cfd[category].most_common(20)
    rand_word = random.choice(most_common_words)
    return rand_word[0]

def build_model(text):
    bigrams = nltk.bigrams(text)
    cfd = nltk.ConditionalFreqDist(bigrams)
    return cfd

def generate_text(cfdist, word, text_length):
    generated_text = ''
    for i in range(text_length):
        generated_text += word + " "
        word = cfdist[word].max()
    return generated_text

n_words_lottery = 200
categories = ['adventure', 'belles_lettres', 'editorial']
rand_category = "belles_lettres"
gen_text_lenght = 100


words = []
for c in categories:
    words += brown.words(categories=c)

rand_word = get_rand_word(rand_category, n_words_lottery)
print ("random word selected : " + rand_word + "\n")

print("building model\n")
model = build_model(words)

print("resulting text : ")
text = generate_text(model, rand_word, gen_text_lenght)

print (text)