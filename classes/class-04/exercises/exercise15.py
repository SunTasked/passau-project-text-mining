"""
Write a program that takes a sentence expressed as a single string, splits it and counts up the words. Get it to print out each word and the word's frequency, one per line, in alphabetical order.
"""

sent = "I hope that a study of very long sentences will arm you with strategies that are almost as diverse as the sentences themselves, such as: starting each clause with the same word, tilting with dependent clauses toward a revelation at the end, padding with parentheticals, showing great latitude toward standard punctuation, rabbit-trailing away from the initial subject, encapsulating an entire life, and lastly, as this sentence is, celebrating the list.".strip(',:.')

def count_freq(sentence):
    sentence = sentence.lower().split()
    sentence_lenght = len(sentence)
    print("sentence lenght : " + str(sentence_lenght))

    counts = dict()
    for word in sentence:
        if word in counts:
            counts[word] += 1
        else :
            counts[word] = 1

    for w, f in sorted(counts.items()):
        print(w,f)

count_freq(sent)
