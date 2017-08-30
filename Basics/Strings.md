To work with text in Python we need to use a string - which is just a series of characters. A string is the type that holds text.
A string is created by using quotes - single or double quotes work equally well.

>>> print("hello") #used double-quotes here
hello
>>> print ('hello') #used single-quotes on this one
hello

A variable can be set to be a string in the same way as a number. Strings can include any characters: even spaces, punctuation and numbers.

>>> welcome_message = "Hello, welcome to Udacity!"
>>> print(welcome_message)
Hello, welcome to Udacity!

Strings are not numbers, but there are some operations that worked for integers and floats that will also work for strings. For example, we can use the + to put strings together - we call this to concatenate strings.

>>> instructor_1 = "Philip"
>>> instructor_2 = "Charlie"
>>> print(instructor_1 + instructor_2)
PhilipCharlie

Python is completely literal when working with strings - we need to explicitly include spaces and punctuation if we want what we write to make sense.

>>> instructor_1 = "Philip"
>>> instructor_2 = "Charlie"
>>> print(instructor_1 + " and " + instructor_2)
Philip and Charlie