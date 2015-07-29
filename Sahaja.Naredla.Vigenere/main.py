
"""
Sahaja Reddy Naredla
CMPS - cryptography 
Programming assignment no.2
"""
import argparse
import randomized_vigenere 

#accepts the data from command line and process it.
def main():
	print()
	print("Program by Sahaha Reddy Naredla")
	print("Implementation of Vigenere Cipher")
	print()
	
	vigenere = randomized_vigenere.VigenereTableBuild()
	symbols =""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{#|}~"""

	parser = argparse.ArgumentParser()

	parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
	parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
	parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
	parser.add_argument("-s", "--seed", dest="seed",default = 12001907, help="Integer seed")

	args = parser.parse_args()
	seed = int(args.seed)

	f = open(args.inputFile,'r')
	message = f.read()

	vigTable = vigenere.buildVigenere(seed)
	encryDecrypt = randomized_vigenere.EncryptDecrypt(seed,symbols,vigTable)
	encryDecrypt.keywordFromSeed()

	if(args.mode == 'encrypt'):
			cipherText = encryDecrypt.encrypt(message)  
			o = open(args.outputFile,'w')
			o.write(str(cipherText))
	else:
		decipherMsg = encryDecrypt.decrypt(message)
		o = open(args.outputFile,'w')
		o.write(str(decipherMsg))

if __name__ == '__main__':
    main()



