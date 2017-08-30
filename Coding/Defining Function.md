Volume of Cylinder function

Write a function that calculates the volumme of a cylinder: the cylinder's height, multiplied by the square of its radius and multiplied by pi.

The definition of a function that calculates the volume of a cylinder:

def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

After defining the cylinder_volume function, it can be used like this:

cylinder_volume(10,3)
282.7431

- The Anatomy of a Function definition

This is explained using diagram shown in image Function Volume.

- Function Header

1. The 'def' keyword indicates that the code that follows is a function definition.

2. Following def is the name of the function, in this case cylinder_volume. This need to be one word, with no gaps - that's why this one has an underscore.

3. The first line of a function definition has one final element, the arguments the functio expects(the rules for function names are the same as the rules for variable names). The arguments of a function are values passed in when the functoin is called; they are used in the body of the function. The arguments are seperated by commas and placed in a pair of parentheses. If you write a function that doesn't take arguments, then use an empty pair of parentheses, (). The first line of the function definition ends with a colon, :.

Here is an example of a function that takes no arguments:

def print_greeting():
print('Hello World!')

The functoin prints "Hello World". Since it takes no arguments we used an empty pair of parentheses.

 - Function Body

 1. The body of the function is indented by four spaces by four spaces. The function body is where the function does its work. In the body we can refer to the argument variables and define new variables. 
 The 'pi' variable that is defined here is a local variable, meaning that it can only be used within the body of the 'cylinder_volume' function. Attempting to access the variable anywhere else would cause an error.

 2. The 'return' keyword is used to get results out of the function. The value of the expression that follows return is the output of the function.

 3. In this example we return the value of an expression, the formula for the volume of a cylinder. 