# ----------------------------------------------------------
# --------             HW 2: Part 3.3              ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 3.3: 2 hours
# Collaborators and sources: n/a
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# Write your python program for part 3.3 below:

grossincome = float(input("What is your gross income? "))
totaldeduction = float(input("What is your total deduction? "))

#taxable income = gross income - total deductions

taxableincome = int(grossincome - totaldeduction)
print("Your taxable income is ", taxableincome)

if taxableincome in range(0, 9325):
    taxowed = taxableincome * .1
    print("You owe $"+str(taxowed), "in federal taxes")

if taxableincome in range(9325, 37950):
    taxowed = 932.5 + (.15 * (taxableincome - 9325))
    print("You owe $"+str(taxowed), "in federal taxes")

if taxableincome in range(37950, 91900):
    taxowed = 5226.25 + (.25 * (taxableincome - 37950))
    print("You owe $"+str(taxowed), "in federal taxes")

if taxableincome in range(91900, 191650):
    taxowed = 18713.75 + (.28 * (taxableincome - 91900))
    print("You owe $"+str(taxowed), "in federal taxes")

if taxableincome in range(191650, 416700):
    taxowed = 46643.75 + (.33 * (taxableincome - 191650))
    print("You owe $"+str(taxowed), "in federal taxes")

if taxableincome in range(416700, 418400):
    taxowed = 120910.25 + (.35 * (taxableincome - 416700))
    print("You owe $"+str(taxowed), "in federal taxes")

if taxableincome in range(418400, 99999999999999999999999999):
    taxowed = 121,505.25 + (.396 * (taxableincome - 418400))
    print("You owe $"+str(taxowed), "in federal taxes")
