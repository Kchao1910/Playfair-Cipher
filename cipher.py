
import sys
import re

# Check if cipher entered in is included in options
def checkCipherName(x, y):
    if (x != y[0] and x != y[1] and x != y[2] and x != y[3] and x != y[4]):
        print('Invalid cipher name used')
        return
    else:
        print('Your cipher: ' + x)

# Check if user entered in enc or dec
def checkEncDec(z):
    z = z.upper()
    if (z != 'ENC' and z != 'DEC'):
        print('Your option ' + z + ' is invalid. Enter in either "ENC" to encrypt or "DEC" to decrypt!')
    else:
        print('Your enc/dec option: ' + z)

# Check if user entered in file that ends in .txt
def checkFileExtension(a, b):
    txtExtension = re.search(r'\.txt$', a)
    txtExtension2 = re.search(r'\.txt$', b)

    if (txtExtension and txtExtension2):
        print('File extension: .txt')
    elif (not txtExtension and not txtExtension2):
        print('Invalid file extension: ' + a + ' and ' + b + ', must be .txt!')
    elif (not txtExtension):
        print('Invalid input file extension: ' + a)
    else:
        print('Invalid output file extension: ' + b)

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
    

# c = cipherName, d = cipherList, e = key, f = encDec, g = inputFile, h = outputFile
def cipherInterface(c, d, e, f, g, h):
    if (c == d[0]):
        print('Playfair cipher chosen')
        playFairCipher(e, f, g, h)
    elif (c == d[1]):
        print('Row Transpostion cipher chosen')
    elif (c == d[2]):
        print('Railfence cipher chosen')
    elif (c == d[3]):
        print('Vigenre cipher chosen')
    elif (c == d[4]):
        print('Caesar cipher chosen')

def playFairCipher(e, f, g, h):
    e = e.upper()
    alphabet = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    newAlphabet = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'IJ', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    print('Keyword: ' + e)

    if (f.upper() == 'ENC'):
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

    pText = readFile(g)
    print("Input File Contents: " + pText)
    playFairCipherEncrypt(e, pText, h, matrix2D)

def playFairCipherEncrypt(myKeyword, myPlaintext, outputFile, matrix2D):
    keywordPair = []
    i = 0
    j = 0
    myPlaintext = myPlaintext + ' '
    lengthOfKeyword = len(myPlaintext)
    print('The length of my string (+1) is: %d' % lengthOfKeyword)

    while i < lengthOfKeyword-1:
        if (len(myPlaintext) == 2): # For string length of 1
            if (myPlaintext[i] == 'X'):
                keywordPair.insert(j, myPlaintext[i] + 'Y')
            else:
                keywordPair.insert(j, myPlaintext[i] + 'X')
            i = i + 2
        if (len(myPlaintext) == 3): # For string length of 2
            if (myPlaintext[i] == myPlaintext[i+1]):
                if (myPlaintext[i] == 'X'):
                    keywordPair.insert(j, myPlaintext[i] + 'Y')
                    keywordPair.insert(j, myPlaintext[i+1] + 'Y')
                else:
                    keywordPair.insert(j, myPlaintext[i] + 'X')
                    keywordPair.insert(j, myPlaintext[i+1] + 'X')
            else:
                keywordPair.insert(j, myPlaintext[i] + myPlaintext[i+1])
            i = i + 2
        if (lengthOfKeyword >= 4 and lengthOfKeyword % 2 == 0 ): # For string length greater than 3 and also odd
            if (myPlaintext[i] == myPlaintext[i+1]):
                if (myPlaintext[i] == 'X'):
                    keywordPair.insert(j, myPlaintext[i] + 'Y')
                else:
                    keywordPair.insert(j, myPlaintext[i] + 'X')
                i = i + 1
            elif (myPlaintext[i+1] == ' '):
                if (myPlaintext[i] == 'X'):
                    keywordPair.insert(j, myPlaintext[i] + 'Y')
                else:
                    keywordPair.insert(j, myPlaintext[i] + 'X')
                i = i + 1
            else:
                keywordPair.insert(j, myPlaintext[i] + myPlaintext[i+1])
                i = i + 2
        if (lengthOfKeyword >= 5 and lengthOfKeyword % 2 == 1): # For string length greater than 4 and also even
            if (myPlaintext[i] == myPlaintext[i+1]):
                if (myPlaintext[i] == 'X'):
                    keywordPair.insert(j, myPlaintext[i] + 'Y')
                else:
                    keywordPair.insert(j, myPlaintext[i] + 'X')
                i = i + 1
            elif (myPlaintext[i+1] == ' '):
                if (myPlaintext[i] == 'X'):
                    keywordPair.insert(j, myPlaintext[i] + 'Y')
                else:
                    keywordPair.insert(j, myPlaintext[i] + 'X')
                i = i + 1
            else:
                keywordPair.insert(j, myPlaintext[i] + myPlaintext[i+1])
                i = i + 2
                
        j = j + 1
        print('Keyword pairing(s): ', end="")
        print(keywordPair)
    keywordPair = "".join(keywordPair)
    print(keywordPair)
    print(matrix2D)
    encryptionPLF(keywordPair, matrix2D)

def encryptionPLF(keywordPair, matrix2D):
    encryptedText = []

    for i in range(len(keywordPair)):
        for row in matrix2D:
            print(row[0])
            try:
                coord1 = matrix2D.index(row)
                coord2 = row.index(keywordPair[i])
                print("the row number: %s" % matrix2D.index(row))
                print("the column number: %s" % row.index(keywordPair[i]))
                x = coord1
                y = coord2
                word = [x, y]
                encryptedText.insert(i, word)
            except:
                print('r')
    print(encryptedText)

    encString = ''

    j = 0
    for i in range(int(len(encryptedText)/2)):
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
            print('(%d, %d), (%d,%d)' % (x3, y3, x4, y4))
            char1 = matrix2D[x3][y3]
            char2 = matrix2D[x4][y4]
            encString = encString + char1 + char2
        elif (y1 == y2):
            x3 = x1 + 1
            y3 = y1
            x4 = x2 + 1
            y4 = y2
            if (x3 == 5):
                x3 = 0 
            if (x4 == 5):
                x4 = 0
            print('(%d, %d), (%d,%d)' % (x3, y3, x4, y4))
            char1 = matrix2D[x3][y3]
            char2 = matrix2D[x4][y4]
            encString = encString + char1 + char2
        else:
            if (y1 > y2):
                x3 = x2
                y3 = y1
                x4 = x1
                y4 = y2
                if (x1 < x2):
                    print('(%d, %d), (%d,%d)' % (x4, y4, x3, y3))
                    char1 = matrix2D[x4][y4]
                    char2 = matrix2D[x3][y3]
                    encString = encString + char1 + char2
                else:
                    print('(%d, %d), (%d,%d)' % (x3, y3, x4, y4))
                    char1 = matrix2D[x4][y4]
                    char2 = matrix2D[x3][y3]
                    encString = encString + char1 + char2
            else:
                x3 = x1
                y3 = y2
                x4 = x2
                y4 = y1
                print('(%d, %d), (%d,%d)' % (x3, y3, x4, y4))
                char1 = matrix2D[x3][y3]
                char2 = matrix2D[x4][y4]
                encString = encString + char1 + char2
        j = j + 2
    print('Your encrypted text: ' + encString)
    fn = open('output.txt', 'w')
    fn.write(encString)
    fn.close()



        

def rowTranspositionCipher(e, f, g, h):
    print('hi')

def railfenceCipher(e, f, g, h):
    print('hi')

def vigenreCipher(e, f, g, h):
    print('hi')

def caesarCipher(e, f, g, h):
    print('hi')



# start of main()
cipherList = ['PLF', 'RTS', 'RFC', 'VIG', 'CES']


# Remember that the first argument of the script is the file name, thus start at index 1
cipherName = str(sys.argv[1])
key = str(sys.argv[2])
encDec = str(sys.argv[3])
inputFile = str(sys.argv[4])
outputFile = str(sys.argv[5])

argumentList = [cipherName, key, encDec, inputFile, outputFile]
checkCipherName(cipherName, cipherList)
checkEncDec(encDec)
checkFileExtension(inputFile, outputFile)
cipherInterface(cipherName, cipherList, key, encDec, inputFile, outputFile)
