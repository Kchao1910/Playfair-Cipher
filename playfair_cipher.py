import sys
import re
from collections import OrderedDict

def readFile(g):
    f = open(g, "r")
    data = f.readlines()
    plaintext = []

    for line in data:
        words = line.split()
        plaintext.append(words)

    newPlaintext = ""

    if (len(plaintext) >= 1):
        for i in range(len(plaintext)):
            p = ''.join(plaintext[i])
            newPlaintext = newPlaintext + p
    return newPlaintext.upper()
        
def playFairCipher(e, f, g, h):
    e = e.upper()
    alphabet = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    newAlphabet = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'IJ', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    print('Keyword: ' + e)

    for i in range(len(e)):
        for j in range(len(alphabet)):
            if (e[i] == alphabet[j]):
                if (e[i] == 'I' or e[i] == 'J'):
                    print('Removing: ' + alphabet[j])
                    try:
                        newAlphabet.remove('IJ')
                    except: 
                        print('Already removed!')
                else:
                    print('Removing: ' + alphabet[j])
                    try:
                        newAlphabet.remove(e[i])
                    except:
                        print('Already removed!')
                break
        j = 0
    e = "".join(OrderedDict.fromkeys(e))
    keywordList = list(map(str, str(e)))
    print('New alphabet: ' + str(newAlphabet))

    # creating new matrix
    matrix = keywordList + newAlphabet
    print('Whole matrix: ' + str(matrix))

    row1 = matrix[0:5]
    row2 = matrix[5:10]
    row3 = matrix[10:15]
    row4 = matrix[15:20]
    row5 = matrix[20:25]
    matrix2D = ([row1] + [row2] + [row3] + [row4] + [row5])
    print('5x5 matrix: ' + str(matrix2D))
    # [row][column]

    if (f.upper() == 'ENC'):
        pText = readFile(g)
        if (len(pText) == 0):
            print("Error: File contains nothing to encrypt!")
            sys.exit(0)
        print("Input File Contents: " + pText)
        playFairCipherEncrypt(e, pText, h, matrix2D)
    elif (f.upper() == 'DEC'):
        decryptionPLF(g, h, matrix2D)
    else:
        print('Error: ENC/DEC was not chosen!')


def insertXY(myPlaintext, keywordPair, j, i):
    if (myPlaintext[i] == 'X'):
        keywordPair.insert(j, myPlaintext[i] + 'Y')
    else:
        keywordPair.insert(j, myPlaintext[i] + 'X')

def insertXY2(myPlaintext, keywordPair, j, i):
    if (myPlaintext[i] == 'X'):
        keywordPair.insert(j, myPlaintext[i] + 'Y')
        keywordPair.insert(j, myPlaintext[i+1] + 'Y')
    else:
        keywordPair.insert(j, myPlaintext[i] + 'X')
        keywordPair.insert(j, myPlaintext[i+1] + 'X')



def playFairCipherEncrypt(myKeyword, myPlaintext, outputFile, matrix2D):
    keywordPair = []
    i = 0
    j = 0
    myPlaintext = myPlaintext + ' '
    lengthOfKeyword = len(myPlaintext)
    #print('The length of my string (+1) is: %d' % lengthOfKeyword)

    while i < lengthOfKeyword-1:
        if (len(myPlaintext) == 2): # For string length of 1
            insertXY(myPlaintext, keywordPair, j, i)
            i = i + 2
        if (len(myPlaintext) == 3): # For string length of 2
            if (myPlaintext[i] == myPlaintext[i+1]):
                insertXY2(myPlaintext, keywordPair, j, i)
            else:
                keywordPair.insert(j, myPlaintext[i] + myPlaintext[i+1])
            i = i + 2
        if (lengthOfKeyword >= 4): # For string length greater than 3 and also odd
            if (myPlaintext[i] == myPlaintext[i+1]):
                insertXY(myPlaintext, keywordPair, j, i)
                i = i + 1
            elif (myPlaintext[i+1] == ' '):
                insertXY(myPlaintext, keywordPair, j, i)
                i = i + 1
            else:
                keywordPair.insert(j, myPlaintext[i] + myPlaintext[i+1])
                i = i + 2    
        j = j + 1
        #print('Keyword pairing(s): ', end="")
        print(keywordPair)

    keywordPair = "".join(keywordPair)
    #print(keywordPair)
    #print(matrix2D)
    encryptionPLF(keywordPair, matrix2D, outputFile)
   

def findCoordinates(matrix2D, row, encryptedText, iOrJ, keywordPair, i):
    coord1 = matrix2D.index(row)
    if (iOrJ == True):
        coord2 = row.index('IJ')
    else:
        coord2 = row.index(keywordPair[i])
    x = coord1
    y = coord2
    word = [x, y]
    encryptedText.insert(i, word)

def findCoordinateValues(x3, y3, x4, y4, matrix2D, encString, y1GreaterThanY2):
    if (y1GreaterThanY2 == True):
        char1 = matrix2D[x4][y4]
        char2 = matrix2D[x3][y3]
    else:
        char1 = matrix2D[x3][y3]
        char2 = matrix2D[x4][y4]
    encString = encString + char1 + char2
    return encString


def encryptionPLF(keywordPair, matrix2D, outputFile):
    encryptedText = []

    for i in range(len(keywordPair)):
        for row in matrix2D:
            try:
                if (keywordPair[i] == 'I' or keywordPair[i] == 'J'):
                    findCoordinates(matrix2D, row, encryptedText, True, keywordPair, i)
                else:
                    findCoordinates(matrix2D, row, encryptedText, False, keywordPair, i)
            except:
                print("",end="")

    print(encryptedText)

    encString = ''

    j = 0
    lengthOfEncryptedText = len(encryptedText)
    for i in range(int(lengthOfEncryptedText/2)):
        index = encryptedText[j]
        index2 = encryptedText[j+1]
        x1 = index[0]
        y1 = index[1]
        x2 = index2[0]
        y2 = index2[1]

        if (x1 == x2):
            x3 = x1
            y3 = y1 + 1
            x4 = x2
            y4 = y2 + 1
            if (y3 == 5):
                y3 = 0
            if (y4 == 5):
                y4 = 0
            #print('(%d, %d), (%d,%d)' % (x3, y3, x4, y4))
            encString = findCoordinateValues(x3, y3, x4, y4, matrix2D, encString, False)
        elif (y1 == y2):
            x3 = x1 + 1
            y3 = y1
            x4 = x2 + 1
            y4 = y2
            if (x3 == 5):
                x3 = 0 
            if (x4 == 5):
                x4 = 0
            #print('(%d, %d), (%d,%d)' % (x3, y3, x4, y4))
            encString = findCoordinateValues(x3, y3, x4, y4, matrix2D, encString, False)
        else:
            if (y1 > y2):
                x3 = x2
                y3 = y1
                x4 = x1
                y4 = y2
                if (x1 < x2):
                    #print('(%d, %d), (%d,%d)' % (x4, y4, x3, y3))
                    encString = findCoordinateValues(x3, y3, x4, y4, matrix2D, encString, True)
                else:
                    #print('(%d, %d), (%d,%d)' % (x3, y3, x4, y4))
                    encString = findCoordinateValues(x3, y3, x4, y4, matrix2D, encString, True)
            else:
                x3 = x1
                y3 = y2
                x4 = x2
                y4 = y1
                #print('(%d, %d), (%d,%d)' % (x3, y3, x4, y4))
                encString = findCoordinateValues(x3, y3, x4, y4, matrix2D, encString, False)
        j = j + 2
    print('Your encrypted text: ' + encString)
    fn = open(outputFile, 'w')
    fn.write(encString)
    fn.close()

def findDecryptionValues(x3, y3, x4, y4, decTxt, matrix2D):
    char1 = matrix2D[x3][y3]
    char2 = matrix2D[x4][y4]
    decTxt = decTxt + char1 + char2
    return decTxt


def decryptionPLF(inputFile, outputFile, matrix2D):
    dTxt = readFile(inputFile)
    if (len(dTxt) == 0):
        print("Error: File contains nothing to decrypt!")
        sys.exit(0)
    print("Input File Contents: " + dTxt)
    print(matrix2D)

    decryptedTxt = []

    for i in range(len(dTxt)):
        for row in matrix2D:
            try:
                coord1 = matrix2D.index(row)
                coord2 = row.index(dTxt[i])
                #print("the row number: %s" % matrix2D.index(row))
                #print("the column number: %s" % row.index(dTxt[i]))
                x = coord1
                y = coord2
                word = [x, y]
                decryptedTxt.insert(i, word)
            except:
                print('', end='')
    print(decryptedTxt)

    decTxt = ""
    j = 0
    for i in range(int(len(decryptedTxt)/2)):
        index1 = decryptedTxt[j]
        index2 = decryptedTxt[j+1]
        x1 = index1[0]
        y1 = index1[1]
        x2 = index2[0]
        y2 = index2[1]

        if (x1 == x2):
            x3 = x1
            y3 = y1 - 1
            x4 = x2
            y4 = y2 - 1
            if (y3 == -1):
                y3 == 4
            if (y4 == -1):
                y4 == 4
            decTxt = findDecryptionValues(x3, y3, x4, y4, decTxt, matrix2D) 
        elif (y1 == y2):
            x3 = x1 - 1
            y3 = y1
            x4 = x2 - 1
            y4 = y2
            if (x3 == -1):
                x3 = 4
            if (x4 == -1):
                x4 = 4
            #print("%d%d%d%d" % (x3,y3,x4,y4))
            decTxt = findDecryptionValues(x3, y3, x4, y4, decTxt, matrix2D) 
        else: 
            x3 = x1
            y3 = y2
            x4 = x2
            y4 = y1
            decTxt = findDecryptionValues(x3, y3, x4, y4, decTxt, matrix2D) 
              
        j = j + 2
    
    oddIndex = []

    m = 1
    for k in range(int(len(decTxt)/2)):
        oddLetter = decTxt[m]
        oddIndex.append(oddLetter)
        m = m + 2
    
    x = 0
    y = 0
    newDecTxt = []
    newDecTxt2 = []

    for q in range(len(decTxt)):
        newDecTxt2.append(decTxt[q])

    for a in range(int(len(decTxt)/2)-1):
        letter1 = decTxt[x]
        letter2 = decTxt[x+1]
        letter3 = decTxt[x+2]
        if (letter1 == letter3):
            if (letter2 == 'X' or letter2 == 'Y'):
                letter2 = x+1
                newDecTxt.append(letter2)
        x = x + 2

    for t in range(len(newDecTxt)):
        newDecTxt2[newDecTxt[t]] = ""

    newDecTxt2 = "".join(newDecTxt2)
    print("Your decrypted text: " + newDecTxt2)
    fn = open(outputFile, 'w')
    fn.write(newDecTxt2)
    fn.close()

