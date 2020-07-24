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

for filename in os.listdir(textdir):
    filepath = os.path.join(textdir, filename)
    with open(filepath, "r") as file:
        text = file.read()
        tokens = tokenizer.tokenize(text)

        for s in tokens:
            if len(s) == 1 and s == "s":
                tokens.remove(s)
        # print("TOKENS", tokens)
        trigrams = Counter(ngrams(tokens, 3))
        # print("This is the trigram",trigrams)
        # for key,value in trigrams.items():
        #     print(key)
        ngram_counts.update(trigrams)


        # print(" ===NGRAM COUNTS ===")
        # print(ngram_counts)  # return a dictionary, key is tuple, value is count

        print(" === MOST COMMON ===")
        most_common_counts = trigrams.most_common(10)
        print(most_common_counts)
        for i in most_common_counts:
            for j in i[0]:
                newWordsList.append(j)
        grams = Counter(ngrams(newWordsList, 3))
        common_counts = grams.most_common(30)
print(common_counts)

file = open("common_ngrams.txt", 'a+')
file.write(str(common_counts))
    # for j in i[0]:
    #     file.write(j)
    #     file.write(" ")



# print("This is most NWL words",t)

#         newStr += str(most_common_counts)
#
#         print("Most common counts",most_common_counts)  # return list of nested tuples [((a,b,c), #),]
# revStr=""
# unwanted = "[]{}�()"
# for i in newStr:
#     if i not in unwanted:
#         revStr+=i
#
# file = open("common_ngrams.txt", 'w')
# file.write(revStr)


tokenizer = nltk.RegexpTokenizer(r"\w+")
words = open("uniquewordslist.txt", 'r')
uniqueList = words.read()
token = tokenizer.tokenize(uniqueList)

# print(" === NGRAM KEYS ===")
ngram_keys = ngram_counts.keys()  # keys of the dictionary are the ngrams
# print(ngram_keys)


for unique_word in token:
    # find word in ngram
    # print("***Searching for ", unique_word)
    for ngram in ngram_keys:
        if unique_word in ngram:
            pass
            # print(ngram, ngram_counts[ngram])

