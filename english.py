import itertools, universal

def is_english(text, strikes = 3):

	'''

	Returns true if text is English.
	Uses a "Three strikes - you're out" policy by default.
	That is, if at least three words in the text are not in the dictionary, then
	you're out and the function returns False.

	'''

	words = text.split()
	tally = 0
	
	for word in words:

		if len(word) > 30:
			return False
		if all([x.isalpha() for x in word]) == False:
			continue

		if word[0].isupper():
			continue

		if word not in universal.wordlist:
			
			tally += 1

		if tally == strikes: # you're out
			return False

	return True