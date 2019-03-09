# CPSC 452 HW1 - Railfence Cipher
# Authors: Jake Cliff, Kenny Chao, and Scott Ng
import sys
import cipherCheck
import math

def enc_railfence(message, key):
    key = int(key)

    # Creating matrix
    railMatrix = []
    for i in range(key):
        railMatrix.append([])

    k = 0

    # Placing plaintext into matrix
    for j in range(len(message)):
        if (k < key):
            railMatrix[k].append(message[j])
            k = k + 1
        else:
            k = 0
            railMatrix[k].append(message[j])
            k = k + 1

    print(railMatrix) 

    eTxt = ""

    for m in range(len(railMatrix)):
        railList = ''.join(map(str,railMatrix[m]))
        eTxt = eTxt + railList

    print("Encrypted Text: " + eTxt)

    return eTxt

def dec_railfence(message, key):
    key = int(key)
    print("Cipher Text: " + message)
    railMatrix = []
    for i in range(key):
        railMatrix.append([])

    elementsPerRow = int(len(message)/key)
    additionalElements = len(message)%key

    elementNumberList = []

    # This calculates how many elements per row before considering remainder
    i = 0
    for j in range(0, key):
        elementNumberList.append(elementsPerRow)
    
    # This takes care of the remainder
    k = 0
    for l in range(0, additionalElements):
        elementNumberList[k] = int(elementNumberList[k]) + 1
        k = k + 1
    
    m = 0
    o = 0
    p = 0
    # Put ciphertext into matrix
    for n in range(len(message)):
        if (m < int(elementNumberList[o])):
            railMatrix[p].append(message[n])
            m = m + 1
        else:
            m = 0
            o = o + 1
            p = p + 1
            railMatrix[p].append(message[n])
            m = m + 1

    #Deterimne number of columns
    columns = len(message)/key

    if (columns != math.ceil(columns)):
        columns = math.floor(columns + 1)

    dTxt = ""
    c = 0
    k = 0
    for m in range(len(message)):
        if (k < key):
            dTxt = dTxt + railMatrix[k][c]
            k = k + 1
        else:
            k = 0
            c = c + 1
            dTxt = dTxt + railMatrix[k][c]
            k = k + 1

    print("Decrypted Text: " + dTxt)

    return dTxt
    


def railfence_main(key, encDec, inputFile, outputFile):
    message = cipherCheck.readFile(inputFile)

    if (encDec.upper() == 'ENC'):
        encryptedText = enc_railfence(message, key)
        cipherCheck.writeFile(outputFile, encryptedText)
    elif (encDec.upper() == 'DEC'):
        decryptedText = dec_railfence(message, key)
        cipherCheck.writeFile(outputFile, decryptedText)
    else:
        sys.exit(0)


    
    