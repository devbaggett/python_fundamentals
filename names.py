# sample list
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# takes sample array and print full name from dictionary
def names(arr):
	for i in arr:
		print i["first_name"] + " " + i["last_name"]

# call function		
names(students)



# separation border
print "-------------------------------------"



# sample dictionary
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# same as names() function only this prints a count of names and name length
def nameNum(arr):

	students_count = 0
	instructors_count = 0
	
	for i in arr:
		print i
		for j in arr[i]:
			if i == "Students":
				students_count += 1
				print "{} - ".format(students_count) + j["first_name"] + " " + j["last_name"] + " - {}".format(len(j["first_name"] + j["last_name"]))
			elif i == "Instructors":
				instructors_count += 1
				print "{} - ".format(instructors_count) + j["first_name"] + " " + j["last_name"] + " - {}".format(len(j["first_name"] + j["last_name"]))

# call function
nameNum(users)
