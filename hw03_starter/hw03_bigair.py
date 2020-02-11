# ----------------------------------------------------------
# --------             HW 3: Part 3.2              ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 3.2: 30 minutes
# Collaborators and sources: lab hours
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# Write your python program for part 3.2 below:

#takes the avg score of 6 judges of each run 
def enterscore():
    num1 = float(input("Enter judge 1's score: "))
    num2 = float(input("Enter judge 2's score: "))
    num3 = float(input("Enter judge 3's score: "))
    num4 = float(input("Enter judge 4's score: "))
    num5 = float(input("Enter judge 5's score: "))
    num6 = float(input("Enter judge 6's score: "))

    scores = [num1, num2, num3, num4, num5, num6]
    scores.remove(max(scores))
    scores.remove(min(scores))
    summ = 0
    for i in scores:
        summ += i
    averagescore = summ / 4
    averagescore = round(averagescore, 3)
    print("Competitor's score: ", averagescore)
    return averagescore

#calculates the final qualification round score
def finalscore(x, y):
    finalqualscore = max(x, y)
    finalqualscore = round(finalqualscore, 3)
    print("Competitor's final qualification round score: ", finalqualscore)

#main fn that takes the judges scores from 2 runs
def main():
    print("Run 1")
    score1 = enterscore()
    print(" ")
    print("Run 2")
    score2 = enterscore()
    print(" ")
    final = finalscore(score1, score2)

main()
    
