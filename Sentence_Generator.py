#Generates random sentences based off of frequencies
import numpy

start_code = Special_Values.start_code
end_code = Special_Values.end_code
def generate_sentence(sequence,frequency_table,tag_table): #sequence is a sequence of letters. the method will generate a word for each letter in the sequence, in order
	sentence = ""
	prev_word = start_code
	prev_tag = start_code
	for letter in sequence:
		#finds a word to start with using a weighted-random selection
		




