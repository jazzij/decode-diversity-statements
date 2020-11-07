import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist
import matplotlib.pyplot as plt


curdir = os.getcwd()
textdir = (r"C:\Users\kumbulat\PycharmProjects\decode-diversity-statements\texts")
myList = []

def stop_words(text):
    """
    This function is for removing the stopwords from the text file.
    Filename: Name of the file
    return: filtered_words
    """
    filtered_words = []
    stop_words = set(stopwords.words('english')) # Creating a List of stopwords
    for w in text:
        if w not in stop_words:
            filtered_words.append(w)    # Add all words after stopwords have been removed
    #print("FilteredWords:", filtered_words)
    return filtered_words

def termfrequency():
    """
    This function is supposed to calculate the term frequency of the text in file.
    Filename: Name of the file
    return: term frequency
    """
    for filename in os.listdir(textdir)[:]:
        filepath = os.path.join(textdir, filename)
        with open(filepath, "r") as file:
            text = file.read()
            tokens = nltk.word_tokenize(text)

            words = stop_words(tokens)
            modifiedTexts = modified_files(words)
            print("DUPLICATES FREE:",modifiedTexts )
def modified_files(tokens):
    """
    This function is supposed to stem the words that end with -ing and lemmatize the rest. It is also supposed to remove duplicates of words.
    filename: Name of text files
    return: duplicates free
    """
    modified_words = []
    duplicates_free = []
    wn = nltk.WordNetLemmatizer()
    ps = PorterStemmer()

    for w in tokens:
        if w[-3:] == "ing":  # Checks for the words that end with -ing and they going through stemming
            modified_words.append(ps.stem(w))
        else:
            modified_words.append(wn.lemmatize(w))

        uniqueWords = set(modified_words[:])  # This removes the duplicates of words after stemming and lemmatization
        for i in uniqueWords:
            duplicates_free.append(i)
    return duplicates_free

def plot_tf(filename):
    """
    This function is for plotting the term frequency of each file or allthewords list on a graph.

    """
    with open(filename.txt, 'r') as file:
        words = file.read()
        new_words = word_tokenize(words)
        tf_grph = dict(new_words)  #Changes the files into a dictionary

        fd = nltk.FreqDist(tf_grph)
        fd.plot(40, cumulative=False)  #Plots forty terms with highest term frequency.

if __name__ == "__main__":
    termfrequency()