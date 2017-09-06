# if in Python

Code with branches - in which the code that gets executed depends on some condition or conditions - is really useful in many programming situations. 
A conditional expression or if statement is used to control whether a block of code will be run. 

For example 
There is a billing system for a pay-as-you-go mobile phone. The customer can set up a link to their bank account so that if their phone credit balance goes below a threshold amount, more credit is added and their bank balance is billed.

if phone_balance < 10:
phone_balance +=10
bank_balance -= 10

1. The if keyword indicates that this line is a conditional expression.
2. Following if is phone_balance < 10, the condition to be checked. This part is a boolean expression - an expression that evaluates too either True or False.
3. The conditional expression (or "if statement") ends with a colon.
4. This line is followed by an indented block of code, in this case:

            phone_balance += 10
            bank_balance -= 10

    This indented block of code will be executed if the boolean expression evaluates to True. If the boolean expression evaluates to False, the indented block will not be executed.

The value of the boolean expression --the pieceof the conditional expression that evaluates to either True or False is the part of the code that defines what happens when th ecode is run. 
One common format of a boolean expression is to use a comparison operator, such as >, <=, == or !=. 

However simple or complex, a boolean expression must evaluate to either True or False and it is this value that decides whether the indented block executes or not.

# Code with more branches: if, elif, and else

When we want to do one thing if a condition is true, and a different thing if that condition is false. 
The code block indented after the 'if' statement will be run if the boolean expression evaluates to True.
'else' keyword can be used to give the alternative: what to do if the boolean expression is False.

The code below prints a message indicating whether an integer is even or odd.

if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")


The else keyword is always followed by a colon and doesn't need a boolean expression - it is simply what happens when the boolean expression from the 'if' statement is False.

If there were more possible cases than two, it would be useful to have another conditional expression along with the 'else' case. Python has a special keyword, 'elif' (short for else - if) to deal with this situation. This saves the multiple indentation that would be needed if we used else and then another 'if' statement inside the 'else' block.

In this example, the conditional statements are inside a function called garden_calendar.

def garden_calendar(season):
    if season == "spring":
        print("time to plant the garden!")
    elif season == "summer":
        print("time to water the garden!")
    elif season == "autumn" or season == "fall":
        print("time to harvest the garden!")
    elif season == "winter":
        print("time to stay indoors and drink tea!")
    else:
        print("I don't recognize that season")


Like 'if' an 'elif' statement always require a conditioal expresion.

# Composing Boolean Expressions

To check compound conditions like these in conditional expressions, we use boolean operations in Python -- keywords like and, or and not -- to put simpler boolean expressions together. So these examples could be put into code as:

if is_raining and is_sunny:
    print("Is there a rainbow?")


if (not do_not_email) and (location == "USA" or location == "CAN"):
    send_email()

 Use and, or and not to combine and change boolean expressions, following the usual rules of logic. The final result after combining all boolean expressions is what will determine whether or not the code in the indented if block is run or not.

'and' and 'or' each work on two boolean expressions, one before and one afterwards. 'and' will give the result 'True' if and only if both of two expressions are 'True', otherwise it will be 'False'. 'or' will give the result 'True' if at least one of the two expressions is 'True' - only if both are 'False' will it give the result 'False'. (Note that if both are 'True', 'or' will still give 'True'.)

The boolean operation 'not' works on a single boolean to swap it: so not True is False and vice versa.

For really complicated conditions we might need to combine some and's, or's and not's together - use parentheses ( and ) if we need to to make the combinations clear.

- True and False are both booleans but it is not a good idea to use if True: or if False:.
- Boolean operators and, or and not have specific meanings that aren't quite the same as their common meanings - don't fall into the trap of writing plain English unless it's also valid Python.
- Do not compare a variable that is a boolean with == True or == False - it's more readable to avoid such a comparison.


# Functoins with multiple possible returns

We can create functions that have more than one return in there definition using branches in code.
Calling a function will return at most once (some of them not at all). However, we can include multiple return statements in the definition of a function. Only onee of them will return when the function is run.

By using conditional statements, codes can be made more readable and concise. 
For example:

def punctuate(sentence, phrase_type):
    """
    Create a punctuated sentence from a string. Defaults to an ordinary
    sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create. 
                "exclamation", "question" and "aside" are known values.
    """
    if phrase_type == "exclamation":
        sentence_punct = sentence + "!"
    elif phrase_type == "question":
        sentence_punct = sentence + "?"
    elif phrase_type == "aside":
        sentence_punct = "(" + sentence + ".)"
    else:
        sentence_punct = sentence + "."
    return sentence_punct

In this implementation of the function, we create a punctuated sentence from the input sentence and appropriate punctuation in each case, depending on the kind of punctuation required.

Once the punctuated sentence has been constructed, the work of the function has been mostly done, but we're waiting until the end to return the constructed sentence.

An alternative would be:

def punctuate2(sentence, phrase_type):
    """
    Create a punctuated sentence from a string. Defaults to an ordinary
    sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create. 
                "exclamation", "question" and "aside" are known values
    """
    if phrase_type == "exclamation":
        return sentence + "!"
    elif phrase_type == "question":
        return sentence + "?"
    elif phrase_type == "aside":
        return "(" + sentence + ")"
    else:
        return sentence + "."

The return statements come inside the indented blocks after conditional statements. Because the main work of the function is really done inside each of the branches.
As soon as return is executed in a function, execution will leave that function. This means that you should see every return as a possible exit from the function.

# Truth values of non-boolean objects

The structure of a conditional so far  has been

    if boolean_expression:
        intented_code

and the boolean_expressions have been expressions that evaluate to a boolean object - either True or False.

If we put some other object that is not a boolean in theif statement in place of the boolean expression, Python will check for its 'truth value' and ues that to decide whether or not to run the intended code.

The "Python Documentation" lists all the objects that are considered 'False' in this situation. Any number that is 0, an object that is 'None' or an empty string will have a truth value of 'False'. Anything that isn't listed as having a truth value 'False' will count as 'True'.

