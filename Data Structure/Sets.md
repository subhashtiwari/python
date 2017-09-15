# Removing Duplicates from Lists

Imagine that you run a popular search engine and you've surveyed your users to see where they're browsing from. You've collected the 785 responses and have assembled them into a list of counttries.

    >>> len(countries)
    785
    >>> countries[:5]
    ['Angola', 'Maldives', 'India', 'United States', 'India']

 There aren't 785 countries in the world, which means that there are probably duplicate entries in the countries list. Slicing the list to see the first few elements confirms this. 
 It would be useful to remove the duplicates to produce a list of all of the countries that users browse from.

# Sets

Removing duplicates from lists with a for loop works, but there is an alternative technique. Python includes several data structures other than lists for storing collections, and one of them is perfectly suited for storing unique elements: sets.

Sets are collections of unique elements without any particular ordering. We can create a set from a list like this:

    >>> country_ set = set(countries)
    >>> len(country_set)
    196

Sets support the in operator the same as lists do:

    >>> 'Mauritius' in countries
    True
    >>> 'Mauritius' in country_set
    True

You can add elements to sets, but you don't use the append method like lists, instead sets have the add method:

    country_set.add("Florin")

Sets also have a pop method, just like lists. When you pop an element from a set a random element is removed (remember that sets, unlike lists, are unordered so there is no "last element").

You can iterate over a set using a for loop in the same manner that you can iterate over a list.

