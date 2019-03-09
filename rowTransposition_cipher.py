# CPSC 452 HW1 - Row Transposition Cipher
# Authors: Jake Cliff, Kenny Chao, and Scott Ng
import sys
import cipherCheck
import math

def enc_rowTransposition(message, key): 
    rows = math.ceil(len(message)/len(key))
    columns = len(key)
    # Calculate number of characters to fill matrix
    totalChars = rows * columns

    voidLetter = 'X'
    matrix = []

    # Firgure out the number of chars need to fill null spaces
    charsToFIll = 0
    if (len(message) < totalChars):
        charsToFIll = totalChars - len(message)
    
    j = 0
    for i in range(charsToFIll):
        message = message + voidLetter
    print(message)

    for i in range(rows):
        matrix.append([])

    r = 0
    c = 0
    for j in range(totalChars):
        if (c < columns):
            matrix[r].append(message[j])
            c = c + 1
        else:
            c = 0
            r = r + 1
            matrix[r].append(message[j])
            c = c + 1
    
    eTxt = ""

    for i in range(len(key)):
        columnIndex = int(key[i])-1
        for row in matrix:
            eTxt = eTxt + row[columnIndex]
        i = i + 1

    print("Encrypted Text: " + eTxt)

    return eTxt

def dec_rowTransposition(message, key):
    rows = math.ceil(len(message)/len(key))
    columns = len(key)

    # Matrix creation
    matrix = []
    for i in range(rows):
        matrix.append([])

    # Fill matrix will 'null' values for future replacement
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

    # Replace spaces with ciphertext
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