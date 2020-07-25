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
ngram_counts ={}
newWordsList = []
def all_corpus_ngrams():
    for filename in os.listdir(textdir):
        filepath = os.path.join(textdir, filename)
        with open(filepath, "r") as file:
            text = file.read()
            tokens = tokenizer.tokenize(text)

            for s in tokens:
                if len(s) == 1 and s == "s":
                    tokens.remove(s)

            trigrams = Counter(ngrams(tokens, 3))  # return a dictionary, key is tuple, value is count
            ngram_counts.update(trigrams)
            all_texts = significant_ngrams(trigrams)

            for i in trigrams:
                newWordsList.append(i)

            grams = Counter(ngrams(newWordsList, 3))
            common_counts = grams.most_common(150)
    return common_counts

def significant_ngrams(trigrams):


    tokenizer = nltk.RegexpTokenizer(r"\w+")
    words = open("uniquewordslist.txt", 'r')
    uniqueList = words.read()
    token = tokenizer.tokenize(uniqueList)


    ngram_keys = trigrams.keys()  # keys of the dictionary are the ngrams
    # print(ngram_keys)


    for unique_word in token:
        # find word in ngram
        # print("***Searching for ", unique_word)
        for ngram in ngram_keys:
            if unique_word in ngram:
                significant = (ngram, ngram_counts[ngram])


                file = open("common_ngrams.txt", 'a+')
                file.write(str(significant))

if __name__ == "__main__":
    all_corpus_ngrams()

