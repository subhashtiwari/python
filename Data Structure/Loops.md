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

    # modify the names list in place
    for index in range(len(names)): # iterate over the index numbers of the names list
        names[index] = names[index].title() # modify each element of names

To create a new list we can start with an empty list ([]) and then use the append method to add new items. Modifying a list is a bit more involved, and requires the use of a new function: range. 
The range function takes one argument, an integer n, and returns the sequence of numbers from zero to n-1.

    >>> for number in range(4):
    >>>     print(number)
    0
    1
    2
    3

We use the range function to generate the indexes for each value in the the names list. This lets us access the elements of the list with names[index] so that we can update the values in the names list.

# While Loops

For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times. A for loop over a list executes the body once for each element in the list. 
A for loop using the range function will execute the number of times specified by the range function call. This differs from "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met. 

Consider this while loop that simulates a blackjack dealer by drawing cards from a deck list into a hand list, stopping when the value of the cards in the hand is 17 or more.

    card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
    hand = []

    while sum(hand) <= 17:
        hand.append(card_deck.pop())

    print(hand)

This example features a new function, sum, and a new list method, pop. sum is pretty intuitive, it calculates the sum of the elements in a list. The pop method is the inverse of the append method, pop removes an element from a list and returns it. 

- The syntax of while loops:

        while sum(hand) <= 17:
            hand.append(card_deck.pop())

1. The while keyword indicates that this is a while loop

2. Next is a test expression, in this example sum(hand) <= 17. If this expression is true, the loop's body will be executed. The test expression is evaluated again after the loop's body runs. This process of checking the test expression and running the loop repeats until the expression becomes false.

3. The loop's body is indented with four spaces. If the value of the test expression never changes, the result is an infinite loop! In this example the loop's body appends numbers to the hand list, which increases the value of sum(hand).

# Stopping for a break 

For loops iterate over every elements in a sequence, and while loops iterate until their stopping condition is met. This is sufficient for most purposes, but we sometimes need more precise control over when a loop should end. In these cases, we use the break keyword.

A loop will terminate immediately if it encounters a break statement. We can use this to end a loop if we detect that some condition has been met. The break keyword can be used in both for and while loops.


- The manifest in this example is a list of list. We have seen lists before, and you can also have list elements that are themselves lists- this is the case with the manifest variable. Each element in the manifest list is a list itself, one that contains two things: an item and its weight.

    # each item in the manifest is an item and its weight
    manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

    cargo_weight = 0
    cargo_hold = []

    for cargo in manifest:
        if cargo_weight >= 100:
            break
        else:
            cargo_hold.append(cargo[0])
            cargo_weight += cargo[1]

The code is intended to stop the weight of the cargo on the boat from going over the stated limit of 100. Let's check what we've put in the boat.

    >>> print(cargo_weight)
    211
    >>> print(cargo_hold)
    ['bananas', 'mattresses', 'dog kennels', 'machine that goes ping!']

The boat is severely over its weight limit. The break statement prevented us for putting every item on the boat, but we still exceeded the limit.

One strategy we can use is to include calls to print in the code. This is a really handy technique, as it can give us some insight into the state of the data as the code is running step-by-step. 
If we choose what to print well (and give context), this might help us to find the bug.

Here's the loop with debugging statements added.

cargo_weight = 0
cargo_hold = []

    for cargo in manifest:
    print("debug: the weight is currently: {}".format(cargo_weight))
    if cargo_weight >= 100:
        print("debug: breaking loop now!")
        break
    else:
        print("debug: adding item: {}".format(cargo[0]))
        print("debug: with weight: {}".format(cargo[1]))
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]

And this is output of the annotated loop:

    debug: the weight is currently: 0
    debug: adding item: bananas
    debug: with weight: 15
    debug: the weight is currently: 15
    debug: adding item: mattresses
    debug: with weight: 34
    debug: the weight is currently: 49
    debug: adding item: dog kennels
    debug: with weight: 42
    debug: the weight is currently: 91
    debug: adding item: machine that goes ping!
    debug: with weight: 120
    debug: the weight is currently: 211
    debug: breaking loop now!   

By reading this printed debug log we can see that the loop adds items to the cargo hold correctly, but it adds one extra item after the weight limit is met.
    