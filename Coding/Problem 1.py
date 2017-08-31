# Write a function named population_density that takes two arguments, 
# population and land_area (in square kilometres), and returns a population density calculated from those values. 

# Code

def population_density(population, land_area):
    return population/land_area


# To verify the results below are the test cases:

test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))

# After performing the test the results are as follows

expected result: 10, actual result: 10.0
expected result: 7123.6902801..., actual result: 7123.690280065897