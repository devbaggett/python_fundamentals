# sample lists
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# takes in two lists and creates a single dictionary
# first list contains keys and the second list contains values
def make_dict(list1, list2):
	# create empty dictionary
  	new_dict = {}
  	# combine both lists into a single list with 2-tuple list form
  	new_list = zip(list1, list2)
  	# transform 2-tuple list form into dictionary
  	new_dict = dict(new_list)
  	print new_dict
  	return new_dict
  	
# call function with sample lists from top
make_dict(name, favorite_animal)