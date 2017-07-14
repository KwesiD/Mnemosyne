from Parser import *
from Sentence_Generator import *

corpus = open("book_corpus.txt","r").read()
print("opened corpus")
frequency_table,tag_table,word_tag_table = parse(corpus)
print("parsed")
sentence = generate_sentence("IPMAT",frequency_table,tag_table,word_tag_table)
print(sentence)

