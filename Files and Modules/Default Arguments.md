# Default Argument Values

Let's revisit the starbox function from earlier on, but with one modification. This box function can use any symbol to draw boxes, not just *.

def box(width, height, symbol):
    """print a box made up of asterisks, or some other character.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    symbol: a single character string used to draw the box edges
    """
    print(symbol * width) # print top edge of box

    # print sides of box
    for _ in range(height-2):
        print(symbol + " " * (width-2) + symbol) 

    print(symbol * width) # print bottom edge of box

This added functionality is nice, but when we call the function we have to specify an extra argument. This is a pain if we just want to draw a box and don't care what symbol is used. 
Fortunately there is a Python feature that allows the flexibility of the extra argument, without requiring extra effort when the flexibility isn't needed.

We can specify a default value for the symbol argument by changing the first line of the function to this:

    def box(width, height, symbol='*'):

Now we can call the function with two arguments or three. If the third argument is omitted then * will be used as the default value.

>>> box(7, 5)
*******
*     *
*     *
*     *
*******

>>> box(7, 5, '#')
#######
#     #
#     #
#     #
#######

