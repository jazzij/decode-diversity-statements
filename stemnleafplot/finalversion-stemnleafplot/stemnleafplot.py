import nltk
import os
import sys
import json 
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer



tokenizer = nltk.RegexpTokenizer(r"\w+")  # Removes all punctuation marks in the text
tokenized_statements = []
roots_and_leaves = {}
text = []
unimportant_roots = []

def tokenize_statements(textdir):
    '''
    Tokenizes all the statements.
    Input: location of the file in the directory
    return: list of tokenized statements.
    '''
   
    for filename in os.listdir(textdir)[:]:
        filepath = os.path.join(textdir, filename)
        with open(filepath, "r") as file:
            text = file.read()
            tokens = tokenizer.tokenize(text)  # Returns a text as a list of words with punctuations
            for word in tokens:
                tokenized_statements.append(word)
    return tokenized_statements


def lemmatized_word(tagged_tokens):
    ''' 
    Lemmatize words in the statements and adds it to the dictionary with as roots and leaves
    Input: tagged tokenized sentences
    return: roots and leaves dictionary with lemmatized words as roots
    '''
    lemmatizer = WordNetLemmatizer()
    
    for word, tag in tagged_tokens:
        if  not tag.startswith('NNP' or 'NNPS'): # ignore propr nouns
            if tag.startswith('NN' or 'NNS'):
                lemmatized_word = lemmatizer.lemmatize(word, pos='n')
            elif tag.startswith('VB' or 'VBP' or 'VBD' or 'VBG' or 'VBP' or 'VBZ'):
                lemmatized_word = lemmatizer.lemmatize(word, pos='v')
            elif tag.startswith('JJ' or 'JJR' or 'JJS' ):
                lemmatized_word = lemmatizer.lemmatize(word, pos='a')
            elif tag.startswith('RB' or 'RBR' or 'RBS' or 'RP'):
                lemmatized_word = lemmatizer.lemmatize(word, pos='r')
            else:
                lemmatized_word = lemmatizer.lemmatize(word)   
            
            if lemmatized_word in roots_and_leaves.keys():
                if word not in roots_and_leaves[lemmatized_word]:
                    roots_and_leaves[lemmatized_word].append(word)
            else:
                roots_and_leaves[lemmatized_word] = []
                roots_and_leaves[lemmatized_word].append(word)
    return roots_and_leaves



def main():
    ''' 
    The main function

    '''


    ##Import the statements which will be used for the root and leaf plot
    textdir = (r"C:\Users\manalais\decode-diversity-statements\texts")
    tokenized_statements = tokenize_statements(textdir)   # tokenize all the statements
    tagged_tokens = nltk.pos_tag(tokenized_statements)  # tag all the statements with the appropriate POS
    root_and_leaves = lemmatized_word(tagged_tokens)  #lemmatize all of the tagged tokenized statements


    #alphabetically sort dictionary
    root_and_leaves = dict(sorted(root_and_leaves.items(), key=lambda item: item[0]))


    #Import the uniquewordslist.txt which will be used for the root words
    textdir = (r'C:\Users\manalais\decode-diversity-statements')
    filename = "uniquewordslist.txt"
    with open(os.path.join(textdir, filename), 'r') as file:
            text = file.read()
            text = tokenizer.tokenize(text)

    #create a list of root  words that is not in the uniquewordlist.txt file
    for key in root_and_leaves.keys():
        if key not in text:
            unimportant_roots.append(key)

    #remove all the roots and its leaves that is not in uniquewordlist.txt file 
    for root in unimportant_roots:
        root_and_leaves.pop(root)

    #Visualize the data and save it as txt.file
    sys.stdout = open(r'C:\Users\manalais\decode-diversity-statements\stemnleafplot\stemnleafplot_py_result.txt', 'w')
    print("Root and Leaf Plot" + "\n")
    for root,leaves in root_and_leaves.items():
        print(root + '| ' + " ".join(leaves))
    sys. stdout. close()

main()
    
