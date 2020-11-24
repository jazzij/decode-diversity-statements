#!/usr/bin/env python
"""
Regular expression to detect
1) Hashtags
2) URL's
3) ... other

Contributors: Tawanda Kumbula, @jazzij
"""

import re
import os

curdir = os.getcwd()
textdir = (r"C:\Users\kumbulat\PycharmProjects\decode-diversity-statements\texts")
newtextdir = (r"C:\Users\kumbulat\PycharmProjects\decode-diversity-statements")
newfilePath = os.path.join(newtextdir, "callout_file_name.txt")

def findHashtag(text):
	"""
	Finds any hashtag (#text) from a text file.
	filename: Name of text files in the folder texts
	return: hashtags
	"""
	hashtags = re.findall(r"(#\w+)", text)  # Expression that finds the hashtags in the files
	print("Found the following: ".format(hashtags))
	return hashtags

def findURL(text):
	"""
	Finds the URLs from the text files.
	filename: Name of text files.
	return: URL
	"""
	URL = re.findall(r'(https?://[^\s]+)', text) # Expression that finds the URL in text files
	print("Found the following: ", format(URL))
	return URL

def findMention( text):
	"""
	Finds the mentions in the text files; @.
	filename: Name of text files
	return: Mention
	"""
	Mention = re.findall(r"(@\w+)", text) # Expression that fimds the mentions, @, in texts.
	print("Found the Following: ", format(Mention))
	return Mention

def callout():
	for filename in os.listdir(textdir)[:]:
		filepath = os.path.join(textdir, filename)
		with open(filepath, "r") as file:
			text = file.read()

			mentions = findMention(text)
			hashtags = findHashtag(text)
			Url = findURL(text)

			newfile = open("callout_file_name.txt", "a+") # Writing the returned characters; @, # and URL in the file
			newfile.write("\n".join(mentions))
			newfile.write("\n")  # Separates the last mention and the first hashtag
			newfile.write("\n".join(hashtags))
			newfile.write("\n")
			newfile.write("\n".join(Url))
			newfile.close()

if __name__ == "__main__":
	callout()






