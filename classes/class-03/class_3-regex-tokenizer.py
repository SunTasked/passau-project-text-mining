import nltk

text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'(?:[a-zA-Z]\.)+|\w+(?:-\w+)*|\$?\d+(?:\.\d+)?%?|\.\.\.|[\.\,\;\"\\\'\?\(\)\:\-\_\`]'
print(nltk.regexp_tokenize(text, pattern))