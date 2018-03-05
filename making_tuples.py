# sample dictionary
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

# takes in a dictionary and returns a list of tuples where the 
# first tuple item is the key and the second is the value. 
def makingTuples(dictionary):
	# create empty list
	new_list = []
	# iterate through key value pair of dictionary
	for key, data in dictionary.iteritems():
		# create tuple with key data pair
		new_tuple = (key, data)
		# add each tuple to empty list
		new_list.append(new_tuple)
	# OBJECTIVE: print list of tuples to console
	print new_list

# call function with sample dictionary
makingTuples(my_dict)