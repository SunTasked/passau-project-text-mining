"""
Write a function shorten(text, n) to process a text, omitting the n most frequently occurring words of the text. How readable is it?
"""

from collections import Counter
import operator
import nltk

def shorten(text, n):
    vocabulary = dict(Counter(text))
    
    frequent_words = sorted(vocabulary.items(), key=operator.itemgetter(1), reverse=True)

    transformed_text = text[:]
    for word in frequent_words[:n]:
        transformed_text = [w for w in transformed_text if w.lower() != word[0].lower()]

    print(" ".join(transformed_text))


shorten(nltk.corpus.gutenberg.words('austen-emma.txt'), 3)
# Given that punctuation represent the most frequent terms as soon as n > 5, we are lacking a lot of information regarding the structure of the sentences.
    

