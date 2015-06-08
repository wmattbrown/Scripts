# redone encryption program (better...hopefully)
# idea - different key options
#	1-use default key (i.e. pi to ~50 digits)
#	2-use a user defined key (not a good idea, too easy to mess it up. maybe keep it as an option though)
#	3-create a random key and hide it in the encrypted file (only this program knows where to find the key) - NOT IMPLEMENTED YET

# not sure if 1 or 3 is a better/safer option might use 1 just so it works with previously encrypted files
# should have both options implemented so that I can change later if I want
import sys
import os

def encryptedMark():
	return "xwqZ3#pE2'*(,t. l9Of5\n"
		   
def isEncrypted(infile):
	if infile.readline() == encryptedMark():
		return True
	else:
		return False

def printDirections():
	#print "python newEncrypt.py <filename> [<key>] where key is an optional string of numbers"
    print "enc <filename> [<key>] where is key is an optional string of numbers"

def encryptFile(infile,key):
	if key == getKey():
		print "Encrypting using the default key"
	else:
		print "Encrypting using custom key : '"+key+"'"
	count = 0
	keyLength = len(key)
	infile.seek(0)
	with open("temp","w+") as tempOut:
		tempOut.write(encryptedMark())
		for line in infile:
			for char in line:
				tempOut.write(chr(ord(char) + int(key[count])))
				count += 1
				if count >= keyLength:
					count = 0
	

def decryptFile(infile,key):
	if key == getKey():
		print "Decrypting using the default key"
	else:
		print "Decrypting using custom key : '"+key+"'"
	count = 0
	keyLength = len(key)
	firstLine = 0
	with open("temp","w+") as tempOut:
		for line in infile:
			if firstLine == 0:
				firstLine = 1
			for char in line:
				tempOut.write(chr(ord(char) - int(key[count])))
				count += 1
				if count >= keyLength:
					count = 0



def getKey():
	return "314159265358979311599796346854418516159057617187500"

def overwriteFile(filename):
	"""
	filename is the original file, to be overwritten with the temporary file "temp"
	"""
	with open (filename,"w") as replaceFile:
		with open("temp","r") as temp:
			for line in temp:
				for c in line:
					replaceFile.write(c)
	os.system("rm temp")

def fileExists(filename):
	if os.path.isfile(filename):
		return True
	else:
		return False

def main():
	# make sure a file was provided
	try:
		filename = sys.argv[1]
	except:
		printDirections()
		return None

	# check if a custom key was used
	try:
		key = sys.argv[2]
	except:
		key = getKey()

	# check that the file provided exists
	if fileExists(filename) == False:
		print "FILE NOT FOUND!"
		return None
	else:
		with open(filename,"r") as infile:
			if isEncrypted(infile):
				decryptFile(infile,key)
			else:
				encryptFile(infile,key)
		overwriteFile(filename)
	

if __name__ == "__main__":
	main()
