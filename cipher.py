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

    print(plaintext)
    newPlaintext = ""

    if (len(plaintext) > 1):
        for i in range(len(plaintext)):
            p = ''.join(plaintext[i])
            newPlaintext = newPlaintext + p
    #print(newPlaintext.upper())
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

    if (f == 'ENC'):
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
    print(matrix)
    print(len(matrix))

    row1 = matrix[0:5]
    row2 = matrix[5:10]
    row3 = matrix[10:15]
    row4 = matrix[15:20]
    row5 = matrix[20:25]
    matrix2D = ([row1] + [row2] + [row3] + [row4] + [row5])
    print(matrix2D)
    # [row][column]
    print(matrix2D[1][0])

    pText = readFile(g)
    print(pText)
    playFairCipherEncrypt(e, pText, h)

def playFairCipherEncrypt(myKeyword, myPlaintext, outputFile):
    print('\n' + myKeyword + '\n' + myPlaintext + '\n' + outputFile)
    keywordPair = []
    i = 0
    j = 0
    while i <= len(myKeyword):
        if (len(myKeyword) == 1):
            if (myKeyword[i] == 'X'):
                keywordPair.insert(j, myKeyword[i] + 'Y')
                print(keywordPair)
                i = i + 1
            else:
                keywordPair.insert(j, myKeyword[i] + 'X')
                print(keywordPair)
                i = i + 1 
        else:
            if (myKeyword[i] == myKeyword[i+1]):
                print('Duplicate')
                if (myKeyword[i] == 'X'):
                    keywordPair.insert(j, myKeyword[i] + 'Y')
                    print(keywordPair)
                    i = i + 1
                    if (i == len(myKeyword)-1 and len(myKeyword)%2 == 0):
                        print('break')
                        keywordPair.insert(j, myKeyword[i] + 'X')
                        print(keywordPair)
                        break
                    elif (i == len(myKeyword)-1):
                        print('Double O')
                        keywordPair.insert(j, myKeyword[i] + 'X')
                        print(keywordPair)
                        break
                else:
                    keywordPair.insert(j, myKeyword[i] + 'X')
                    print(keywordPair)
                    i = i + 1
                    if (i == len(myKeyword)-1 and len(myKeyword)%2 == 0):
                        print('break')
                        keywordPair.insert(j, myKeyword[i] + 'X')
                        print(keywordPair)
                        break
                    elif (i == len(myKeyword)-1):
                        print('Double O')
                        keywordPair.insert(j, myKeyword[i] + 'X')
                        print(keywordPair)
                        break

            else:
                print('Yarghhh')
                if (myKeyword[i+1] == ''):
                    if (myKeyword[i] == 'X'):
                        keywordPair.insert(j, myKeyword[i] + 'Y')
                        print(keywordPair)
                    else:
                        keywordPair.insert(j, myKeyword[i] + 'X')
                        print(keywordPair)
                else:
                    if (i == len(myKeyword)-3 and len(myKeyword)%2 == 1):
                        keywordPair.insert(j, myKeyword[i] + myKeyword[i+1])
                        print(keywordPair)
                        i = i + 1
                        print('I am here JKLDJSLF')
                    elif (i == len(myKeyword)-2 and len(myKeyword)%2 == 1):
                        print('I am here ODD 1')
                        i = i + 1
                        print(myKeyword[i])
                        if (myKeyword[i-1] == myKeyword[i-2]):
                            keywordPair.insert(j, myKeyword[i-1] + myKeyword[i])
                        elif (myKeyword[i-1] != myKeyword[i]):
                            keywordPair.insert(j, myKeyword[i-1] + myKeyword[i])
                        elif (myKeyword[i-1] == myKeyword[i]):
                            keywordPair.insert(j, myKeyword[i-1] + 'TA')
                        else:
                            if (myKeyword[i] == 'X'):
                                keywordPair.insert(j, myKeyword[i] + 'Y')
                            else:
                                keywordPair.insert(j, myKeyword[i] + 'X')
                        print(keywordPair)
                        i = i + 1
                    elif (i == len(myKeyword)-2 and len(myKeyword)%2 == 0):
                        print('Even 2')
                        if (myKeyword[i] == 'X'):
                            keywordPair.insert(j, myKeyword[i] + myKeyword[i+1])
                        else:
                            keywordPair.insert(j, myKeyword[i] + myKeyword[i+1])
                        print(keywordPair)
                        print('I am here now')
                        i = i + 2
                    elif (i == len(myKeyword)-3 and len(myKeyword)%2 == 0):
                        print('Even 1')
                        keywordPair.insert(j, myKeyword[i] + myKeyword[i+1])
                        print(keywordPair)
                        i = i + 1
                    else: 
                        print('That else statement')
                        keywordPair.insert(j, myKeyword[i] + myKeyword[i+1])
                        print(keywordPair)
                        i = i + 2



        
    
            
        j = j + 1
        print(len(myKeyword))
        print(i)
        if (i == len(myKeyword)):
            i = i + 1
        print(i)




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
