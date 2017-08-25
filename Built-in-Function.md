Built-in function are the fuctions which are predefined in Python. 
There are some of them such as print.

Another one is len. The len fuction computes the length in character of strings passed into it like this:
>>> udacity_length = len("Udacity")
>>> print(udacity_length)
7

The len function is similar to print in that we call it by passing a variable as the argument inside of parentheses. len differs from print in that it produces a value that can be stored in a variable.

len only accepts strings and no other parameter if it is given an integer it will give an error.

An example is 

given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"

name_length = len(given_name + middle_names + family_name)
driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)

