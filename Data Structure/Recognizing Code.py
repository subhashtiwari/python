# n this quiz, you should identify ways in which the implementation of this function could be improved, without removing its current usage. 
# Here are some questions to get you started thinking about this, but you should use your own judgement!

# Reading the code, is it clear what each piece does? How could it be be easier?
# If you needed to change some part of the functionality, would that be easy? Would you have to change the same thing in several places?
# If you break down what the function does into steps, how many steps are there? It's best to have each function doing only one thing.
# Is there unnecessary repetition? Does every piece of code get used? Could anything be more succinct whilst still being readable? This is called the DRY (Don't Repeat Yourself) principle.

    def check_answers(my_answers,answers):
        """
        Checks the five answers provided to a multiple choice quiz and returns the results.
        """
        results= [None, None, None, None, None]
        if my_answers[0] == answers[0]:
            results[0] = True
        elif my_answers[0] != answers[0]:
            results[0] = False
        if my_answers[1] == answers[1]:
            results[1] = True
        elif my_answers[1] != answers[0]:
            results[1] = False
        if my_answers[2] == answers[2]:
            results[2] = True
        elif my_answers[2] != answers[2]:
            results[2] = False
        if my_answers[3] == answers[3]:
            results[3] = True
        elif my_answers[3] != answers[3]:
            results[3] = False
        if my_answers[4] == answers[4]:
            results[4] = True
        elif my_answers[4] != answers[4]:
            results[4] = False
        count_correct = 0
        count_incorrect = 0
        for result in results:
            if result == True:
                count_correct += 1
            if result != True:
                count_incorrect += 1
        if count_correct/5 > 0.7:
            return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
        elif count_incorrect/5 >= 0.3:
            return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."


    def check_answers(my_answers,answers):
        #1 variable names are not easy to tell apart
        """
        Checks the five answers provided to a multiple choice quiz and returns the results.
        """
        #2 Code will only work if there are exactly five answers
        results= [None, None, None, None, None]
        #3 Repeated code would be better as a separate function
        if my_answers[0] == answers[0]:
            results[0] = True
        elif my_answers[0] != answers[0]:
            results[0] = False
        #4 if and elif could be clearer with if and else
        if my_answers[1] == answers[1]:
            results[1] = True
        elif my_answers[1] != answers[0]:
            results[1] = False
        if my_answers[2] == answers[2]:
            results[2] = True
        elif my_answers[2] != answers[2]:
            results[2] = False
        if my_answers[3] == answers[3]:
            results[3] = True
        elif my_answers[3] != answers[3]:
            results[3] = False
        if my_answers[4] == answers[4]:
            results[4] = True
        elif my_answers[4] != answers[4]:
            results[4] = False
        #6 this function does several things in one long block
        count_correct = 0
        count_incorrect = 0
        for result in results:
        #7 The code counts both correct and incorrect answers.
            if result == True:
                count_correct += 1
            if result != True:
                count_incorrect += 1
        if count_correct/5 > 0.7:
        #8 The pass rate has been hard-coded into the function
            return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
        elif count_incorrect/5 >= 0.3:
            return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."


1. The names my_answers and answers were quite similar, which made it a bit confusing. Set better names for these parameters and put their definitions in the docstring for reference.

2. The fact that there are five questions in the quiz is vital to the working of the code. Although this constraint doesn't stop it working properly, if one day we had a quiz with ten questions it would be nice to be able to reuse that same code.

3. The parts that checked the answers, were repeated five times! This would be far better as a separate function that checks an answer.

    if my_answers[1] == answers[1]:
        results[1] = True
    elif my_answers[1] != answers[0]:
        results[1] = False

4. There are a few places where if and elif were used but the boolean expression in the elif clause is just what's leftover after the if. The program would work the same but be easier to read if we used if and else in those cases.

5. There are no inline comments explaining what the code does.

6. It seems as though this function does several things -- it checks each answer, and then it adds up the number of correct and incorrect answers, and then it outputs a message. At least some of that should be separated out.

7. If every question is either correct or incorrect, and we know how many questions there are, there's no need to count both the number of correct and incorrect answers. We could also make the code shorter by using a sum to count the correct answers in results.

8. The proportion of correct answers in the boundary of passing the quiz is hard-coded, and doesn't need to be.

              