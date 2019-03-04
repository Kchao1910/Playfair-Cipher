#Vigenere Cipher
#Letters are incremented by codeWord A + C = 1 + 3 = D

def enc_vigenere(message,key):

    encrypted = []
    c = 0

    for i in range(0, len(message)):
        #if the letter is upper continue
        if message[i].isupper():

            enc = ord(message[i]) + ord(key[c%len(key)])
            while enc > ord('Z'):
                enc -= 26
            encrypted.append(chr(enc))
            c += 1
            
        #assuming its lower since not upper
        elif message[i].islower():
                
            enc = ord(message[i]) + ord(key[c%len(key)])
            while enc > ord('z'):
                enc -= 26
            encrypted.append(chr(enc))  
            c += 1
            
        else:
            encrypted.append(" ")

    encrypted = ''.join(map(str,encrypted))

    return encrypted

def dec_vigenere(message,key):
    
    decrypted = []
    c = 0

    for i in range(0, len(message)):
        #if the letter is upper continue
        if message[i].isupper():

            dec = ord(message[i]) - ord(key[c%len(key)])
            while dec < ord('A'):
                dec += 26
            decrypted.append(chr(dec))
            c += 1
            
        #assuming its lower since not upper
        elif message[i].islower():
                
            dec = ord(message[i]) - ord(key[c%len(key)])
            while dec < ord('a'):
                dec += 26
            decrypted.append(chr(dec))  
            c += 1
            
        else:
            decrypted.append(" ")

    decrypted = ''.join(map(str,decrypted))

    return decrypted
    
    
