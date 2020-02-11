# ----------------------------------------------------------
# --------              HW 8: Part 2               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Name:Alexa Canaan
# Time spent on part 2: 4 hours 
# Collaborators and sources: mike belleville/tutor 
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


def openReadFile(filename):
    '''ask the user for the name of the file of text in which they want to find haikus
    if the user enters the name of a file that does not exist, the program should print the error “File not found” and exit.
    format the file using read(), putting into lower case, stripping punctuation'''
    try:                                        #asks the user for the name of file to find haikus
        myfile = open(filename, 'r+')
    except:                                     #if the file doesn't exist, notify user and exit
        print('File not found')
        return None
    punctuation = '.,!?;:'
    file = myfile.read()
    file1 = file.lower()
    file2 = file1.split()
    for word in range(len(file2)):              #strips words of punctuation
        file2[word] = file2[word].strip('.,!?;:')
    myfile.close()
    return file2

def openWriteFile(readfile, sylDict):
    '''creates an empty haiku file called haikus.txt, writing one haiku per line.
    the haikus are lower case without any punctuation, separated into respective phrases using forward slashes
    reads each word in the given file and adds the word of the text to the haiku.'''
    writefile = open('haikus.txt', 'w')
    syllablecount = 0
    haikucount = 0
    tempstr = ''
    for word in readfile:                                   #iterates over each word in file to start finding haikus
        if word.isdigit() == False and word in sylDict:     #checks the word is not a digit and is a valid word
            if syllablecount < 5:                           #begins on the first line of 5 syllables
                if ((syllablecount + sylDict[word]) <= 5):  #checks that the word doesn't go over syllable count
                    syllablecount += sylDict[word]
                    tempstr += word + ' '
                    if syllablecount == 5:                  #separates the 1st and 2nd line
                        tempstr += '/ '
                elif (syllablecount + sylDict[word]) > 5:   #starts the haiku over if the syllable limit is exceeded
                    syllablecount = 0
                    tempstr = ''
            elif syllablecount >= 5 and syllablecount < 12:#begins on second line of 7 syllables
                if ((syllablecount + sylDict[word]) <= 12):#checks that the word doesn't go over syllable count
                    syllablecount += sylDict[word]
                    tempstr += word + ' '
                    if syllablecount == 12:                 #separates the 2nd and 3rd line
                        tempstr += '/ '
                elif (syllablecount + sylDict[word]) > 12:  #starts the haiku over if the syllable limit is exceeded
                    syllablecount = 0
                    tempstr = ''
            elif syllablecount >= 12 and syllablecount < 17:#begins on third line of 5 syllables
                if ((syllablecount + sylDict[word]) <= 17):#checks that the word doesn't go over syllable count
                    syllablecount += sylDict[word]
                    tempstr += word + ' '
                    if syllablecount == 17:                 #writes the completed haiku to the new file
                        writefile.write(tempstr + '\n')
                        syllablecount = 0
                        haikucount += 1
                        tempstr = ''
                elif (syllablecount + sylDict[word]) > 17:  #starts the haiku over if the syllable limit is exceeded
                    syllablecount = 0
                    tempstr = ''
    writefile.close()
    return haikucount

##                haiku = haikuCreate(5, syllablecount, sylDict[word], word)
##                if haiku[0] != '':
##                    tempstr += haiku[0]
##                if haiku[1] != 0:
##                    syllablecount += haiku[1]
                
##                haiku = haikuCreate(12, syllablecount, sylDict[word], word)
##                if haiku[0] != '':
##                    tempstr += haiku[0]
##                if haiku[1] != 0:
##                    syllablecount += haiku[1]

                
##                haiku = haikuCreate(17, syllablecount, sylDict[word], word)
##                if haiku[0] != '':
##                    tempstr += haiku[0]
##                if haiku[1] != 0:
##                    syllablecount += haiku[1]
                    

##def haikuCreate(n, syllablecount, value, word):
##    tempstr = ''
##    if ((syllablecount + value) <= n):
##        syllablecount += value
##        tempstr += word + ' '
##        if syllablecount == n:
##            tempstr += '/ '
##        elif (syllablecount + value) > n:
##            syllablecount = 0
##            tempstr = ''
##    print(tempstr)
##    print(syllablecount)
##    return (tempstr, syllablecount)

def syllableCounter():
    '''takes a file with all words in the english dictionary and corresponding number of syllables.
    creates a dictionary where the key is the word and the value is the syllable count'''
    myfile = open('hw08_syllables.csv', 'r')
    sylDict = {}
    line = myfile.readline()
    while line != '':                                   #creates a dictionary of valid words with their corresponding syllable count
        line = line.split(',')
        sylDict[line[0]] = int(line[1])
        line = myfile.readline()
    return sylDict
	
##def haikuCount(haikufile, readfile):
##    '''displays the total number of haikus found in the text'''
##    myfile = open(haikufile, 'r')
##    file = myfile.readlines()
##    haikucount = len(file)
##    print('Found', haikucount, 'haikus in', readfile) 

def main():                           
    readfile = input('File in which to find haikus: ')
    mainfile = openReadFile(readfile)
    if mainfile != None:                            #carries on finding haikus if the file exists
        sylDict = syllableCounter()
        haikucount = openWriteFile(mainfile, sylDict)
        if haikucount != 0:                         #if there are haikus, notify the user of how many                                                              
            print('Found', haikucount, 'haikus in', readfile)



main()
