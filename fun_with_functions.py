# counts from 1 to 2000 and prints whether odd or even
def oddEven():
	for i in range(1, 2001):
		if i % 2 == 0:
			print "Number is {}. This is an even number.".format(i)
		else:
			# print "Number is {}. This is an odd number.".format(i)
			print "Number is " + str(i) + ". This is an odd number."

oddEven()


# iterates through 'list' and multiplies the value by parameter: 'mult'
def multiply(list, mult):
	newlist = []
	for i in list:
		i *= mult
		newlist.append(i)
	return newlist


b = multiply([1,2,3], 2)
print b


def layered_multiples(list):
	newlist = []
	for i in list:
		subList = []
		for i in range(0, len(list)):
			print i
			subList.append(1)
		newlist.append(subList)
	return newlist

b = layered_multiples(multiply([2,4,5], 3))