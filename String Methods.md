we've seen two distinct ways to process data with Python. We've used operators like +, <= and = which process the two values on either side of the operator. We've also used functions like print and len.
Functions are very similar to operators, in fact the only real difference is in how they look: function inputs are put in parentheses rather than being placed next to an operator, and functions have descriptive names rather than short symbols.

There is a third technique for operating on values: methods. Consider the title method:

>>> "charlotte hippopotamus turner".title()
'Charlotte Hippopotamus Turner'

Methods are related to functions but unlike functions, methods are associated with specific types of objects. In this example the object is a string with the value, "charlotte hippopotamus turner", and we are calling its title method. The method returns a string in Title Case, meaning that the first letter of each word is capitalized.

Another string method, islower:

>>> full_name = "charlotte hippopotamus turner"
>>> full_name.islower()
True

The islower method inspects the string object it has been called with. In this case the string object is "charlotte hippopotamus turner". islower then returns a bool that indicates whether the string object consists of lowercase letters.

When we call the islower and title methods we use parentheses, but we haven't put anything in them like we did when calling functions. This isn't because methods don't take arguments though, the methods so far simply don't require arguments. Let's try a method that does take arguments, count.

>>> "One fish, two fish, red fish, blue fish.".count('fish')
4

The count method returns how many times the substring "fish" occurs in the string.

There are various String Methods. They can implement various operations, some of them which we have used are described below.

- str.count(sub[, start[, end]]) : Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
The documentation mention two optional arguments, start and end, these limits the counts to occurrences that appear within specified sections of a string.

- str.capitalize() : Return a copy of the string with its first character capitalized and the rest lowercased.

- str.center(width[, fillchar]) : Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).

Throughout the documentation optional are indicated with square brackets like these. Any argument surrounded by square brackets are optional. 
The documentation tends to be terse and precise, but it's very useful.

All of them are given in Python's official documentation.