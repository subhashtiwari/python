Imagine that you work for a consumer ratings website. Users submit reviews and scores for products they use, and you show the results so that consumers can make informed choices.

Throughout this section we will write a function that takes as input five scores and aggregates them to output a single rating.

Because the highest and lowest scores might be outliers and skew the results, we will take the three middle scores out of the five, discarding the highest and lowest.

Then we will take the average (mean) of those three middle scores.

For example, if the scores are 1,2,2,4,4 then we take the average of 2, 2 and 4 to get 2.6666666666.

Then we will map that average score to a written rating like this:

Average Score	Rating
0 <= score < 1	Terrible
1 <= score < 2	Bad
2 <= score < 3	OK
3 <= score < 4	Good
4 <= score <= 5	Excellent

We will do this step by step

- The function should be like this:

def scores_rating(score1,score2,score3,score4,score5):

""" This turns five scores into a rating by averaging the middle three of the five scores and assigning this average to a written rating
"""
# THE CODE GOES HERE!

return rating

This is just the skeleton of what the function will actually do, but it's got the inputs and the output and the docstring to describe what it's going to do.

- The steps should be like this:
 
def scores_rating(score1,score2,score3,score4,score5):
    
""" This turns five scores into a rating by averaging the middle three of the five scores and assigning this average to a written rating
"""

    # STEP 1 convert scores to numbers

    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 find middle three scores
    #how am I going to do this?

    #STEP 3 take average of middle three scores

    average_score = # (sum of the middle scores)/3

    #STEP 4 turn average score into a rating

    rating = score_to_rating_string(average_score)

    return rating
 

Now we need some helper functions: convert_to_numeric and score_rating_string. 

For step 2, getting the middle values is a tricky one, but as we only need the sum of the scores, not the actual values. Python has built-in functions for min() and max().

sum_of_three_middle_scores = sum_of_all_five_scores - min(all five scores) - max(all five scores)

Separating Step 2 and Step 3 made sense at the time, but turned out to be the wrong way to implement this- the implementation is easier if we merge them and avoid having to figure out the three middle scores separately. 

The new outline of the scores_rating() function

def scores_to_rating(score1,score2,score3,score4,score5):
    
""" This turns five scores into a rating by averaging the middle three of the five scores and assigning this average to a written rating
"""

    #STEP 1 convert scores to numbers

    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores

    average_score =  sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating

    rating = score_to_rating_string(average_score)

    return rating
