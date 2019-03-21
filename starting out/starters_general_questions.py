'''
Dennis Zethof
21-03-2019

To be used as one sees fit.

Some more ideas for simple questions:
	- something concerning 'index out of range' type of questions
	- something about how different variables can hold the same list
	- how you can change lists without returning them
	- show a keyword argument such as 'key=key'

'''

'''
SETTING UP A SIMPLE CODING ENVIRONMENT
------------------------------------

Option 1: Google Colab

pros:
	- easy and fast to set up
	- can save code in Jupyter notebooks
	- can create files and a filestructure

cons:
	- coding environment limited to Jupyter notebook
	- need a google account


-> Setup:
	- go to your google drive
	- press 'New'
	- choose 'More'
	- choose 'Colaboratory'



Option 2: www.Brython.info

pros:
	- even faster to setup
	- don't need any accounts or login


cons:
	- also not a real coding environment
	- depended on way conversion to browser code (Javascript) is handled
	- more limited in possibilities
	- more difficult to save code (copy/paste to your hardrive?)


-> Setup:
	- go to www.brython.info
	- choose 'Editor' in top menu

'''

'''
WHERE TO PUT THE CODE
---------------------

Github:
	- you can say "go to repository and copy paste the code"
	- would increase familiarity with github, and a general accessibility of
	the examples

Presentation sheets:
	- code could be copied wrong, making it more likely the assignments go to
	waste
	- however, the examples are very simple and short, and copying through
	typing might already be informative by itself

(Jupyter) Notebook:
	- perhaps creating some Jupyter Notebook type of file or format with the
	examples ready to go might be nice
	- this would require people to use that specific format

'''


#									ASSIGNMENTS
###############################################################################

'''
ITERATION AND CUSTOMIZATION
---------------------------

dataset:
grid = '----ppyytthhoonniissttaass----'

code:
for i in range(0, len(grid), 1):
	print(grid[i], end='')
print()

A1:
	change the values so that it will print "pythonistas" (without changing the
	grid).
		TIP1: run the code after every adjustment to see if it does what you want
		TIP2: search the internet for documentation or explanations on how the
		range function works

B1:
	exchange the empty string in 'end' with something else to see what happens
B2:
	then replace the empty string with "'\n'" to see what happens
B3:
	replace the print statement with "print(grid[i])" to see  is anything changes
B4:
	remove the very last print statement and see if anything changes


ANSWERS:

A1:
for i in range(4, 26, 2):
	print(grid[i], end='')
print()


'''


'''
SORTING AND ASSIGNING
---------------------

dataset: li_1 = [5, 4, 3, 2, 1]
A:
	Assign a non reverse ordered version of li_1 to li_2 and print it.

B1:
	Now order li_1 itself, print li_1 to check if it was done correctly.
B2:
	There are at least two ways of doing this, did you find both?

C:
	Reorder li_1 back to its original reverse ordered state.

BONUS:
D:
	'li_1 = reversed(li_1)' creates an iterator which is not a list
	and thus not the correct answer to C. Do you know the difference
	between an iterator and an iterable?


ANSWERS:

A:
li_2 = sorted(li_1)

B1/B2:
li_1.sort()
li_1 = sorted(li_1)

C:
li_1.reverse()
li_1 = sorted(li_1, reverse=True)


NOTE:
li_1 = reversed(li_1) creates an iterator
do you know the difference?
maybe google it?

'''


'''
ITERATORS
---------

from itertools import permutations

per = permutations(['a', 'b', 'c'])


A1
	Print the object 'per', what does it say? Is this an error?
A2
	Can you find out the length of 'per', or how many elements it holds?
	Why does the len() function not work?
A3
	Try to loop through 'per' and print every element, how many are there?
A4
	Search for 'Python 3 itertools docs', and look for the table that
	explains what this function does.

B1
	Convert 'per' to a list. Through searching I found at least two ways,
	did you found those too?
B2
	Can you find a third (or even a fourth) way?


ANSWERS:
A1:  itertools.permutations object, with its memory address. It is not an
error.
A2: the len() function does not work, because it's not a list and the elements
are (often at least) not yet created. Even Python may not know yet how may
results the iterator will produce.
A3:
for p in per:
	print(p)

A4:
https://docs.python.org/3/library/itertools.html
look for table: 'Combinatoric iterators'

B1:
per_list = list(per)
per_list = [*per]

B2:
per_list = []
for p in per:
	per_list.append(p)

per_list = []
[per_list.append(p) for p in per]

'''


'''
EXTENDING AND APPENDING
-----------------------

li = [1, 2, 3, 4, 5]
li.extend(6)


A1
	What does the error message say? Can you search the error?
A2
	Why can we not extend this list this way?
A3
	Name two ways to fix this error.

B1
	With the list 'li' still in memory, run this code:

		li.append('stuff')
		print(li)
	
	What does it show?
B2
	Now run this code also:

		li.extend('stuff')
		print(li)
	
	What does it print now? What does this say about the string 'stuff' and
	strings in general? For example: why do you not have to put 'stuff' in
	brackets in order to enter it as argument to the extend() function?
B3
	Given this code:
		var = 'pythonistas'
	
	Find a way to iterate over the variable 'var', and print each element
	of this string seperately.

ANSWERS:
A3
li.extend([6])
li.append(6)

B2
Strings are not the same as lists, but they are both iterables.

B3
for v in var:
	print(v)

'''

'''
STRINGS AND QUOTES
------------------

var = 'The question is: who's shoes are these?'

A1
	What's wrong with this sentence?
A2
	What are two ways to fix this?
A3
	Look at this code:

		var = '"Those aren't" mine she said'

	There is at least one more way, can you find it?
A4
	Look at this code:
	
		var_2 = `A sentence`

	What do you think, will it work?


ANSWERS:

A1:
The quotes that are suppose to indicate a string are conflicting. Python cannot
know when the supposed string starts and ends because of the apostrophe.

A2:
var = "The question is: who's shoes are these?"
var = 'The question is: who\'s shoes are these?'

A3
var = '''"Those aren't" mine she said'''
var = """"Those aren't" mine she said"""
var = '"Those aren\'t" mine she said'

A4:
The variable contains backticks, usually located under the tilde next to the
"1" on the keyboard. Python does not accept these to indicate a string. They
can be used inside strings.

'''
