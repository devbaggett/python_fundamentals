# input
string_list = ['hello','world','my','name','is','Anna']
char = 'o'

# output
# new_list = ['hello','world']


# takes a list of strings & single char, and prints a new list of all the strings containing that char
def findCharacters(word_list, char):

	new_list = []

	for i in range(0, len(word_list)):
		if char in word_list[i]: # (if word_list[i].find(char) > 0:) also works
			new_list.append(word_list[i])
	print new_list

findCharacters(string_list, char)