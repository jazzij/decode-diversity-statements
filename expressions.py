#!/usr/bin/env python
'''
Regular expression to detect
1) Hashtags
2) URL's
3) ... other

Contributors: Tawanda Kumbula, @jazzij
'''

import re

#Example use: findHashtag( os.path.join(textdir, "AISES.txt"))
def findHashtag( filename):
	''' Finds any hashtag (#text) from a text file. Returns list of hashtags found '''

	with open(filename, "r") as file:
		text = file.read()
	
	hashtags = re.findall(r"(#\w+)", text)
	print("Found the following: ".format(hashtags))
	return hashtags

def findURL( filename):
	''' TODO: find URLs in the text '''
	pass



