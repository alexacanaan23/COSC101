# ----------------------------------------------------------
# --------              HW 5: Part 2               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 1: 15 minutes
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# There is some starter code in this function.  Do
# not change this code.  Simply add your cases to the
# function provided.

############# Do not change following function #################

import version1 as longest_item_sequence

def test_longest_item_sequence(parameter, expected_output):
    '''Calls longest_item_sequence with parameter and checks
       that the expected output matches the actual output.
       parameter -> (list) to be passed to function
       expected_output -> what the output of the function
                          should be when it is passes parameter.
       returns 0 if test Failed, 1 otherwise
    '''

    function_output = longest_item_sequence(parameter)
    if function_output != expected_output:
        print("Test longest_item_sequence(",parameter,") Failed!")
        print("\t Expected Output: ", expected_output)
        print("\t Actual Output: ", function_output)
        return 'Failed'
    else:
        print("Test longest_item_sequence(",parameter,") Failed!")
        print("\t Expected Output: ", expected_output)
        return 'Passed'

############# Do not change above function #################

# Write your python code for part 2 by adding to the
# function below:

def run_tests():

    passed = 0           #count of tests that passed
    total_tests = 0      #how many tests were run

    # Test Longest Sequence in Middle of List
    total_tests += 1
    result = test_longest_item_sequence([1, 2, 9, 9, 9, 3, 4],[9, 9, 9])
    passed += result

    #Add your tests here

    total_tests += 2
    result = test_longest_item_sequence([], [])
    passed += result

    total_tests += 3
    result = test_longest_item_sequence([0],[0])
    passed += result

    total_tests += 4
    result = test_longest_item_sequence([1, 1, 2, 2], [1, 1])
    passed += result

    total_tests += 5
    result = test_longest_item_sequence([111, 2, 2, 2,], [2, 2, 2])
    passed += result

    

    # At the end print out a summary of how
    # many tests failed and how many Passed
    print("Testing Complete.")
    print(passed, "of", total_tests, "passed")

run_tests()
