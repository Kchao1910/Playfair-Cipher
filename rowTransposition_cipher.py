import sys
import cipherCheck
import math

def enc_rowTransposition(message, key): 
    rows = math.ceil(len(message)/len(key))
    columns = len(key)
    totalChars = rows * columns

    voidLetter = 'X'
    matrix = []

    charsToFIll = 0
    if (len(message) < totalChars):
        charsToFIll = totalChars - len(message)
    
    j = 0
    for i in range(charsToFIll):
        message = message + voidLetter
    print(message)

    for i in range(rows):
        matrix.append([])

    print(columns)
    print(rows)

    r = 0
    c = 0
    for j in range(totalChars):
        if (c < columns):
            matrix[r].append(message[j])
            c = c + 1
            print(matrix)
        else:
            c = 0
            r = r + 1
            matrix[r].append(message[j])
            c = c + 1
            print(matrix)
    
    encryptedText = ""

    for i in range(len(key)):
        columnIndex = int(key[i])-1
        for row in matrix:
            encryptedText = encryptedText + row[columnIndex]
            print(encryptedText)
        i = i + 1

    print("Encrypted Text: " + encryptedText)

    return encryptedText

def dec_rowTransposition(message, key):
    print(message)
    return message

def rowTransposition_main(key, encDec, inputFile, outputFile):
    message = cipherCheck.readFile(inputFile)

    if (encDec.upper() == 'ENC'):
        encryptedText = enc_rowTransposition(message, key)
        cipherCheck.writeFile(outputFile, encryptedText)
    elif (encDec.upper() == 'DEC'):
        decryptedText = dec_rowTransposition(message, key)
        cipherCheck.writeFile(outputFile, decryptedText)
    else:
        sys.exit(0)