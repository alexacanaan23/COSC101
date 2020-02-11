# ----------------------------------------------------------
# --------              HW 7: Part 1               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 1: 7 hours
# Collaborators and sources: lab hours
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

def read_data(filename):
    '''takes a string specifying a filename
    returns a list of the lines in the file'''
    myfile = open(filename, 'r')
    line = myfile.readline()
    linelist = []
    while line != '':                               #iterating over each line in the file, making each line a string item in a list
        linelist.append(line)
        line = myfile.readline()
    myfile.close()
    return linelist

def parse_data(listoflines):
    '''takes the list of the lines from the file
    returns a list of sublists containing each of the six values contained in a line
    the types of each of the items in the sublist should be converted to the correct type'''

    mainlist = listoflines[:]
    newlist = []
    templist = []
    tempstring = ''
    punctuation = '"$\n'

    tstring2 = ''

    for item in mainlist:                           #for each 'line' in the list of lines
        index = 0
        while index < len(item):                    #iterating over each string line
            if item[index] != '"' and item[index] != ',':           #if the index neither " nor , add it to the tempstring
                tempstring += item[index]
            if item[index] == '"':                                  #if the index is a "
                index += 1
                while index < len(item) and item[index] != '"':     #grab the name or number from between the "
                    tempstring += item[index]
                    index += 1
            elif item[index] == ',':                #if the item is a comma, this is the end of a string
                templist.append(tempstring)
                tempstring = ''
            index+=1
        templist.append(tempstring)
        tempstring = ''
        newlist.append(templist)
        templist = []


    for idx in range(1, len(newlist)):              #iterating over each sublist in the mainlist      
        for index in range(1, len(newlist[idx])):   #iterating over each item in the sublist in the mainlist, strip punctuation
            newlist[idx][index] = newlist[idx][index].strip(punctuation)
            if index == 3:                          #if the index on the salary, make it a number
                newlist[idx][index] = newlist[idx][index].replace(',','')
                newlist[idx][index] = int(newlist[idx][index])
                
    newlist[0][5] = newlist[0][5].strip(punctuation)
    return newlist
       
def analyze_salary_data(dataformatted, intervalsize):
    '''takes the data and an interval size
    divides the salary range of the data into categries of interval size.
    the function then calculates the number of individual salaries in reach range
    and returns the list of maximum salary in each range and the list of counts in each range'''

    maxx = 0
    for sublist in range(1, len(dataformatted)):    #iterating over each sublist
        if dataformatted[sublist][3] > maxx:        #find max salary
            maxx = dataformatted[sublist][3]
    intervallist = []
    interval = intervalsize - 1
    while interval <= maxx:                         #creating interval list
        intervallist.append(interval)
        interval += intervalsize
    intervallist.append(interval)
    numineachrange = []
    for num in range(len(intervallist)):            #setting up list of counts in each range
        numineachrange.append(0)

    
    for index in range(1, len(dataformatted)):      #iterating over every salary, checking which interval it falls under      
        for item in range(len(intervallist)):
            if dataformatted[index][3] <= intervallist[item]:       #updating the list of counts in each range
                numineachrange[item] += 1
                break

    return (intervallist, numineachrange)
    
    
##    mininterval = intervalsize - 1
##    interval2 = mininterval + intervalsize
##    interval3 = interval2 + intervalsize
##    intlist = [mininterval, interval2, interval3]
##    numineachrange = []
##    minn = 0
##    midd = 0
##    top = 0
##    for index in range(1, len(dataformatted)):      #iterating over each salary
##        if int(dataformatted[index][3]) <= mininterval:     #if the salary is between 0 and the minimum
##            minn += 1
##        elif int(dataformatted[index][3]) > mininterval and int(dataformatted[index][3]) <= interval2:  #or if the salary is in the middle
##            midd += 1
##        elif int(dataformatted[index][3]) > interval2 and int(dataformatted[index][3]) <= interval3:    #or of the salary is on the high end
##            top += 1
##    numineachrange.append(minn)
##    numineachrange.append(midd)
##    numineachrange.append(top)
##
##    return(intlist, numineachrange)

def display_data(intlist, numineachrange):
    '''print out a small table titled "Salary Range Data"
    print out two neatly arranged rows
    the top row should be the ranges and the bottom row should be the counts
    takes the intlist and numineachrange list from the previous function'''
    print('')
    print('\t\tSalary Range Data')
    print('')
    interval = intlist[0] + 1
    rangelist = []
    for i in range(len(intlist)):                   #setting up the items for rangelist
        rangelist.append('')
    for spot in range(len(rangelist)):              #creating range strings in the list
        if spot == 0:                               #the first interval starts with 0-interval
            rangelist[0] = str(0)+'-'+str(intlist[0])
        else:                                       #all other intervals are formatted as normal
            rangelist[spot] = str(intlist[spot] - interval + 1)+'-'+str(intlist[spot])
    print('Range\t\t', end='')
    for item in rangelist:                          #prints out row items for range row
        print(str(item)+'\t', end='')
    print('')
    print('Count\t\t', end='')
    for items in numineachrange:                    #prints out row items for count row
        print(str(items)+'\t\t', end='')
        
##    rangelist1 = [str(str(0)+'-'+str(intlist[0])), str(str(intlist[0] + 1)+'-'+str(intlist[1])), str(str(intlist[1] + 1)+'-'+str(intlist[2]))]

    return rangelist
          
def save_results(filename, rangelist, distriblist):
    '''ask the user if they would like to save the results to a file.
    takes the original filename, the list of ranges, and the list of counts as arguments.
    the function modifies the filename so that _results is inserted into the new filname before the file extention
    save the data in a file with the new filename'''
    
    rangelist = rangelist
    distriblist = distriblist
    if '.' in filename:         #adds '_results.' to the new file name
        newname = filename.replace('.', '_results.')
    print('')
    resultant = input('Would you like to save the results to a file? (y)es or (n)o: ')
    if resultant == 'y':        #if the user wants to save results to a file, call the function write_new_file
        writtennewfile = write_new_file(newname, rangelist, distriblist)
        return True         
    else:                       #if the user doesn't want to save results to a file, return False
        return False

##    newname = ''
##    filename1 = filename.split()
##    for i in range(len(filename1)):
##        print(newname)
##        if filename1[i] == '.':
##            newname += '_results.'
##        else:
##            newname += str(filename1[i])
                           
def write_new_file(newfilename, rangelist, distriblist):
    '''writes the formatted data into a new file'''
    myfile = open(newfilename, 'w')
    for idx in range(len(rangelist)):           #iterating over indexes of both list to write into the new file
        part1 = rangelist[idx]
        part2 = distriblist[idx]
        myfile.write(str(part1)+','+str(part2)+'\n')
    myfile.close()
    
                           
def main():
    '''after the save file interaction the program asks the user whether they want to analyze another dat set
    if so, the program begins again.
    else, the program lets the user know the program is finished'''
    bools = True
    while bools != False:       #continues while the user wants the process to do so
        filename = str(input('Enter the name of the file you wish to analyze: '))
        linelist = read_data(filename)
        dataformatted = parse_data(linelist)
        intervalsize = int(input('Enter the salary granularity: '))
        listofmaxsalary = analyze_salary_data(dataformatted, intervalsize)
        rangelist = display_data(listofmaxsalary[0], listofmaxsalary[1])
        save = save_results(filename, rangelist, listofmaxsalary[1])
        if save == True:        #gives result of saving the file
            print('Success! File Saved.')
        else:
            print('Failed to Save File.')
        results = input('Would you like to analyze another file? (y)es or (n)o: ')
        if results == 'y':      #if user wants to analyze another file, the loop continues, otherwise it ends
            bools = True
        elif results == 'n':
            bools = False
    if bools == False:          #at the end of the program, the program says goodbye
        print('Goodbye!')


main()
