import nltk
from Special_Values import *
import string
import pprint

def parse(corpus):
	frequency_table = {"$t@rt":{}} #a dictionary containing the bigrams and their frequencies
	tag_table = {"$t@rt":{}} #a table of POS tags and words of that tag and their frequenies - POS Bigrams
	word_tag_table = {"$t@rt":{}} #a table of tags and words associated with them + frequencies as those tags
	word_count = 0 #number of words found
	tag_count = {} #counts of each POS tag
	prev_token = start_code #previous token. initialized to sentence start 
	prev_tag = start_code
	corpus = nltk.sent_tokenize(corpus)
	print("tokenized corpus")
	print(len(corpus))

	#we are processing each line of the corpus on its own.
	for line in corpus:
		prev_token = start_code
		prev_tag = start_code
		tokens = nltk.word_tokenize(line) #splits line into tokens
		tagset = nltk.pos_tag(tokens) #tags the tokens returns list of tupules (word,tag)
		tags = [tag for word,tag in tagset] #list of the second elements (the tags) of the tuple in the form (word,tag)

		for token,tag in zip(tokens,tags):
			token = token.lower()
			if token in punctuation_list: #skips punctuation
				continue

			if(prev_token not in frequency_table): #if the token is not in the table at all, then add it
				frequency_table[prev_token] = {}

			if(token in frequency_table[prev_token]): #if it is contained in the table after start
				frequency_table[prev_token][token] += 1
			else:
				frequency_table[prev_token].update({token:1})

			if(prev_tag not in tag_table):
				tag_table[prev_tag] = {}

			if(tag in tag_table[prev_tag]): #if it is contained in the table after start
				tag_table[prev_tag][tag] += 1
			else:
				tag_table[prev_tag].update({tag:1})	

		

			if(tag not in word_tag_table):
				word_tag_table[tag] = {}


			if(token not in word_tag_table[tag]):
				word_tag_table[tag].update({token:1})
			else:
				word_tag_table[tag][token] += 1

			


			prev_token = token #set the current token as the previous token
			prev_tag = tag

		if(prev_token not in frequency_table): #if the token is not in the table at all, then add it
				frequency_table[prev_token] = {}

		if(end_code in frequency_table[prev_token]): #closes with end_token
			frequency_table[prev_token][end_code] += 1
		else:
			frequency_table[prev_token].update({end_code:1})


		if(prev_tag not in tag_table):
				tag_table[prev_tag] = {}

		if(end_code in tag_table[prev_tag]): 
			tag_table[prev_tag][end_code] += 1
		else:
			tag_table[prev_tag].update({end_code:1})



	for first_term in frequency_table: #for each preceding term in the table...
		count = sum(frequency_table[first_term].values()) #...sum up the counts of every term
		for second_term in frequency_table[first_term]: #for each following term
			frequency_table[first_term][second_term] /= count #divide by the total count to get the frequency the second term follows the first

	#same ideas as before, but with POS tags

	for first_tag in tag_table: #for each preceding tag in the table...
		count = sum(tag_table[first_tag].values()) #...sum up the counts of every tag
		for second_tag in tag_table[first_tag]: #for each following tag
			tag_table[first_tag][second_tag] /= count #divide by the total count to get the frequency the second tag follows the first


	for tag in word_tag_table:
		count = sum(word_tag_table[tag].values())
		for word in word_tag_table[tag]:
			word_tag_table[tag][word] /= count

	#the building of the tables is complete
	return frequency_table,tag_table,word_tag_table


# corpus = open("corpus.txt","r")
# f,t,w = parse(corpus)
# pp = pprint.PrettyPrinter(indent = 4)
# pp.pprint(w)







			


