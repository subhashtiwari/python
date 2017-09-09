# Lists

List is a collection of data in form of list. It can contain any type of data as it's collection.

For Example

python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]

This code defines a variable, python_versions, which contains a list of floats. Each element in the list is the version number of a significant Python release. A list is defined using square brackets ([ and ]), and the elements of the list are separated by commas.

We can look up individual elements in the list by their index. We can look up version numbers like this:

        >>> python_versions[0]
        1.0

        >>> python_versions[1]
        1.5

        >>> python_versions[7]
        2.4

The first element in the list, 1.0 is located at index 0 rather than index 1. Many programming languages follow this convention, called "zero based indexing". 

If zero based indexing is confusing, consider it this way: an element's index describes how far the element is from the beginning of the list. The first element is 0 elements away from the beginning, the second is one element away, and so on.

We can also index from the end of the list rather than front like we have been doing so far. To do this we use negative indexes, for example we can get the most recent Python version in the list like this:

>>> python_versions[-1]
3.6
The index -1 refers to the last element of the list, -2 to the second to last, and so on.


# Index Errors

If you attempt to access an index in a list that does not exist in this list you will get a List Index Exception. This is Python's way of telling you that you are trying to access an index that is not in the list. For example, let's define the following list:

    >>> my_list = ['a','b','c','d','e']

This list has five elements, with the indices 0, 1, 2, 3 and 4.

    >>> my_list[4]
    'e'

As you can see, my_list[4] returns the last element of this list. But what would happen if we tried to access an element at index 5?

    >>> my_list[5]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range

Because the list only contains 5 elements, attempting to access an element at index 5 is really asking Python to give you the sixth element in this list. Since this element does not exist, we received an IndexError.

# Slicing Lists

In addition to accessing individual elements from a list we can use Python's slicing notation to access a subsequence of a list. Consider this list of months,

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

We can slice the third quarter of the year from the months list like this:

    >>> q3 = months[6:9]
    >>> print(q3)
    ['July', 'August', 'September']
    >>> print(months)
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

The index to the left of the colon, 6, is where the slice begins. The slice continues up to the second index, 9.

- Slicing Shorcuts

There are a couple of slicing shortcuts that simplify common situations. If you would like to make a slice that begins at the very beginning of the original list, or that ends at the very end of the original list, you can omit the start or end index like this:

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

We can slice the third quarter of the year from the months list like this:

    >>> q3 = months[6:9]
    >>> print(q3)
    ['July', 'August', 'September']
    >>> print(months)
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Lists, Strings and Mutability

'list' is a type, like 'string', 'float' and 'int'. Of the types we've seen, lists are most like strings: both types support indexing, slicing, the len function and the in operator.

    >>> sample_string = "And Now For Something Completely Different"
    >>> sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
    >>> sample_string[4]
    'N'
    >>> sample_list[4]
    'Terry'
    >>> sample_string[12:21]
    'Something'
    >>> sample_list[2:4]
    ['Terry', 'Eric']
    >>> len(sample_string)
    42
    >>> len(sample_list)
    6
    >>> 'thing' in sample_string
    True
    >>> 'Rowan' in sample_list
    False

Strings are sequences of letters, while list elements can be any type of object. A more subtle difference is that lists can be modified, but strings can't be:

    >>> sample_list[3] = 'Eric'
    >>> print(sample_list)
    ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
    >>> sample_string[8] = 'f'
    TypeError: 'str' object does not support item assignment

The technical term for whether an object can be modified is mutability. Lists are mutable, while strings are immutable. 

# Variable that holds a list

 When we created a variable that held an immutable object, the value of that immutable object was saved in memory. Here we create name with value "Old Woman" and assign it to another variable called person.

    >>> name = "Old Woman"
    >>> person = name
    >>> name = "Dennis"
    >>> print(name)
    Dennis
    >>> print(person)
    Old Woman 


It is the string "Old Woman" that is assigned to person, so when we reassign name to update it to "Dennis", this change is not reflected in the value of person.

Lists are different from strings as they are mutable. 
Here, we create a list called dish with the ingredients of a dish at a café. We assign this same list to the variable mr_buns_order and when we change (mutate) the dish list because an ingredient is unavailable, this affects both dish and mr_buns_order.

    >>> dish = ["Spam", "Spam", "Spam", "Spam", "Spam", "Spam", "baked beans", "Spam", "Spam", "Spam", "Spam"]
    >>> mr_buns_order = dish
    >>> print(dish)
    ['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'baked beans', 'Spam', 'Spam', 'Spam', 'Spam']
    >>> print(mr_buns_order)
    ['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'baked beans', 'Spam', 'Spam', 'Spam', 'Spam']
    >>> dish[6] = "Spam" #baked beans are off
    >>> print(mr_buns_order)
    ['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam']
    >>> print(dish)
    ['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam']

Both dish and mr_buns_order are variable names for the same underlying list, and either name can be used to access and change that list.

# Working with Lists   

These are functions that are useful for working with lists:

- len(some_list)
Returns how many elements are in some_list

- max(some_list)
Returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number:

    >>> batch_sizes = [15, 6, 89, 34, 65, 35]
    >>> max(batch_sizes)
    89

The maximum elements in a list of strings is element that would occur last of the list were sorted alphabetically:

    >>> python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']
    >>> max(python_varieties)
    'Reticulated Python'

This works because the the max function is defined in terms of >, the greater than comparison operator. The > operator is defined for many non-numeric types; if you're working with objects that can be compared with > then you can use max on a list of the objects. 
For strings the standard comparison is alphabetical, so the maximum of this list is the element that appears last alphabetically.
The max function is undefined for lists that contain elements from different, incomparable types:

    >>> max([42, 'African Swallow'])
    TypeError: unorderable types: str() > int()

- min(some_list)
Returns the smallest element in a list. min is the opposite of max.

- sorted(soem_list)
Returns a copy of some_list in order from smallest to largest, leaving some_list unchanged. You can sort from largest to smallest by adding the optional argument reverse=True.

    >>> sorted(batch_sizes)
    [6, 15, 34, 35, 65, 89]
    >>> sorted(batch_sizes, reverse=True)
    [89, 65, 35, 34, 15, 6]
    >>> print(batch_sizes)
    [15, 6, 89, 34, 65, 35]

# Joining Lists

A new string method, join. An example is shown below:

    >>> nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
    >>> print(nautical_directions)
    fore
    aft
    starboard
    port

The join takes a list as an argument, and returns a string consisting of the list elements joined by a separator string. In this example we use the string \n as the separator so that there is a newline between each element.

We can also use other strings (instead of '\n') with .join For instance:

    >>> names = ["García", "O'Kelly", "Davis"]
    >>> "-".join(names)
    "García-O'Kelly-Davis"

It is important to remember to separate each of the items in the list you are joining with a comma (,). Forgetting to do so will not trigger an error, but will also give you unexpected results. 
In the example below omitting the comma between "García" and "O'Kelly" results in the following:

    >>> names = ["García" "O'Kelly", "Davis"]
    >>> "-".join(names)
    "GarcíaO'Kelly-Davis"

Notice how the '-' separator is missing between "García" and "O'Kelly" and instead the two strings were appended? This happens because of Python's default string-literal appending. If .join returns different results then expected.

join will trigger an error if we try to join anything other than strings. For example:

    >>> stuff = ["thing", 42, "nope"]
    >>> " and ".join(stuff)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: sequence item 1: expected str instance, int found

# Appending to Lists
The append method of list objects adds an element to the end of the list.

>>> python_varieties.append('Blood Python')
>>> print(python_varieties)
['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python', 'Blood Python']