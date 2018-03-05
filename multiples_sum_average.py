#print all odd numbers from 1 to 1000
for i in range(1,1001):
	if i % 2 == 1:
		print (i)

#print all multiples of 5 from 5 to 1,000,000
for i in range(5, 1000001, 5):
	print (i)

#print the sum of all values in list
a = [1,2,5,10,255,3]

def sumList(list):
	sum_list = 0
	for i in list:
		sum_list += i

	print sum_list
	return sum_list

sumList(a)

#print the average of values in list above
def avgList(list):
	sum_list = 0
	for i in list:
		sum_list += i

	print sum_list / len(list)
	return sum_list / len(list)

avgList(a)