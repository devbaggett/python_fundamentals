# allows use of random function
import random

# generates ten scores between 60 and 100, then displays a grade for corresponding score
def scoresGrades():
	for i in range(0, 10):
		random_num = random.randint(60, 100)
		if 59 < random_num < 70:
			print "Score: {}; Your grade is D.".format(random_num)
		elif random_num < 80:
			print "Score: {}; Your grade is C.".format(random_num)
		elif random_num < 90:
			print "Score: {}; Your grade is B.".format(random_num)
		else:
			print "Score: {}; Your grade is A.".format(random_num)
		
scoresGrades()