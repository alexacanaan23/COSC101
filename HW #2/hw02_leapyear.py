# ----------------------------------------------------------
# --------             HW 2: Part 3.1              ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 3.1: 10 minutes
# Collaborators and sources: https://support.microsoft.com/en-us/help/214019/method-to-determine-whether-a-year-is-a-leap-year
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# Write your python program for part 3.1 below:

YOB = int(input("What year were you born?"))
##YOB must be divisible by 4 and 400 according to leap year rules
if YOB % 4 == 0 and YOB % 400 == 0:
    print(str(YOB) + " was a leap year")
else:
    print(str(YOB) + " was not a leap year")
