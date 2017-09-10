# For Loops

We use lists to store sequences of data, and we use for loops to iterate over lists. Consider this for loop that capitalizes the each name in a list of names and prints them:

    names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
            'nigel incubator-jones', 'philip diplodocus mallory']

    for name in names:
        print(name.title())

Running this code gives this output:

Charlotte Hippopotamus Turner
Oliver St. John-Mollusc
Nigel Incubator-Jones
Philip Diplodocus Mallory

Let's examine the for loop syntax:
        for name in names:
        print(name.title())

1. The for keyword signals that this is a for loop.

2. The rest of the line specifies what we're iterating over. names is the list that this for loop iterates over. name is this loop's iteration variable. The body of the for loop will be executed once for each element in names, and the iteration variable name can be used in the loop's body to refer to the element that the loop is currently processing.

3. The body of a for loop is indented four spaces, and is run once for each element in the list.

A note about naming You can name iteration variables however you like. 
This example demonstrates a common pattern though, the list names has a plural name ending in "s", and the iteration variable is the singular word with no "s". 
Naming lists and iteration variables in this style makes it easier for other programmers to understand what the different variables are for.

# Building Lists with Loops

The loops we've written so far extract information from lists. We can also use for loops to create lists, and to modify lists. Consider our list of uncapitalized names from earlier,

    names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
            'nigel incubator-jones', 'philip diplodocus mallory']

If we don't want to keep the uncapitalized list around, we can overwrite it instead of making a new list.

