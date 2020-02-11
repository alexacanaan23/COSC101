# ----------------------------------------------------------
# --------             HW 3: Part 3.3              ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 3.3: 2 hours
# Collaborators and sources: open lab hours
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# Write your python program for part 3.3 below:

import time
import random

def instructions():
    print("Test Your Reflexes")
    print(" ")
    print("Instructions: You will be promted to press Enter several times, do so as quickly as you can.")
    print(" ")
    print(input("Press Enter when ready to begin."))

def trial():
    

    delay = random.randrange(1,5)
    time.sleep(delay)
    
    start = time.time()
    input("Press Enter when you see this prompt!")
    end = time.time()
    length = round((end - start), 2)
    return length
 

def avgreflextime(a):
    summ = 0
    for num in a:
        summ += num
    avg = summ / len(a)
    avg = round(avg, 2)
    print(" ")
    print("Your average reflex time was: ", avg, "s")

def main():
    a = instructions()
    L = []
    for i in range(1,4):
        L.append(trial())
        print("Your reflex time for trial", i, "was: "+str(L[i-1])+" s")
        print(" ")       
    end = avgreflextime(L)
    
        

main()
