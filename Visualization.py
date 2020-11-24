import re
import string
import nltk
from nltk.tokenize import word_tokenize
import nltk
import os
import itertools
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

wn = nltk.WordNetLemmatizer()
ps = PorterStemmer()

lemmatized_words = []
stemmed_words = []
my_list = []
new_dict = {}
modified_words = []
text = []
tokens = []
allWords = []
duplicates_free = []

tokenizer = nltk.RegexpTokenizer(r"\w+")

curdir = os.getcwd()
textdir = os.path.join(os.getcwd(), "texts")

for filename in os.listdir(textdir):
    filepath = os.path.join(textdir, filename)
    if os.path.isfile(filepath):
        text = open(filepath, "r")
        text = text.read()

        file = open("alltexts.txt", "a+")  # Creating a new text file that contain all the texts
        file.write(str(text) + "\n")
        file.close()

with open("alltexts.txt", "r") as file:
    text = file.read()
    tokens = tokenizer.tokenize(text)

# Finding the words that stemmed and lemmatized and return them as final stem and leaf
    for w in tokens:
        stemmed_words.append(ps.stem(w))
    for w in stemmed_words:
        lemmatized_words.append(wn.lemmatize(w))


    for i in range(len(lemmatized_words)):  # Checking if lemmatized_words contain keys in new_dict

        if lemmatized_words[i] not in new_dict.keys():
            if lemmatized_words[i] != tokens[i]:
                new_dict[lemmatized_words[i]] = [tokens[i]]
        else:                                     # Finding all the words which have the same root/stem
            if lemmatized_words[i] != tokens[i]:
                a = new_dict[lemmatized_words[i]]
                if tokens[i] not in a:
                    a.append(tokens[i])
                    new_dict[lemmatized_words[i]] = a

    allWords = []
    for j, k in new_dict.items():

        new_str = ""
        newStr = ""
        for i in range(len(k)):
            new_str += k[i]
            if i != (len(k) - 1):
                new_str += ","
            newStr = j + " " + "|" + " " + new_str
        if newStr not in allWords:
            allWords.append(newStr)

    allWords.sort()  # Sorts alphabetical order if the length of the leaf is the same
    allWords.sort(key=len, reverse=True)  # Sorts the leaf by descending length
    print("NUMBER OF STEMS:", len(allWords))
    for i in allWords:
        print(i)  # Stems



