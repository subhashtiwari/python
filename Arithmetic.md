To carry out various arithmetic function using Python, we use different symbols.

In all these examples >>> is the Python prompt it distinguish our input from the output on the following line.

>>> print(3+1) 
4 

This prints the result, 4. The calculation can be done without printing it, but then we wouldn't see the result.

The symbols for addition and subtraction in Python are usual ones, + and -, multiplication asterisk * and division is forward slash /. Brackets for the mathematics are the curved parentheses(and).

Too raise one number to the power of another with two asterisks **.

e.g. 
>>> print(2**3)
8 

The caret ^ is mistaken for exponential operator. Instead it performs a more obscure operation called "bitwise or". 

Another operation is given by % - it is modulo operation. It gives the remainder after you divide the first number by the second.

>>> print(11 % 2)
1

Integer Division is denoted by //. It divides one integer by another, but rather than giving the exact answer it rounds the answer to an integer. It rounds down even if the answer is negative.

>>> print(17 // 4)
4
>>> print(-5 // 4)
-2

It is possible to assign two assignments on a single line.
e.g. books, movies = 1234, 4321
It can be used to assign two closely related variables, like width of an object, or its x and y coordinates.