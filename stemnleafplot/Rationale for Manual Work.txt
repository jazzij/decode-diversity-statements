 Explain the manual inspection process and rationale for words were misclassified and taken off of the leaves list
 Example of iterative problem solving
 
 Manual inspection was done in two stages of the process of stem and leaf plot.
 This project aims to plot a stem and leaf visualizations of most important words and their derivatives in all of the statements.
 A list of unique and important words was already provided. This project gets the base form of these words which will be used as the root words in the stem and leaf visualization. The lemmatization function removes proper nouns tagged as NNP and changes words to their base form. There was manual inspection in this stage to remove some proper nouns that were mistagged by the lemmatizer POS function because the input was a list of words rather than a full sentence. As a result, POS did not tag some names as NNP. Therefore, they had to be removed manually from the list. In addition, some words were mistagged and I added the base form manually.
 E.g. violently --> violent
 
The second stage of the project focuses on going through all of the statements to get the derivatives of the root words. Manual inspection was done to remove words from the values of the dictionary because the ifflib.SequenceMatcher mathced some words that did not go together.

**E.g.**
 "right": ["rights", "right", "bright", "wright"]
 "officer": ["officer", "officers", "office"]
 "equality": ["equality", "quality"]
 
 As you can see it has categorized bright and wright as the leaves of word right which is incorrect. A correct stem and leaf categorization would look like the following example:
 
 "demonstration": ["demonstrations", "demonstration", "demonstrating"]
 