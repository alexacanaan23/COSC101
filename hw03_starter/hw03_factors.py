# ----------------------------------------------------------
# --------             HW 3: Part 2                ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have finished
# debugging this program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 2: 45 minutes
# Collaborators and sources: n/a
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

### This program finds and displays information about the
### factors of an entered positive integer.

### Program 1: Factors

# prompt user for number to find factors of
x = int(input("Enter a positive integer: "))

# find and display factors of entered numner
num_factors = 0
for i in range(1, x + 1):
        if x % i == 0:
                print(i, '*', int(x / i), '=', x)
                num_factors += 1

# display information about factors of the number
if num_factors == 2:
    print(x, "is a prime number.")
elif num_factors == 1:
    print("You entered the number", str(x) +'.', x, "only has 1 factor, itself!")
elif num_factors > 2:
    print(x, "has", num_factors, "factors.")
elif num_factors < 1:
    print("You did not enter a positive integer.")
