# ----------------------------------------------------------
# --------              HW 4: Part 1               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 1: 1 hour 10 minutes
# Collaborators and sources: n/a
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# Write your python program for part 1 below:

def check_url(string):
    "Check if a given string is a valid URL"
    'Check if given string contains only lower-case letters and digits before and after the period'
    'Returns boolean True if string meets all conditions, Returns boolean False if it doesnt'
    'ex. http://1.2.3 returns false; https://google.com returns True'
    begin1 = 'http://'                  
    begin2 = 'https://'
    validchs = 'abcdefghijklmnopqrstuvwxyz0123456789.'
    error = 0
    if begin1 in string:                #if http:// is in the string, a valid beginning
        value = check_domain_name(string)
        if value == True:
            if begin1 == string[0:7]:   #if http:// is in the beginning
                for ch in string[7:]:   #all chs after must be valid characters
                    if ch not in validchs:  #tallying invalid chs
                        error += 1
                if error == 0:          #if there are no invalid chs
                    return True
                else:                   #if there's atleast one invalid ch
                    return False
        else:
            return False
    elif begin2 in string:              #if https:// is in the string, a valid beginning
        value = check_domain_name(string)
        if value == True:   
            if begin2 == string[0:8]:   #if https:// is in the beginning
                for ch in string[8:]:   #all chs after must be valid chs
                    if ch not in validchs:  #tallying invalid chs
                        error += 1
                if error == 0:          #if there are no invalid chs
                    return True
                else:                   #if there's atleast one invalid ch
                    return False
        else:
            return False
                
    else:                               #if https:// and  http:// aren't in the string, it's not a URL
        return False

def check_domain_name(string):
    "Check if a given string is a valid domain name"
    'Check if given string contains exactly one period'
    'Check if given string contains at least one character before the period and at least one character after the period'
    'Returns boolean True if it meets the above two conditions, else returns boolean False'
    'ex. https://google.com returns True, http://1.2.3 returns False'
    periodcount = 0                     #must contain exactly 1 period to be valid
    periodindex = 0                     #index of where period occurs
    validchs = 'abcdefghijklmnopqrstuvwxyz0123456789.' #chs in a valid domain
    for index in range(len(string)):    #checking each ch in a list
        if '.' == string[index]:        #identify the number of times a period occurs, and if only once at what index
            periodcount += 1            #tally number of occurrences of a period
            periodindex += index
    if periodcount == 1:                #if there's exactly one period in the string
        if string[periodindex - 1] in validchs: #if the ch before it is a valid ch
            if string[periodindex + 1] in validchs:     #if the ch after it is a valid ch
                return True
    else:
        return False
    

def main():
    'Checks whether a given string is a valid URL'
    'Returns string indicating validity'
    'ex. https://google.com returns "Valid URL"'
    possibleURL = input("Enter a URL: ")        #get URL
    check = check_url(possibleURL)              #enter check_url
    if check == False:                          #if the string fails check_url it's invalid
        print("Invalid URL")
    else:
        print("Valid URL")

main()
