import os
import os.path
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

def all_texts(filename):
  """
  This function is supposed show all the list of files in the directory
  filename: The texts files in the texts folder
  return: filenames
  """

  print(os.getcwd()) #check which directory python file is in
  textdir = os.path.join( os.getcwd(), "texts") #assuming texts is a directory located in the same place as your python file
  print(os.path.isdir(textdir)) #check if valid

  for filename in os.listdir(textdir):
    filepath = os.path.join(textdir, filename) #create the full filepath using the directory and filename
    with open(filepath, "r") as file:
      text = file.read()

    return filename

def new_tokenized_texts(filename):
  """
  This function us supposed to create new text files
  """

  textdir = os.path.join( os.getcwd(), "texts") #assuming texts is a directory located in the same place as your python file
  prefix = "tokens_"  # add this to beginning of filename to avoid duplicating originals
  newtextdir = os.path.join(os.getcwd(), "tokenText")  # instead of ~/texts

  for filename in os.listdir(textdir):
    newfilePath = os.path.join(textdir, filename)
    with open(newfilePath,"r") as file:
      texts = file.read()

      stop_words = set(stopwords.words('english'))  # Creating a List of stopwords
      tokens = nltk.word_tokenize(texts)  # Breaks text paragraph into word
      tokens  = [word.lower() for word in tokens if word.isalpha()]  # Changes all the words into lower case

      filtered_words = [w for w in tokens if not w in stop_words]  # Filter out a list of tokens from the text.
      filtered_ = []

      for w in tokens:
        if w not in stop_words:
          filtered_.append(w)  # Add all words after stopwords have been removed

      newfileName = prefix + filename
      newfilePath = os.path.join(newtextdir, newfileName)
      with open(newfileName, 'w') as newfile:
        newfile.write(", ".join(filtered_))  # this will write to file the list of filtered tokens as comma separated string
      return newfile

def lemmatization(newfile):
  """
  This function is meant to reduce the word to its root synonym.
  newfile: Name of the file
  return: lemmatized_words
  """
  with open(newfile, "r") as file:
    text = file.read()

  wn = nltk.WordNetLemmatizer()
  words = word_tokenize(text)
  lemmatized_words = []
  for line in words:
    lemmatized_words.append(wn.lemmatize(line))  # Adds words to the list

  return lemmatized_words




