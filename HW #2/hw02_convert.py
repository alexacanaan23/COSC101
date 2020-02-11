# ----------------------------------------------------------
# --------             HW 2: Part 2                ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have finished
# debugging this program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 2: 25 minutes
# Collaborators and sources:n/a
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# Convert a measurement in inches to feet, meters, and kilometers:

inches = int(input("Enter a measurement in inches (positive integers only): "))
feet = inches // 12
##inches = int(inches % 12)
print(str(feet) + "' " + str(inches % 12) + '" ')
meters = float(inches / 39.3701)
print(str(meters) + " meters")
kilometers = meters / 10 ** 3
print(str(kilometers) + " kilometers")
