def get_ascii_int_tuple():

	'''
	Retrieves ASCII data from cipher.txt, and then returns
	it as a tuple of ints.
	i.e. cipher.txt is 'abc', get_ascii_int_tuple()
	returns [97,98,99]

	'''
	f = open('cipher.txt','r')

	text = f.read()
	f.close()

	ascii_list = [int(w) for w in text.split(',')]

	return tuple(ascii_list)

def get_wordlist():

	'''
	Generates an English wordlist set from enable1.txt.
	'''

	s = set()

	f = open('enable1.txt','r')

	for word in f.readlines():
		word = ''.join(x for x in word if x.isalpha())

		s.add(word)

	return s
	
