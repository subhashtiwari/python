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

