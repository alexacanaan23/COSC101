# ----------------------------------------------------------
# --------              HW 5: Part 3               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 1: 7 hours
# Collaborators and sources: lab hours
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

# Write your python program for part 3 below:

# This is some starter code.  You will need to modify it.
def reformat_data(data):
    'checks that a given string is in the correct format'
    'if of proper form, returns a list of strings, such that for each distinct name in hte original string, a string exists in the returned list that conains the name, followed by all associated data separated by commas'
    'strings in the list should appear in order of the name values encountered'
    'ex.["apples,5\n", "pears,8,2\n", "oranges,3\n"]'
    'is string is not of proper format, the function returns the original string'
    
    step1 = check_and_list(data)
    if step1 != (True, step1[1]):       #checks if the string is of proper format
        return data      
    step2 = group_data(step1[1])
    step3 = divide_list(step2[1], step2[2])
    step4 = lists_to_expected(step2[0], step3)
    return step4

def check_and_list(data):
    'accepts a given string of data'
    'checks the format of a given string to see if it matches below'
    'name1 data1 name2 data2 name3 data3'
    'there can be any number of pairs of names and data; names do not have to be unique'
    'returns True if format is correct and a list containing each name followed by its associated data point'
    'returns False if format is incorrect and an empty list'

    returnlist = []
    newdata = data.split()
    
    for item in range(1, len(newdata)):                 #checks the format of given string
        if newdata[item].isdigit() == True:             #checks that there are not two consecutive integer objects
            if newdata[item - 1].isdigit() == True:
                return False, returnlist
            
    previousdigit = 0
    for index in range(len(newdata)):                   #for each object in the formatted list
        if newdata[index].isdigit() == True:            #if the index is a digit, concatenate the strings and add them to returnlist, then add the data
            returnlist += [' '.join(newdata[previousdigit:index])]
            returnlist += [newdata[index]]
            previousdigit = index + 1
               
    return True, returnlist

def group_data(data):
    'takes a list of the format [name1, data1, name2, data2, ...]'
    'returns 3 lists'
    '1st list is all the name items with no repeats'
    '2nd list is all the data items in order of the name item they correspond to'
    '3rd list is the count of data items associated with each name'

    namelist = []
    datalist = []
    countofdatalist = []
    
    for index in range(0, len(data) - 1, 2):            #iterate over each name
        if data[index] not in namelist:                 #creates name list, count of data list and data list for unique name
            countofdatalist.append(1)
            namelist.append(data[index])
            datalist.append(data[index + 1])
        else:                                           #formats datalist and countofdatalist for repeat names
            indexlist3 = namelist.index(data[index])
        
##            print(countofdatalist[indexlist3])
            temp = sum([int(x) for x in countofdatalist[:indexlist3 + 1]])
##            print(temp)
            datalist.insert(temp, data[index + 1])
            countofdatalist[indexlist3] += 1
            
            

    return namelist, datalist, countofdatalist

def divide_list(mixlist1, intlist2):
    'takes two lists; 1st is of mixed type and 2nd is a list of integers'
    'divides the item in the first list into separate lists according to the counts of the 2nd list'
    'returns a list of the sublists'

    listofsublists = []
    leftindex = 0
    rightindex = 0
    for index in range(len(intlist2)):                  #creates sublist based on the 1st and 2nd list
        rightindex += intlist2[index]
        listofsublists.append(mixlist1[leftindex:rightindex])
        leftindex = rightindex
    return listofsublists

def lists_to_expected(namelist1, datalist2):
    'takes two lists'
    'merges lists in index order into strings with each item separarted by a comma'
    'every string except for the last should end with the newline character'
    'both lists can be of any non-sequence type'
    'assume lengths of both lists are the same'

    combinedlist = []
    index = 0
    for item in range(len(namelist1)):                  #iterates over namelist and starts newlist
        newstring = namelist1[item] + ','
        for integer in datalist2[item]:                 #iterates over datalist and adds data to names
            newstring += str(integer) + ','
        newstring1 = newstring[:-1]
        if item != (len(namelist1) - 1):                #adds a newline character when appropriate
            newstring1 += '\n'
        combinedlist.append(newstring1)

    return combinedlist
                  
    

