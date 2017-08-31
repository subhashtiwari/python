- Indentation 

Indentation is important as it tell Python what code is in the body of a function and which code is outside of the function. Indentation doesn't just matter in function definitions. 
Some other languages use braces like{ and } to show where blocks of code begin and end. In Python indentation is used to enclose blocks of code.

In Python, indentation conventionally comes in multiple of four spaces. It's important to be strict about following this convention, because changing the indentation can completely change the meaning of the code.

If you are working on a team of Pythonprogrammers it's important that everyone followa the same indentation convention.


- Documenting Functions

One of the key advantages of functions is that they can help to break a program down into smaller chunks. This makes code easier to write and also easier to read because they're reusable. 
If a program needs to calculate multiple population densities, it can call population_density multiple times which is tidier than writing out the formula over and over again.

Functions make code easier to read because they give human-readable, documentation strings ( also called "docstrings"). Docstrings are a type of comment used to explain the purpose of a function, and how it should be used. 

Here's the population_density function, with a docstring.

# def population_density(population, land_area):
      """ Calculate the population density of an area.

      population: int. The population of the area
      land_area: int or float. This function is unit-agnostic, if you pass in values in terms of square km or square miles the function will return a density in those units.
      """

      return population / land_area

Docstrings are surrounded by triple quotes, """. The first line of the docstrings is a brief explanation of the function's purpose. If you feel that this is sufficient documentation then you can end the docstring at thsu point, single line docstrings are perfectly acceptable. If you think that the function is complicated enough to warrant a longer description, you can add a more thorough paragraph after the one line summary. 

The next element of a docstring is an explanation of the function's arguments. In here we can list the arguments, state their purpose, and what types the arguments should be.

Each of these pieces of teh docstring is optional, as is the docstring itself. Remember though, it's always easier to write code than to read it. If one can make things easier for your collaborators to read the code, then one should.


- A Function That doesn't Return Anything

Functions can be imagined as little machines that take inputs(arguments) and process them into return (return values). 
But some functions, like print, don't return anything at all:

>>> return_value = print("I wish to register a complaint")
I wish to register a complaint.
>>> print(return_value)
None

print displays text on the console, but it returns None here. None is a special value in Python. It represents the abscence of value. None is what a function will return by default if it doesn't explicitly return anything else.

An example of that is shown using the previous problem.

def print_testcase(expected_value, actual_value):
print("expected value: {}, actual value: {}". format(expected_value, actual_value))

This function doesn't have a return statement like the earlier examples did, but it's still a valid function. 

>>> return_value = print_testcase(42, 42)
expected value: 42, actual value: 42

The ouput was printed when the function was called. Buy waht was assigned to return_value?
We use print on return_value to check.

>>> print(return_value)
None