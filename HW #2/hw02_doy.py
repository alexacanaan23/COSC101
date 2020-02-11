# ----------------------------------------------------------
# --------             HW 2: Part 3.2              ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 3.2: 1.5 hours
# Collaborators and sources: https://asd.gsfc.nasa.gov/Craig.Markwardt/doy2017.html
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# Write your python program for part 3.2 below:

#January day 1-31
#February day 32-59
#March day 60-90
#April day 91-120
#May day 121-151
#June day 152-181
#July day 182-212
#August day 213-243
#September day 244-273
#October day 274-304
#November day 305-334
#December day 335-365

DOY = int(input("Enter the day of the year: "))
if DOY <= 0:
    print("Enter a positive integer")

elif DOY > 0 and DOY < 32:
    print('Day', DOY, 'is January', DOY)

elif DOY >= 32 and DOY <= 59:
    print('Day', DOY, 'is February', (DOY - 31))

elif DOY >= 60 and DOY <= 90:
    print('Day', DOY, 'is March', (DOY - 59))
    
elif DOY >= 91 and DOY <= 120:
    print('Day', DOY, 'is April', (DOY - 90))
    
elif DOY >= 121 and DOY <= 151:
    print('Day', DOY, 'is May', (DOY - 120))
    
elif DOY >= 152 and DOY <= 181:
    print('Day', DOY, 'is June', (DOY - 151))
    
elif DOY >= 182 and DOY <= 212:
    print('Day', DOY, 'is July', (DOY - 181))
    
elif DOY >= 213 and DOY <= 243:
    print('Day', DOY, 'is August', (DOY - 212))
    
elif DOY >= 244 and DOY <= 273:
    print('Day', DOY, 'is September', (DOY - 243))
    
elif DOY >= 274 and DOY <= 304:
    print('Day', DOY, 'is October', (DOY - 273))
    
elif DOY >= 305 and DOY <= 334:
    print('Day', DOY, 'is November', (DOY - 304))
    
elif DOY >= 335 and DOY <= 365:
    print('Day', DOY, 'is February', (DOY - 334))


elif DOY > 365:
    print("There are only 365 days in a year")
