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

#Finding the words that stemmed and lemmatized and return them as final stem and leaf
    for w in tokens:
        stemmed_words.append(ps.stem(w))
    for w in stemmed_words:
        lemmatized_words.append(wn.lemmatize(w))

    for i in range(len(lemmatized_words)):

        if lemmatized_words[i] not in new_dict.keys():
            if lemmatized_words[i] != tokens[i]:
                new_dict[lemmatized_words[i]] = [tokens[i]]
        else:
            if lemmatized_words[i] != tokens[i]:
                a = new_dict[lemmatized_words[i]]
                if tokens[i] not in a:
                    a.append(tokens[i])
                    new_dict[lemmatized_words[i]] = a


    for j, k in new_dict.items():
        new_str = ""

        for i in range(len(k)):
            new_str += k[i]
            if i != (len(k) - 1):
                new_str += ","
            newStr = j + " " + "|" + " " + new_str
            allWords.append(newStr)
uniqueWords = set(allWords[:])  # This removes the duplicates of words after stemming and lemmatization
for i in uniqueWords:
    duplicates_free.append(i)

    def Sorting(lst):
        lst2 = sorted(lst, key=len)
        return lst2


    x = Sorting(duplicates_free)
    x2 = x[::-1]  # this is reversing the  list

    for i in x2:
        print(i)