import sys
import cipherCheck


def enc_vigenere(message,key):
    #Vigenere Cipher
    #Letters are incremented by codeWord A + C = 1 + 3 = D

    newMessage = [message[i] for i in range(0,len(message))]
    codeMessage = [key[i] for i in range(0,len(key))]
    encrypted = []
    c = 0

    for i in range(0, len(newMessage)):
        #if the letter is upper continue
        if message[i].isupper():
            encrypted.append(chr(((ord(message[i])
                                   + ord(key[c%len(codeMessage)].upper())
                                   - 130) % 26)+ 65))
            c += 1
        #assuming its lower since not upper
        elif message[i].islower():
            encrypted.append(chr(((ord(message[i])
                                   + ord(key[c%len(codeMessage)].lower())
                                   - 194) % 26)+ 97))
            c += 1
        else:
            encrypted.append(" ")

    encrypted = ''.join(map(str,encrypted))

    return encrypted

def dec_vigenere(message, key):
    newMessage = [message[i] for i in range(0,len(message))]
    codeMessage = [key[i] for i in range(0,len(key))]
    decrypted = []
    c = 0

    for i in range(0, len(newMessage)):
        #if the letter is upper continue
        if message[i].isupper():
            decrypted.append(chr(((ord(message[i])
                                   - ord(key[c%len(codeMessage)].upper())
                                   - 130) % 26)+ 65))
            c += 1
        #assuming its lower since not upper
        elif message[i].islower():
            decrypted.append(chr(((ord(message[i])
                                   - ord(key[c%len(codeMessage)].lower())
                                   - 194) % 26)+ 97))
            c += 1
        else:
            decrypted.append(" ")

    decrypted = ''.join(map(str,decrypted))

    return decrypted


def vigenere_main(key, encDec, inputFile, outputFile):
    message = cipherCheck.readFile(inputFile)

    if (encDec.upper() == 'ENC'):
        encryptedText = enc_vigenere(message, key)
        cipherCheck.writeFile(outputFile, encryptedText)
    elif (encDec.upper() == 'DEC'):
        decryptedText = dec_vigenere(message, key)
        cipherCheck.writeFile(outputFile, decryptedText)
    else:
        sys.exit(0)

