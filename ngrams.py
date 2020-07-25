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
tokens = []
ngram_counts ={}
newWordsList = []

def all_corpus_ngrams():
    """
    This function is creating the trigrams from the corpus and find the most common 150 trigrams.
    """
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
            most_common_tri = common_ngrams(trigrams)
def common_ngrams(trigrams):

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

    for unique_word in token:
        # find word in ngram
        for ngram in ngram_keys:
            if unique_word in ngram:
                significant = (ngram, ngram_counts[ngram])

                file = open("common_ngrams.txt", 'a+')
                file.write(str(significant))

if __name__ == "__main__":
    all_corpus_ngrams()

