"""
Sahaja Reddy Naredla
CMPS - cryptography 
Programming assignment no.2
"""

import random
#includes the function to build the vigenere and print matrix
class VigenereTableBuild:
#Builds the vigenere tableau.
    def buildVigenere(self,seed):
        symbols =""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{#|}~"""
        self.seed = seed
        random.seed(seed)
        n = len(symbols)
        vigenere = [[0 for i in range(n)] for i in range(n)]
        symbols = list(symbols)
        random.shuffle(symbols)
        symbols = ''.join(symbols)
        
        for sym in symbols:
            random.seed(seed)
            myList = []

            for i in range(n):
                r = random.randrange(n)

                if r not in myList:
                    myList.append(r)
                else:
                    while(r in myList):
                        r = random.randrange(n)

                    myList.append(r)

                while(vigenere[i][r] != 0):
                    r = (r + 1) % n

                vigenere[i][r] = sym

        return vigenere
#print the vigenere matrix
    def printMatrix(self,v):
        i=0
        j=0
        k=0
        line = ""

        for i in range(95*95):
            line = line + v[j][k]
            j = j + 1
            if j >= 95:
                print(line)
                line = ""
                j = 0
                k = k + 1


#class incudes the functions to encrypt, decrypt, keywordfromseed
class EncryptDecrypt:
#initializes seed,symbols,vigenere
    def __init__(self,seed,symbols,vigenere):
            self.vigenere = vigenere
            self.seed = seed
            self.symbols = symbols
            self.key = ""
#generates the key
    def keywordFromSeed(self):
            Letters = []
            while self.seed > 0:
                Letters.insert(0,chr((self.seed % 100) % 26 + 65))
                self.seed = self.seed // 100
                self.key  = ''.join(Letters)
#does encryption
    def encrypt(self,m):
            key = self.key
            cipher = ""
            for i in range(len(m)):
                ki = i % len(key)
                mi = i 
                col = ord(self.key[ki])-32
                row = ord(m[mi])-32
                cipher = cipher + self.vigenere[row][col]
                 
            return cipher
#does decryption    
    def decrypt(self,cipherText):
        vigenere = self.vigenere
        symbols = self.symbols
        key = self.key
        deciText = ""
        row = 0
        col = 0
        for s in range(len(cipherText)):
            for a in range(len(symbols)):
                ki = s % len(key)
                if (key[ki]==symbols[a]):
                    col = a
            for h in range(len(symbols)):
                if vigenere[h][col] == cipherText[s]:
                    row = h
            deciText = deciText + symbols[row]
            
        return(deciText)
