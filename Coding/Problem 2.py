# Write a function  named readable_timedelta. The fuction should take one argument, an integer days, and return a string that says how many weeks and days that is. 
# For example, readable_timedelta(10) should return, 1 week(3) and 3 days(s).
# Also include a docstring that expalins what the function does.

def readable_timetable(days):
    """Print the number of weeks and days in a number of days."""

    # to get the number of weeks we use integer division

    weeks = days//7

    # to get the number of days that remain use %, the modulus operator

    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)