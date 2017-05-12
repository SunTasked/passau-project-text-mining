import nltk 

latin_fileids = [x for x in nltk.corpus.udhr.fileids() if x[-7:] == "-Latin1"]
dictionnary = dict()
for file in latin_fileids:
    words = nltk.corpus.udhr.words(file)
    lang = file[:-7]

    for w in words:
        if w in dictionnary:
            if not (lang in dictionnary[w]):
                dictionnary[w].append(lang)
            else:
                continue
        else :
            dictionnary[w] = [lang]

print(dictionnary["des"])