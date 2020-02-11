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
    print(seq)


sequence4('while loops can be tricky')
