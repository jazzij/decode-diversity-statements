import nltk
import os
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

tokenizer = nltk.RegexpTokenizer(r"\w+")  # regex to get all words, including numbers, but not punctuaction

curdir = os.getcwd()
textdir = (r"C:\Users\kumbulat\PycharmProjects\decode-diversity-statements\texts")
newtextdir = (r"C:\Users\kumbulat\PycharmProjects\decode-diversity-statements")
newfilePath = os.path.join(newtextdir, "Significant wordlist_ngrams.txt")

text = []
tokens = []
ngram_counts ={}
newWordsList = []

def all_corpus_ngrams():
    """            
    This function is creating the trigrams from the corpus and find the most common 150 trigrams.
    return: common_counts
    """
    for filename in os.listdir(textdir)[:]:
        filepath = os.path.join(textdir, filename)
        with open(filepath, "r") as file:
            text = file.read()
            tokens = tokenizer.tokenize(text)

            for s in tokens:   # This removes the single letter s
                if len(s) == 1 and s == "s":
                    tokens.remove(s)

            trigrams = Counter(ngrams(tokens, 3))  # return a dictionary, key is tuple, value is count
            ngram_counts.update(trigrams)
            significant_ngrams(trigrams)  # Calling the next function
    ngram = Counter(ngram_counts)
    common_counts = ngram.most_common(150)
    return common_counts

def significant_ngrams(trigrams):
    """
    This function compares the unique words with all the texts ngrams.
     It also create a new text file with significant words trigrams.

    """
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    words = open("uniquewordslist.txt", 'r')
    uniqueList = words.read()
    tokens = tokenizer.tokenize(uniqueList)
    words.close()

    ngram_keys = trigrams.keys()  # keys of the dictionary are the ngrams

    for unique_word in  tokens:
        # find word in ngram
        for ngram in ngram_keys:
            if unique_word in ngram:
                significant = (ngram, ngram_counts[ngram])  #

                file = open("Significant wordlist_ngrams.txt", "a+")
                file.write(str(significant)+ "\n")
                file.close()

if __name__ == "__main__":
   gram = all_corpus_ngrams()
   print(gram)




