import sys


def enc_cipher(message,key):
    #Caesar Cipher
    #Letters are incremented by codeWord A + C = 1 + 3 = D

    #changes message into list of chars
    encrypted = []

    for i in range(0, len(message)):
        #if the letter is upper continue
        if message[i].isupper():
            
            enc = ord(message[i]) + key
            while enc > ord('Z'):
                enc -= 26
            encrypted.append(chr(enc))
            
        #assuming its lower since not upper
        elif message[i].islower():

            enc = ord(message[i]) + key

            #if it exceeds the alphabet
            while enc > ord('z'):
                enc -= 26
            encrypted.append(chr(enc))
            
        else:
            encrypted.append(" ")

    #changes from list to string
    encrypted = ''.join(map(str,encrypted))

    return encrypted

def dec_cipher(message,key):
    #Caesar Cipher

    decrypted = []

    for i in range(0, len(message)):
        #if the letter is upper continue
        if message[i].isupper():
            dec = ord(message[i]) - key
            while dec < ord('A'):
                dec += 26
            decrypted.append(chr(dec))
            
        #assuming its lower since not upper
        elif message[i].islower():

            dec = ord(message[i]) - key

            #if it exceeds the alphabet
            while dec < ord('a'):
                dec -= 26
            decrypted.append(chr(dec))
            
        else:
            decrypted.append(" ")


    #changes from list to string
    decrypted = ''.join(map(str,decrypted))
    
    return decrypted


if __name__ == "__main__":
    message = "hello"
    key =  1

    print("message",message,sep=' ')
    enc_message = enc_cipher(message,key)
    print(enc_message)

    dec_message = dec_cipher(enc_message,key)
    print(dec_message)
    
    
