There are four Objects types till yet 

int - integer for whole number
float - for numbers that aren't necessarily whole numbers
bool - boolean, for true and false values
str - string, for text

Different types have different properties, and when we designing a computer program, we'll need to choose the types for we data based on how you’re going to use them. For example, if you want to use a number as a part of a sentence, it'll be easiest if that number is a string. If you want to encode a true/false value, it will be much easier to manipulate as a boolean than a string.

We can create new objects from old, and change the type in the process. Some of the examples are:

- Creating an int from a float and assigning it to a variable count, printing count and its type.

>>> count = int(4.0)
>>> print(count)
4
>>> print(type(count))
<class 'int'>

- Making a string from a number:

>>> house_number = 13
>>> street_name = "The Crescent"
>>> town_name = "Belmont"
>>> print(type(house_number))
<class ‘int’>
>>> address = str(house_number) + " " + street_name + ", " + town_name
>>> print(address)
13 The Crescent, Belmont

- Build a number from a string:

>>> grams_of_sugar = float("35.0")
>>> print(grams_of_sugar)
35.0
>>> print(type(grams_of_sugar))
<class ‘float’>


For example:

Calculate and print the total sales for the week from the data provided. Print out a string of the form "This week's total sales: xxx", where xxx will be the actual total of all the numbers. You’ll need to change the type of the input data in order to calculate that total.

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

mon_sales = float("121")
tues_sales = float("105")
wed_sales = float("110")
thurs_sales = float("98")
fri_sales = float("95")

print("This week's total sales:",mon_sales+tues_sales+wed_sales+thurs_sales+fri_sales)

And output is

This week's total sales: 529.0