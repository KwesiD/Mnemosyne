import pickle #for data serialization



def serialize(dictionary):
	if(type(dictionary)) != type({"":""}):
		raise TypeError("Variable passed to \"serialize\" is not a dictionary!")
	dict_file = open("dict",'wb')
	pickle.dump(dictionary,dict_file) #saves serialized dict as "dict" in cwd
	return dict_file #returns the file


