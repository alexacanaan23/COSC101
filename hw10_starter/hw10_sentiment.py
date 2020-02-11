# ----------------------------------------------------------
# --------                 HW 10                   ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on homework: 10 hours
# Collaborators and sources: 
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

import sys 
class Review:
    '''class format used for online reviews'''
    def __init__(self, string, boolean):
        '''indicates whether or not a string contains a review score before review text'''
        self.bool = boolean
        self.string = string
        if self.bool == True:                   #checks if the review contains a score
            self.score = self.string[0]
            self.string = self.string[2:]
        else:
            self.score = None

    def get_score(self):
        '''returns the review's score'''
        return self.score
    
    def get_sentiment(self):
        '''returns the review's sentiment'''
        score = float(self.get_score())
        if score < 2.5:                         #a score of less than 2.5 is negative
            return 'Negative'
        elif score >= 2.5 and score <= 3.5:     #a score between 2.5 and 3.5 inclusive is neutral
            return 'Neutral'
        elif score > 3.5:                       #a score above 3.5 is positive
            return 'Positive'

    def get_words(self):
        '''returns a list of words containing the review text; only digits and letters should be kept
        and the words must be lowercase'''
        reviewlist = []
        currentword = ''
        for idx in range(len(self.string)):     #formates each character
            if self.string[idx] == ' ':         #checks if the character is a space or not
                reviewlist.append(currentword)
                currentword = ''
            elif self.string[idx].isdigit() == True or self.string[idx].isalpha() == True:      #checks if the character is a letter or digit
                currentword += self.string[idx].lower()
        reviewlist.append(currentword)
        return reviewlist

    def compute_and_update_score(self, avg_score_words):
        '''takes a dictionary of words and their sentiment score
        and updates the review's score'''
        sums = 0
        wordcount = 0
        reviewlist = self.get_words()
        for word in reviewlist:                         #looks at each word in the review
            if word in avg_score_words:                 #assigns a score value to the word if it exists
                wordcount += 1
                sums += float(avg_score_words[word])
        self.score = sums / wordcount


    def __str__(self):
        '''allows the object to be converted to a string object'''
        reviewtext = ''
        reviewscore = str(round(float(self.score), 2))
        sentiment = str(self.get_sentiment())
        return reviewscore+ " (" + sentiment + '): '+ self.string

    def compare_sentiment(self, other):
        '''compares the sentiments of two reviews and returns True if they are equal and False if they are not'''
        one = str(self.get_sentiment())
        two = str(other.get_sentiment())
        if one == two:                                  #checks if the sentiments are equal
            return True
        else:
            return False

##----------------------------------------------------------------------------------------                

def train(tuple_list):
    '''takes a list of review objects and returns a dictionary of words and their numeric rating'''
    avg_score_words = {}
    counts = {}
    for review in tuple_list:                       #iterates over each review object
        score = review.get_score()
        words = review.get_words()
        for i in words:                             #formats each review into a dictionary
            if i not in avg_score_words:            #checks if the word exists in the dictionary or not
                avg_score_words[i] = int(score)
                counts[i] = 1
            elif i in avg_score_words:
                avg_score_words[i] += int(score)
                counts[i] += 1
    for k in avg_score_words:                       #creates a new sentiment score for the word
        avg_score_words[k] = (float(avg_score_words[k]) / counts[k])
    return avg_score_words

def read_file_train(filename):
    '''reads the file of provided data and each line/review becomes an item in a list'''
    reviewobjs = []
    myfile = open(filename, 'r')
    for line in myfile:                             #turns each line into a review object
        if line[0].isdigit() == True:               #checks if the review has a human-given score
            a = Review(line, True)
            reviewobjs.append(a)
    myfile.close()
    return reviewobjs       

def write_file_train(filename, trainobjs):
    '''writes the train file using the given dictionary and filename'''
    myfile = open(filename, 'w')
    for item in sorted(trainobjs):                  #writes each key-value pair in dictionary to file
        myfile.write(item+','+ str(trainobjs[item])+'\n')
    myfile.close()

#_____________________________________________________________________________

def open_train_file(filename):
    '''opens a training file where each line is a word and its sentiment score, separated by a comma
    formats it into a dictionary where the word is the key and the sentiment score is the value'''
    traindict = {}
    myfile = open(filename, 'r')
    for line in myfile:                             #formats each line into a key-value pair
        line = line.split(',')
        traindict[line[0]] = line[1].strip('\n')
    myfile.close()
    return traindict

def dictionary_format(reviewwordlist, avg_score_words):
    '''takes a list of reviews and formats them into a dictionary so that
    keys are words and values are the sentiment score for each word'''
    reviewdict = {}
    for word in reviewwordlist:                     #formats each review into a dictionary
        if word in avg_score_words:                 #only accounts for words with an already-determined sentiment score
            reviewdict[word] = avg_score_words[word]
    return reviewdict
            

def main():
    itemload = input('Would you like to (T)rain or (L)oad? ') #T = training data/compute new word scores, L = load a file of previously computed words
    if itemload == "T":
        filename = input('Enter filename: ')
        reviewobjs = read_file_train(filename)
        traindict = train(reviewobjs)
        save_or_nosave = input('Do you want to save the word scores (Y/N)? ')
        if save_or_nosave == 'Y':                   #if the user wants to save the score
            save_train_file = input('Enter filename: ')
            write_file_train(save_train_file, traindict)
    elif itemload == "L":
        filenames = input('Enter training file name: ')
        traindict = open_train_file(filenames)
    analyze = input('Would you like to analyze a (S)ingle review, analyze a (F)ile of reviews, (M)easure the accuracy, or (Q)uit? ')
    if analyze == 'S':                              #single review to be processed
        reviewtext = input('Enter a review: ')
        if reviewtext[0].isdigit() == True:         #checks if a review score is given
            review = Review(reviewtext, True)
        else:
            review = Review(reviewtext, False)
        wordlist = review.get_words()
        reviewvalues = dictionary_format(wordlist, traindict)
        review.compute_and_update_score(reviewvalues)
        print(review)
    elif analyze == 'F':                            #review a file
        analyzeit = input('Enter a filename: ')
        analyzefile = open(analyzeit, 'r')
        for line in analyzefile:                    #iterating over each line in the file
            line = line.strip('\n')
            review = Review(line, False)
            wordlist = review.get_words()
            reviewvalues = dictionary_format(wordlist, traindict)
            review.compute_and_update_score(reviewvalues)
            print(review)
    elif analyze == 'M':                            #measuring the accuracy of the program
        measure = input('Enter a filename: ')
        interobjs = read_file_train(measure) #list of review objects
        computeobjs = train(interobjs)
        realscoreobj = read_file_train(measure)
        totalreviews = 0
        correctreviews = 0
        for review in range(len(interobjs)):        #iterating over each review
            interobjs[review].compute_and_update_score(computeobjs)     
            result = interobjs[review].compare_sentiment(realscoreobj[review])
            if result == True:                      #checks if the sentiments are the same
                correctreviews += 1
                totalreviews += 1
            else:
                totalreviews += 1
        print(correctreviews, 'out of', totalreviews, 'reviews were scored correctly')
    elif analyze == 'Q':                        #Quits
        sys.exit()

def test_review():
    a = Review('1 This product is junk.', True)
    print(Review('1 This product is junk.', True))
##    a.compute_and_update_score({'this': 1.5, 'product': 2.5, 'great' : 5})
##    print(a.get_score())
    return None

if __name__ == '__main__':
  main()
