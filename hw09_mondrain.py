# ----------------------------------------------------------
# --------              HW 9: Part 1               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 1: 8 hours
# Collaborators and sources: lab hours, office hours 
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

import turtle
import random

WIDTH = 1024
HEIGHT = 768

def mondrian(x, y, w, h, t):
  # Write your code here
  # You will want to create other Functions
  # for good program design
  
  W = random_int_gen(w)
  H = random_int_gen(h)
  
  t.setx(x)       #sets coordinates, turtle will always face east/right to begin
  t.sety(y)

  if w > (.5 * WIDTH) and h > (.5 * HEIGHT):      #checks if the region is wider than half the initial canvas size and the region is taller than half the inital canvas height
    neww, newh = split4ways(x, y, w, h, t)        #region is split into 4 smaller ones
    mondrian(x, y, neww, newh, t)
    mondrian((x + neww), y, (w-neww), newh, t)
    mondrian((x + neww), (y + newh), (w - neww), (h - newh), t)
    mondrian(x, (newh + y), neww, (h - newh), t)

  elif w > (.5 * WIDTH):                          #if the region is wider than half the initial canvas size
    neww = splitVert(x, y, w, h, t)               #region is split into 2 smaller ones w/ vertical line
    mondrian(x, y, neww, h, t)
    mondrian((x + neww), y, (w-neww), h, t)
    
  elif h > (.5 * HEIGHT):                         #if the region is taller than half the initial canvas size
    newh = splitHoriz(x, y, w, h, t)              #region is split into 2 smaller ones w/ horizontal line
    mondrian(x, y, w, newh, t)
    mondrian(x, (y + newh), w, (h-newh), t)

  elif W >= 120 and H >= 120 and W < w and H < h: #randomly chooses to split horizontally and vertically
    neww, newh = split4ways(x, y, w, h, t)        #region is split into 4 smaller ones
    mondrian(x, y, neww, newh, t)
    mondrian((x + neww), y, (w-neww), newh, t)
    mondrian((x + neww), (y + newh), (w - neww), (h - newh), t)
    mondrian(x, (newh + y), neww, (h - newh), t)
   
  elif W >= 120 and W < w:                        #randomly chooses to split vertically
    neww = splitVert(x, y, w, h, t)               #region is split into 2 smaller ones
    mondrian(x, y, neww, h, t)
    mondrian((x + neww), y, (w-neww), h, t)
   
  elif H >= 120 and H < h:                        #randomly chooses to split horizontally
    newh = splitHoriz(x, y, w, h, t)              #region is split into 2 smaller ones           
    mondrian(x, y, w, newh, t)
    mondrian(x, (y + newh), w, (h-newh), t)
    
  else:                                           #when it can't be split anymore, fill it with a color
    fill_color(t)     
    t.begin_fill()
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.end_fill()
    t.left(90)
    
    

def fill_color(t):
  '''fills the region'''
  r = random.random()
  if r < .0833:               #probability of filling a region red
    t.fillcolor('red')
  elif r < .1667:             #probability of filling a region blue
    t.fillcolor('blue')
  elif r < .25:               #probability of filling a region yellow
    t.fillcolor('yellow')
  else:                       #probability of filling a region white
    t.fillcolor('white')
  
def random_int_gen(x):
  '''randomly decides whether or not to split'''
  extralength = x * 1.5
  integer = int(random.uniform(120, extralength))     #generates a num b/w 120 and w *1.5 to split
  return integer


def random_split():
  '''choose the split point'''
  return random.randint(33, 67) / 100   #chooses the percent between 33 and 67 to split at

##def split_region(w, h):
##  '''decides how to split the region'''

def splitVert(x, y, w, h, t):
  '''splits region with a vertical line into 2 regions'''
  t.setx(x)
  t.sety(y)
  
  pVert = random_split()
  neww = w * pVert
  
  t.forward(w * pVert)        #draws the left box
  t.left(90)
  t.forward(h)
  t.left(90)
  t.forward(w * pVert)
  t.left(90)
  t.forward(h)
  t.left(90)
  
  t.penup()                   #draws the right box
  t.forward(w * pVert)
  t.pendown()
  t.forward(w - neww)
  t.left(90)
  t.forward(h)
  t.left(90)
  t.forward(w - neww)
  t.left(90)
  t.forward(h)
  t.right(90)
  t.penup()
  t.forward(neww)
  t.left(180)
  t.pendown()
  
  return neww

def splitHoriz(x, y, w, h, t):
  '''splits region with a horizontal line into 2 regions'''
  t.setx(x)
  t.sety(y)
  pHoriz = random_split()
  newh = h * pHoriz
  
  t.forward(w)                #draws the bottom box
  t.left(90)
  t.forward(h * pHoriz)
  t.left(90)
  t.forward(w)
  t.left(90)
  t.forward(h* pHoriz)
  t.left(90)
  
  t.left(90)                  #draws the top box
  t.forward(h)
  t.right(90)
  t.forward(w)
  t.right(90)
  t.forward(h - newh)
  t.right(90)
  t.forward(w)
  t.left(90)
  t.forward(newh)
  t.left(90)
  
##  t.left(90)
##  t.forward(h * pHoriz)
##  t.right(90)
##  t.forward(w)
##  t.right(90)
##  t.forward(h * pHoriz)
##  t.right(90)
##  t.forward(w)
##  t.left(180)
  return newh

def split4ways(x, y, w, h, t):
  '''splits the region with a horizontal line and a vertical line into 4 regions'''
  newh = splitHoriz(x, y, w, h, t)
  neww = splitVert(x, y, w, h, t)
##  pVert = random_split()
##  pHoriz = random_split()
##  neww = w * pVert
##  newh = h * pHoriz
##  
##  t.setx(x)
##  t.sety(y)
##  
##  t.forward(w * pVert)
##  t.left(90)
##  t.forward(h)
##  t.left(90)
##  t.forward(w * pVert)
##  t.left(90)
##  t.forward(h)
##  t.left(90)
##  
##  t.penup()
##  t.forward(w * pVert)
##  t.pendown()
##  t.forward(w - neww)
##  t.left(90)
##  t.forward(h)
##  t.left(90)
##  t.forward(w - neww)
##  t.left(90)
##  t.forward(h)
##  t.right(90)
##  t.penup()
##  t.forward(neww)
##  t.left(180)
##  t.pendown()
##
##  t.forward(w)                      
##  t.left(90)
##  t.forward(h * pHoriz)
##  t.left(90)
##  t.forward(w)
##  t.left(90)
##  t.forward(h* pHoriz)
##  t.left(90)
##
##  t.left(90)                        
##  t.forward(h)
##  t.right(90)
##  t.forward(w)
##  t.right(90)
##  t.forward(h - newh)
##  t.right(90)
##  t.forward(w)
##  t.left(90)
##  t.forward(newh)
##  t.left(90)

  return neww, newh


def main():
  # Create a window with a canvas
  t = turtle.Turtle()
  wn = turtle.Screen()
  wn.setworldcoordinates(0, 0, WIDTH+1, HEIGHT+1)
  t.pensize(5)
  t.speed(0)
  t.hideturtle()
  
  # Draw the art
  t.forward(WIDTH)              #draws the initial box
  t.left(90)
  t.forward(HEIGHT)
  t.left(90)
  t.forward(WIDTH)
  t.left(90)
  t.forward(HEIGHT)
  t.left(90)
  mondrian(0, 0, 1024, 768, t)
##  split_region(1024, 768)
  wn.exitonclick()

if __name__ == '__main__':
  main()
