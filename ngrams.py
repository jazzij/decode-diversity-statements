import nltk
import os
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

tokenizer = nltk.RegexpTokenizer(r"\w+")  # regex to get all words, including numbers, but not punctuaction

curdir = os.getcwd()
textdir = (r"C:\Users\kumbulat\PycharmProjects\decode-diversity-statements\texts")
newtextdir = (r"C:\Users\kumbulat\PycharmProjects\decode-diversity-statements")
newfilePath = os.path.join(newtextdir, "common_ngrams.txt")
text = []
new_trigrams = []
tokens = []
for filename in os.listdir(textdir):
    filepath = os.path.join(textdir, filename)
    with open(filepath, "r") as file:
        text = file.read()
        tokens = tokenizer.tokenize(text)

        for s in tokens:
            if len(s) == 1 and s == "s":
                tokens.remove(s)
        # print("TOKENS", tokens)

ngram_counts = Counter(ngrams(tokens, 3))
print(" ===NGRAM COUNTS ===")
print(ngram_counts)  # return a dictionary, key is tuple, value is count

print(" === NGRAM KEYS ===")
ngram_keys = ngram_counts.keys()  # keys of the dictionary are the ngrams
print(ngram_keys)

print(" === MOST COMMON ===")
most_common_counts = ngram_counts.most_common(10)
print(most_common_counts)  # return list of nested tuples [((a,b,c), #),]



tokenizer = nltk.RegexpTokenizer(r"\w+")
words = open("uniquewordslist.txt", 'r')
uniqueList = words.read()
token = tokenizer.tokenize(uniqueList)

# print(" === NGRAM KEYS ===")
# ngram_keys = ngram_counts.keys()  # keys of the dictionary are the ngrams
# print(ngram_keys)

for unique_word in token:
    # find word in ngram
    print("***Searching for ", unique_word)
    for ngram in ngram_keys:
        if unique_word in ngram:
            ngrams = (ngram, ngram_counts[ngram])
            print(ngrams)


    file=open("common_ngrams.txt", 'w')
    file.write(", ".join(ngram))
    file.close()