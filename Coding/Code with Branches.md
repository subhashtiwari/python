- if in Python

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

if 