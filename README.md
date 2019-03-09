# CPSC 452 Assignment 1
__Authors__

Jake Cliff: tallmadman@csu.fullerton.edu

Kenny Chao: kchao@csu.fullerton.edu

Scott Ng: scottng49@csu.fullerton.edu

#
__Languaged Used__

Python 3.7.1

#
__How to Execute__
```
command line: python .\cipherInterface.py <cipher name> <keyword> <enc/dec> <input file> <output file>

*The examples down below for decryption assume that the user doesn't switch 'output.txt' for 'input.txt', in other words the user saves the ciphertext in 'input.txt' when decrypting.
```
__Caesar Encrypt/Decrypt__
```
Ex. python .\cipher.py CES 3 enc .\input.txt .\output.txt
Ex. python .\cipher.py CES 3 dec .\input.txt .\output.txt
```
__Playfair Encrypt/Decrypt__
```
Ex. python .\cipher.py PLF security enc .\input.txt .\output.txt
Ex. python .\cipher.py PLF security dec .\input.txt .\output.txt
```
__Vigenere Encrypt/Decrypt__
```
Ex. python .\cipher.py VIG security enc .\input.txt .\output.txt
Ex. python .\cipher.py VIG security dec .\input.txt .\output.txt
```
__Railfence Encrypt/Decrypt__
```
Ex. python .\cipher.py RFC 3 enc .\input.txt .\output.txt
Ex. python .\cipher.py RFC 3 dec .\input.txt .\output.txt
```
__Row Transposition Encrypt/Decrypt__
```
Ex. python .\cipher.py RTS 3142 enc .\input.txt .\output.txt
Ex. python .\cipher.py RTS 3142 dec .\input.txt .\output.txt
```
#
__Extra Credit__

N/A
#
__Special Notes__

None
