**Date: Thursday, January 14, 2021**

**Rational For Manual Inspection for slplot_uniquewords_allstatements.ipynb file** 

This project aims to plot a stem and leaf visualizations of most important words and their derivatives in all of the statements. This is done in three stages, getting base form of the root words, getting its derivatives from all of the statements, and visualizing the data. Manual inspection was done in two stages of the process of stem and leaf plot. 

In the first stage, the lemmatization function is used to get the base form of a list of unique and important words in all of the statements. These words will be used as the root words in the stem and leaf visualization. The function removes proper nouns tagged as NNP and changes words tagged differently to their base form. There was manual inspection in this stage to remove some proper nouns that were mistagged by the lemmatizer POS function. This is because the input was a list of words rather than a full sentence. As a result, POS did not tag some names as NNP. Therefore, they had to be removed manually from the list. In addition, some words were mistagged and I added the base form manually.

**E.g. Example of manual removal of mistagged proper nouns and words**

```python

    if word == 'ahmaud': # example of removing a proper noun
        clean_words.remove(word)

    if words == 'violently':
        clean_words[clean_words.index('violently')] = 'violent'   # example of changing a word to base from
```

 
The second stage of the project focuses on going through all of the statements to get the derivatives of the root words. Manual inspection was done to remove words from the values of the dictionary because the ifflib.SequenceMatcher mathced some words that did not go together.

**E.g. Example of incorrect stem to leaf matching**

```python

 "right": ["rights", "right", "bright", "wright"]
 "officer": ["officer", "officers", "office"]
 "equality": ["equality", "quality"]
 
 ```
 
As you can see it has categorized **bright** and **wright** as the leaves of word **right** which is incorrect. A correct stem and leaf categorization would look like the following example:

```python
 "demonstration": ["demonstrations", "demonstration", "demonstrating"]
 ```
 
 **E.g. Example of manual removal of incorrect leaves**
 
 ```python
for value in dic.values():
    for i in value:
        if i == 'wright':
            value.remove(i)
 ```
 
 
 
 
 