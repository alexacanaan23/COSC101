# ----------------------------------------------------------
# --------              HW 4: Part 2               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 2: 50 minutes
# Collaborators and sources: n/a
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# Write your python program for part 2 below:

##temperature = range(40, -31, -10)
##windspeed = range(5, 45, 5)
def main():
    'Creates a windchill chart that depends on the temperature (in Farenheit) and windspeed (in mph) rounded to the nearest integer'
    '! after windchill below -17 due to frostbite temp'

    temperature = [40, 30, 20, 10, 0, -10, -20, -30] #given temp on the x axis
    windspeed = [5, 10, 15, 20, 25, 30, 35, 40] #given mph on the y axis

    for i in temperature: #creates and formats x axis
        if i == 40: #indents x axis
            print('\t', i, "F", '\t', end='')
        elif i != -30:
            print(i, "F", '\t', end='')
        else:
            print(i, "F")
        
    for x in windspeed: #for each row given the windspeed
            print(x, "mph", '\t', end=' ') #creates y axis
            for i in temperature:
                windchill = (35.74) + (0.6215 * i) - (35.75 * (x ** 0.16)) + ((0.4275 * i) * (x ** 0.16)) #windchill formula
                windchill = round(windchill)
                if windchill < -17:
                    windchill = str(windchill) + "!" #puts ! after windchill where you can get frostbite in 30 minutes or less
                if i == -30:
                    print(windchill)
                else:
                    print(windchill, '\t', end='')
        
main()
