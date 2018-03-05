# The keys should include name, age, country of birth, favorite language.
mySelf = {"Name" : "Devin", "Age" : "34", "Country of birth" : "United States", "Favorite Language" : "Gibberish"}

print "My name is {}.".format(mySelf["Name"])
print "My age is {}.".format(mySelf["Age"])
print "I was born in: {}".format(mySelf["Country of birth"])
print "My favorite language is {}".format(mySelf["Favorite Language"])


# can take and print out any dictionary keys and values
def buildDict(list):
	for i in list:
		print i, ":", list[i]

buildDict(mySelf)


# another way of writing the above
def buildDict2(list):
	for key, value in mySelf.iteritems():
		print "My", key, "is", value

buildDict2(mySelf)

