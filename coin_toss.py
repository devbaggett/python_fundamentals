# allows use of random library function
import random

# simulates tossing a coin 5,000 times, then prints # of heads and tails with each flip
def coinToss():
	print "Starting the program..."
	heads = 0
	tails = 0
	for i in range(0, 5001):
		toss = round(random.random() * 100)
		if toss < 50:
			heads += 1
			print "Attempt #{}: Throwing a coin... It's heads!... Got {} head(s) so far and {} tail(s) so far.".format(i, heads, tails)
		elif toss > 49:
			tails += 1
			print "Attempt #{}: Throwing a coin... It's tails!... Got {} tails(s) so far and {} heads(s) so far.".format(i, tails, heads)			
		
coinToss()