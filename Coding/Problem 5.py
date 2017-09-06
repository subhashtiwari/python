# Rewrite the which_prize() function from earlier to use what you've learned about truth values. 
# Start your function by setting the variable prize = None, change the prize depending on the number of points and then use another conditional to return a message depending on whether prize is there or not. 
# This will avoid repeating the return part of the code.

def which_prize(points):
    
    prize = None
    if points <= 50:
        prize = "wooden rabbit"
    elif 150 <= points <= 180:
        prize = "wafer-thin mint"
    elif points >= 181:
        prize = "penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."