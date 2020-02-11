# ----------------------------------------------------------
# --------             HW 3: Part 3.1              ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 3.1: 1.5 hours
# Collaborators and sources: https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.getshapes
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# Write your python program for part 3.1 below:

#set up turtle

import turtle 
wn = turtle.Screen()
bob = turtle.Turtle


#set attributes

wn.bgcolor("black")
turtle.pencolor("white")

#get the word to be used

word = input("Word to be spaced in a circular, clockwise position: ")
num = len(word)
angle = 360 / num

#turns turtle to appropriate starting position facing north    
turtle.left(90)

#for words with even amount of letters or for words with odd amount
if num % 2 == 0:
    for i in word:
        turtle.right(angle)
        turtle.penup()
        turtle.forward(200)
        turtle.write(i, True, align="right", font=("Arial", 16, "normal"))
        turtle.backward(200)
else:
    turtle.right(angle/2)
    for i in word:
        turtle.penup()
        turtle.forward(200)
        turtle.write(i, True, align="right", font=("Arial", 16, "normal"))
        turtle.backward(200)
        turtle.right(angle)
    


#ending
turtle.hideturtle()
wn.exitonclick()
