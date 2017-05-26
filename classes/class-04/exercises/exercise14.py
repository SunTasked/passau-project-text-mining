""" 
Write a function novel10(text) that prints any word that appeared in the last 10% of a text that had not been encountered earlier.
"""
import nltk

def novel10(words) : 
    """
    Prints any word that appeared in the last 10% of a text that had not been encountered earlier.
    """

    cut = int(0.9 * len(words))
    first_90, last_10 = set(words[:cut]), words[cut:]
    
    for word in last_10:
        if not(word in first_90):
            print(word, end=' ')

novel10(nltk.corpus.gutenberg.words('austen-emma.txt'))