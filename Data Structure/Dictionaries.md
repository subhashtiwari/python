# Dictoinaries
Sets are simple data structures, and they have one main use: collecting unique elements. Our next data structures, dictionaries, are more flexible. 
Rather than storing single objects like lists and sets do, dictionaries store pairs of elements: keys and values. 

In this example we define a dictionary where the keys are element names and the values are their corresponding atomic numbers.

    elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}

We can look up values in the dictionary using square brackets enclosing a key:

    >>> print(elements['carbon'])

We can also insert new values into the dictionary with square brackets:

    >>> elements['lithium'] = 3
    >>> print(elements['lithium'])
    3

Dictionary keys are similar to list indices: we can select elements from the data structure by putting the index/key in square brackets. Unlike lists, dictionaries can have keys of any immutable type, not just integers. 
The element dictionary uses strings for its keys. However, it's not even necessary for every key to have the same type.    