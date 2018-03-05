# takes a list of numbers and prints out "*" for each line
def drawStars(numList):
	for i in numList:
		if type(i) == str:
			print len(i) * i[0].lower()
		else:
			print "*" * i

drawStars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])


