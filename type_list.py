#takes a list a prints a message for each element in list, based on its data type
def typeList(list):

	new_string = ""
	sum_of_list = 0
	count_num = 0
	count_str = 0

	for i in list:
		if type(i) == str:
			new_string += i + " "
			count_str += 1
		elif type(i) == int or type(i) == float:
			sum_of_list += i
			count_num += 1

	if count_num > 0 and count_str > 0:
		print "The list you entered is of mixed type."
	elif count_num > 0 and count_str <= 0:
		print "The list you entered is of integer (or float) type."
	elif count_num <= 0 and count_str > 0:
		print "The list you entered is of string type."

	if count_str > 0:
		print "String: ", new_string

	if count_num > 0:
		print "Sum: ", sum_of_list

typeList(['magical','unicorns'])




