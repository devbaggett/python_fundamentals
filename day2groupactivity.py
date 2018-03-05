'''Write as functions and then call them.
1.
SET greeting AS 'hello' 
SET name AS 'dojo' 
LOG name + greeting
2.
1. Given an array of words: ['Wish', 'Mop', 'Bleet', 'March', 'Jerk'] 
2. Loop through the array
3. Print each word to console
3.
Write a function that takes a number.
Create an empty list.
Multiply that number by 2.
Push the new number to our empty list.
Repeat 25 times.
Print list.
4.
1. Define a small program that accepts strings as inputs
2. Have your program create a blank string.
3. Starting at the back of the input string and walking backwards:
   3a. Push each character into the blank string.
   3b. Repeat for all characters in input string.
4. Print the reversed string.


'''
def equals():
	x = 10
	x = x * 7
	y = 30
	z = y + x
	z = z* 3
	z = z - y
	z = z/27
	x = z + y
	y = 3
	x = x + y
	if x % 10 == 0:
		return True
	else:
		return False
print equals()



def greeting():
	greeting = "hello"
	name = "dojo"
	print greeting + name

greeting()


def words(list):
	for i in list:
		print i

words(['Wish', 'Mop', 'Bleet', 'March', 'Jerk'])


def num(num):
	empty_list = []
	num *= 2
	for i in range(0, 25):
		empty_list.append(num)
	print empty_list

num(3)

def program(string):
	blank_string = ""
	for i in range(len(string) - 1, -1, -1):
		blank_string += string[i]

	print blank_string

program("reverse")

random = range(10)
print random[0::2]
