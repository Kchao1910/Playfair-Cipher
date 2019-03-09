import sys
import re
from collections import OrderedDict
import cipherCheck
import playfair_cipher
import vigenere_cipher

# start of main()
cipherList = ['PLF', 'RTS', 'RFC', 'VIG', 'CES']


# Remember that the first argument of the script is the file name, thus start at index 1
cipherName = str(sys.argv[1])
key = str(sys.argv[2])
encDec = str(sys.argv[3])
inputFile = str(sys.argv[4])
outputFile = str(sys.argv[5])

argumentList = [cipherName, key, encDec, inputFile, outputFile]
cipherCheck.checkCipherName(cipherName, cipherList)
cipherCheck.checkEncDec(encDec)
cipherCheck.checkFileExtension(inputFile, outputFile)
cipherCheck.cipherInterface(cipherName, cipherList, key, encDec, inputFile, outputFile)
