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
The element dictionary uses strings for its keys. However, it's not even necessary for every key to have the same type.q    

# What's in the Dictionary?

We can check whether a value is in a dictionary on the same way we check whether a value is in a list or set with the 'in' keyword.

    if 'mithril' in elements:
        print("That's a real element!")
    else:
        print("There's no such element!')

We can use 'in' to verify whether a key is in the dictionary before looking it up, if there's a possibility that the key isn't there.

Dicts have a related method that's also useful, get. get looks up values in a dictionary, but unlike square brackets, get returns None (or a default value of your choice) if the key isn't found. If you expect lookups to sometimes fail, get might be a better tool than normal square bracket lookups.

    >>> elements.get('dilithium')
    None
    >>> elements['dilithium']
    KeyError: 'dilithium'
    >>> elements.get('kryptonite', 'There\'s no such element!')
    "There's no such element!"   

In the last example we specified a default value (the string 'There\'s no such element!') to be returned instead of None when the key is not found.

# Iterating over Dicts and Sets

We can use for loops to iterate over sets and dicts, much in the same way we iterate over lists. We iterate over sets like this:

    >>> colors = set(['Pthalo Blue', 'Indian Yellow', 'Sap Green'])
    >>> for color in colors:
    ...    print(color)
    ...
    Indian Yellow
    Sap Green
    Pthalo Blue
            
Notice that the for loop didn't print the colors in the same order they were inserted into the set. Sets don't track ordering the way lists do, so iterating over them produces values in an arbitrary order.

The syntax for iterating over dictionaries is very similar. The difference is that dicts store key value pairs, and when we loop over them we iterate through the keys:

    Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
        "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
        "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
        "Sgt. Pepper's Lonely Hearts Club Band": 1967,
        "Magical Mystery Tour": 1967, "The Beatles": 1968,
        "Yellow Submarine": 1969 ,'Abbey Road': 1969,
        "Let It Be": 1970}

    for album_title in Beatles_Discography:
        print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))

We can use the key album_title to get to each value in the the dict: Beatles_Discography[album_title].
