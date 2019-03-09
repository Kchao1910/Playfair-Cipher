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
    
    eTxt = ""

    for i in range(len(key)):
        columnIndex = int(key[i])-1
        for row in matrix:
            eTxt = eTxt + row[columnIndex]
            print(eTxt)
        i = i + 1

    print("Encrypted Text: " + eTxt)

    return eTxt

def dec_rowTransposition(message, key):
    rows = math.ceil(len(message)/len(key))
    columns = len(key)

    matrix = []
    for i in range(rows):
        matrix.append([])

    r = 0
    c = 0
    for j in range(len(message)):
        if (c < columns):
            matrix[r].append("")
            c = c + 1
        else:
            c = 0
            r = r + 1
            matrix[r].append("")
            c = c + 1

    j = 0
    for i in range(len(key)):
        columnIndex = int(key[i])-1
        for row in matrix:
            row[columnIndex] = message[j]
            j = j + 1
        i = i + 1
    
    print(matrix)
    
    dTxt = ""

    for row in matrix:
        decrypted = "".join(row)
        dTxt = dTxt + decrypted

    print("Decrypted Text: " + dTxt)

    return dTxt
    

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