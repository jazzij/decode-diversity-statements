import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def remove_puctuation(filename):
    """
    This function removes the punctuations from the text.
    Filename: Name of the file
    return: new_text
    """
    with open(filename.text, "r") as file:
        text = file.read()

    tokenizer = nltk.RegexpTokenizer(r"\w+")  # Removes all punctuation marks in the text
    new_text = tokenizer.tokenize(text)      # Returns a text as a list of words with punctuations removed.
    #print (new_text)
    return new_text

def lower_case(filename):
    """
    This function is for changing the text to lower caps
    Filename: Name of the file
    return: words (in lower caps)
    """
    with open(filename.text, "r") as file:
        text = file.read()

    words = nltk.word_tokenize(text)  # Breaks text paragraph into words
    words = [word.lower() for word in words if word.isalpha()]  # Changes all the words into lower case
    #print(words)

    return words

def stop_words(filename):
    """
    This function is for removing the stopwords from the text file.
    Filename: Name of the file
    return: filtered_words
    """
    with open(filename.text, "r") as file:
        text = file.read()

    stop_words = set(stopwords.words('english')) # Creating a List of stopwords

    word_tokens = word_tokenize(text) # Split sentences in the text into words

    filtered_words = [w for w in word_tokens if not w in stop_words] # Filter out a list of tokens from the text.
    filtered_words = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_words.append(w)    # Add all words after stopwords have been removed
    print ("Filtered_words:",filtered_words )

    return filtered_words

def termfrequency(filename):
    """
    This function is supposed to calculate the term frequency of the text in file.
    Filename: Name of the file
    return: term frequency
    """
    with open(filename.text, "r") as file:
        text = file.read()
        myList = []
        normalizeTermFreq = text.split()  # Removes the white space between the words
        allWords = (normalizeTermFreq)

        uniqueWords = set(allWords)  # Searches and store each unrepeated word in text

        for i in uniqueWords:
            count = 0
            for j in allWords:
               if i == j:      # Compares each with word with every word in the text
                    count += 1
            myList.append([i, count / len(allWords)]) # Add every word to the list and calculate the term frequency

        for i in myList:
            #print (i)
            return i

def _stemming(filename):
    """
    This function reduces the word to its stem; stemming.
    Filename: Name of the file
    return: stemmed_words
    """

    with open(filename.text, "r") as file:
        text = file.read()

    ps = PorterStemmer()
    words = word_tokenize(text)
    stemmed_words = []
    for w in words:
        stemmed_words.append(ps.stem(w)) # Adds words to the list
    print(stemmed_words)
    return stemmed_words
