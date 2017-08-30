Variables are used to store values in them.

e.g.
>>> books = 125478 

In here, variable name is books, the equal sign is assignment operator, the value of variable books is 125478.

The order of this assignment is very important. It always goes in that same order, variable name = value.
The assignment operator assigns the value on the right to the variable name on the left.

There is no keyword for variable assignment in Python as there is in some language, and there is no need to specify the value.

If we need to know the assigned value just use print(variable name).
>>> print(books)
125478

print is used when we need to know the value of a certain variable. Without print what happens in Python, stays in Python.
print is very useful for debugging when something's goes wrong. 
print is a built-in function in Python, and you’ll come across more of those later on. Function calls in Python always have a pair of parentheses attached, and if there are any arguments, they go inside the parentheses. 
In naming variables there are some reserved words known as keywords and hence cannot be used as a variable name. Use underscore '_' to seperate a long variable name, e.g. history_books.

To update an already set variable simply reassign the value to that variable.

Reassignment Operators

To increase, decrease and for other operatoins re-assign is very common. Python includes special operators for it.

These are some examples
>>> history_books += 1675 # increase the value of history_books by 1675
>>> history_books -= 250 # decrease the value of history_books by 250
>>> history_books *= 0.9 # decimate history_books
>>> books /=  2 # approximate the books in the library.