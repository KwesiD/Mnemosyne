#Generates random sentences based off of frequencies
from numpy.random import choice
from Special_Values import *


##TODO: account for sentence ending. Add something to choose sentence-ending terms
def generate_sentence(sequence,frequency_table,tag_table,word_tag_table): #sequence is a sequence of letters. the method will generate a word for each letter in the sequence, in order
	sequence = sequence.lower()
	sentence = []
	prev_word = start_code
	prev_tag = start_code
	retries = 0 # number of retries
	current = ""
	i = 0
	while(i < len(sequence)):
		current = sequence[i]
		if retries >= 5:
			raise RetryError()

		#finds a word to start with using a weighted-random selection

		random_tag = choice(a=list(tag_table[prev_tag].keys()),p=list(tag_table[prev_tag].values()))

		#dictionary of pairs in the form (word,frequency as tag) only start with current letter
		words_with_tag = {}# = {word:word_tag_table[random_tag][word] for word in word_tag_table[random_tag] if word.startswith(current)}
		for word in word_tag_table[random_tag]:
			if word.startswith(current):
				entry = {word:word_tag_table[random_tag][word]}
				words_with_tag.update(entry)

		if not bool(words_with_tag):
			#i -= 1
			retries += 1
			continue

		#dictionary of pairs of words folowing prev_word and their frequencies
		frequency_set = frequency_table[prev_word]
		for word in words_with_tag: 
			if word in frequency_set:
				words_with_tag[word] *= frequency_set[word] #calculate total frequency
			else:
				words_with_tag[word] = 0

		count = sum(words_with_tag.values())
		try:
			for word in words_with_tag:

				words_with_tag[word] /= count
		except ZeroDivisionError:
					#i -= 1
					retries += 1
					continue
	

		#print(words_with_tag)
		random_word = choice(a=list(words_with_tag.keys()),p=list(words_with_tag.values()))
		if random_word == None or words_with_tag[random_word] == 0: #if no word found or if total frequency is 0
			retries += 1
			continue

		sentence.append(random_word) #add word to sentence
		i += 1 #increment i
		retries = 0
	return sentence



class RetryError(Exception):
	"Too many retries. Exiting"


		


		




