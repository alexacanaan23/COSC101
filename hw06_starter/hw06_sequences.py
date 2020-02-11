# ----------------------------------------------------------
# --------              HW 6: Part 1               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Name:Alexa Canaan
# Time spent on part 1: 1 hour
# Collaborators and sources: n/a
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

def sequence1(n, count):
    '''Should return a list containing the first count multiples of n'''
    seq = []
    i = 1
    while i < count + 1:
        seq += [i*n]
        i += 1
    return seq

def sequence2(phrase, n):
    '''Should return a string containing the first n vowels in phrase'''
    i = 0
    j = 0
    seq = ''
    while j < n:
        if phrase[i] in 'aeiou':
            seq += phrase[i]
            j += 1
        i += 1
    return seq

def sequence3(data):
    '''Should return a list containing the first item in data repeated once,
    the second item in data repeated twice, the third item in data repeated
    thrice, etc.'''
    seq = []
    i = 0
    while i < len(data):
        j = 0
        while j < i + 1:
            seq += [data[i]]
            j += 1
        i += 1
    return seq

def sequence4(sentence):
    '''Should return a list containing the words in the sentence in the 
    opposite order'''
    seq = []
    i = 0
    while i < len(sentence):
        w = ''
        while i < len(sentence) and sentence[i] != ' ':
            w += sentence[i]
            i += 1
        seq.insert(0, w)
        i += 1
    return seq
    
def main():
    # You may add testcases here to test each function

    #Test 1
    step1 = sequence1(5, 3)
    print(step1)
    if step1 == [5, 10, 15]:
        print('Test 1: Passed')
    else:
        print('Test Failed')

    #Test 2
    step2 = sequence2('ice cream', 3)
    print(step2)
    if step2 == 'iee':
        print('Test 2: Passed')
    else:
        print('Test Failed')

    #Test 3
    step3 = sequence3([4, 5, 6])
    print(step3)
    if step3 == [4, 5, 5, 6, 6, 6]:
        print('Test 3: Passed')
    else:
        print('Test Failed')

    #Test 4
    step4 = sequence4('while loops can be tricky')
    print(step4)
    if step4 == ['tricky','be','can','loops','while']:
        print('Test 4: Passed')
    else:
        print('Test Failed')


if __name__ == '__main__':
    main()
