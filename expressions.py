#!/usr/bin/env python
'''
Regular expression to detect
1) Hashtags
2) URL's
3) ... other

Contributors: Tawanda Kumbula, @jazzij
'''

import re


def findHashtag( filename):
	"""
	Finds any hashtag (#text) from a text file.
	filename: Name of text files in the folder texts
	return: hashtags
	"""
	with open(filename, "r") as file:
		text = file.read()
	
	hashtags = re.findall(r"(#\w+)", text)  # Expression that finds the hashtags in the files
	print("Found the following: ".format(hashtags))
	return hashtags

def findURL( filename):
	"""
	Finds the URLs from the text files.
	filename: Name of text files.
	return: URL
	"""
	with open(filename, "r") as file:
		text = file.read()

	URL = re.findall(r'(https?://[^\s]+)', text) # Expression that finds the URL in text files
	print("Found the following: ", format(URL))
	return URL

def findMention( filename):
	"""
	Finds the mentions in the text files; @.
	filename: Nmae of text files
	return: Mention
	"""

	with open(filename, "r") as file:
		text = file.read()

	Mention = re.findall(r"(@\w+)", text) # Expression that fimds the mentions, @, in texts.
	print("Found the Following: ", format(Mention))
	return Mention








