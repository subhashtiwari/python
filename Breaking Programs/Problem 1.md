In this quiz add outlines for the helper functions that are needed for scores_rating. Include the definition line, a docstring describing the function and a return statement. 
There is no need to actually include any of the code contained in the function at this stage.

The functions you need to outline are:

convert_to_numeric for STEP 1
sum_of_middle_three for STEP 2 and STEP 3
score_to_rating_string for STEP 4

# Solution

def convert_to_numeric(scores):
    """
    Convert the score to a numerical type.
    """
    converted_score = #convert the scores

    return converted_score

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    sum = # add all the five scores and subtract the min and max

    return sum

def score_to_rating_string(score):
    """
    Convert the average score, that should be between 0 and 5, into a string rating.

    rating = 
    return rating

def scores_rating(score1,score2,score3,score4,score5):

    """
    This turns the five scores into a rating by averaging the middle three of the the five scores and assigning this average to a written rating.
    """

    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score =     
        sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating
