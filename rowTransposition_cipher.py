import sys
import cipherCheck
#keyword is number string
def enc_rowTransposition(message, key):

def dec_rowTransposition(message, key):

def rowTransposition_main():
    message = cipherCheck.readFile(inputFile)

    if (encDec.upper() == 'ENC'):
        encryptedText = enc_rowTransposition(message, key)
        cipherCheck.writeFile(outputFile, encryptedText)
    elif (encDec.upper() == 'DEC'):
        decryptedText = dec_rowTransposition(message, key)
        cipherCheck.writeFile(outputFile, decryptedText)
    else:
        sys.exit(0)