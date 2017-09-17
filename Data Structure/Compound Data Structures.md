# A Dictionary of Dictionaries

In the dictionary elements,

    elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}

This dictionary maps element names (strings) to their atomic numbers (ints). 
But what if we wanted to store more information about each element, like their weight and symbol? We can do that by adjusting the dictionary so that it maps element names (strings) to a dictionary that stores that collection of data:

    elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
                'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

We can look the information about an entry in this nested dictionary in the same ways we did before, with square brackets or the get method:

    >>> print(elements['helium'])
    {'number': 2, 'symbol': 'He', 'weight': 4.002602}
    >>> print(elements.get('unobtainium', 'There\'s no such element!'))
    There's no such element!

We can look up specific information from the helium dictionary like this:

    >>> print(elements['helium']['weight'])
    4.002602    

This code is first looking up the key "helium" in the elements dictionary, producing the helium dictionary. The second lookup, ['weight'] then looks up the "weight" key in that helium dictionary to find helium's atomic weight.
    
    