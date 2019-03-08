import sys
import re
import playfair_cipher
import vigenere_cipher
import caesar_cipher
import railfence_cipher
import rowTransposition_cipher

# Check if cipher entered in is included in options
def checkCipherName(x, y):
    if (x != y[0] and x != y[1] and x != y[2] and x != y[3] and x != y[4]):
        print('Invalid cipher name used')
        sys.exit(0)
    else:
        print('Your cipher: ' + x)

# Check if user entered in enc or dec
def checkEncDec(z):
    z = z.upper()
    if (z != 'ENC' and z != 'DEC'):
        print('Your option ' + z + ' is invalid. Enter in either "ENC" to encrypt or "DEC" to decrypt!')
        sys.exit(0)
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
        sys.exit(0)
    elif (not txtExtension):
        print('Invalid input file extension: ' + a)
        sys.exit(0)
    else:
        print('Invalid output file extension: ' + b)
        sys.exit(0)

# Reading files
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

def writeFile(h, text):
    fn = open(h, 'w')
    fn.write(text)
    fn.close()

# c = cipherName, d = cipherList, e = key, f = encDec, g = inputFile, h = outputFile
def cipherInterface(c, d, e, f, g, h):
    if (c == d[0]):
        print('Playfair cipher chosen')
        playfair_cipher.playFairCipher(e, f, g, h)
    elif (c == d[1]):
        print('Row Transpostion cipher chosen')
        rowTransposition_cipher.rowTransposition_main(e, f, g, h)
    elif (c == d[2]):
        print('Railfence cipher chosen')
        railfence_cipher.railfence_main(e, f, g, h)
    elif (c == d[3]):
        print('Vigenere cipher chosen')
        vigenere_cipher.vigenere_main(e, f, g, h)
    elif (c == d[4]):
        print('Caesar cipher chosen')
        caesar_cipher.caesar_main(e, f, g, h)