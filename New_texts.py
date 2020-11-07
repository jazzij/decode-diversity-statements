import os
import os.path
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

def all_texts():
  """
  This function is supposed show all the list of files in the directory
  filename: The texts files in the texts folder
  return: filenames
  """

  print(os.getcwd())  # Checks which directory python file is in
  textdir = os.path.join( os.getcwd(), "texts")  # Assuming texts is a directory located in the same place as your python file
  print(os.path.isdir(textdir))  # Checks if valid

  for filename in os.listdir(textdir):
    filepath = os.path.join(textdir, filename)  # Create the full filepath using the directory and filename
    with open(filepath, "r") as file:
      text = file.read()
    return filename

def new_tokenized_texts():
  """
  This function us supposed to create new text files; token_texts
  """

  textdir = os.path.join(os.getcwd(), "texts")  # Assuming texts is a directory located in the same place as your python file
  prefix = "tokens_"  # This is added at the beginning of filename to avoid duplicating originals
  newtextdir = os.path.join(os.getcwd(), "tokenText")  # instead of ~/texts

  for filename in os.listdir(textdir):
    newfilePath = os.path.join(textdir, filename)
    with open(newfilePath,"r") as file:     # Opens the original text files
      texts = file.read()

      tokens = nltk.word_tokenize(texts)  # Breaks text paragraph into word
      tokens = [word.lower() for word in tokens if word.isalpha()]  # Changes all the words into lower case

      newfileName = prefix + filename
      newfilePath = os.path.join(newtextdir, newfileName)
      print("newfilePath",newfilePath)
      with open(newfilePath, 'w') as newfile:
        newfile.write(", ".join(tokens))  # This will write to file the list of filtered tokens as comma separated string

if __name__ == "__main__":
  all_texts()
  new_tokenized_texts()




