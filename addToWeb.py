#make additions to the internet.txt file
##################
############
# IDEA
############################# make the prompts colorful to stand out more and be mroe readable
########## - could add this to the search functon also
############
#################
import os
import sys

#FILEPATH FOR INTERNET.TXT
filePath = "/home/matt/Documents/NOTES/internet.txt"

# ask user for title, login, pword, other
print "\033["+str(0)+";"+str(36)+"m"+str("\n Blank entries will not be recorded.\n")+"\033[m"
title = raw_input("\033["+str(0)+";"+str(33)+"m"+str("      Enter the title of the new entry: ")+"\033[m")
if len(title) < 1:
	print "\n ERROR! THE TITLE CANNOT BE LEFT BLANK!\n"
	print "\033["+str(0)+";"+str(31)+"m"+str("\n ERROR! THE TITLE CANNOT BE LEFT BLANK!\n")+"\033[m"
	sys.exit()
user   = raw_input("\033["+str(0)+";"+str(33)+"m"+str("   Enter the username of the new entry: ")+"\033[m")
login  = raw_input("\033["+str(0)+";"+str(33)+"m"+str("      Enter the login of the new entry: ")+"\033[m")
email  = raw_input("\033["+str(0)+";"+str(33)+"m"+str("      Enter the email of the new entry: ")+"\033[m")
accNum = raw_input("\033["+str(0)+";"+str(33)+"m"+str("  Enter the account # of the new entry: ")+"\033[m")
pword  = raw_input("\033["+str(0)+";"+str(33)+"m"+str("   Enter the password of the new entry: ")+"\033[m")
more   = raw_input("\033["+str(0)+";"+str(36)+"m"+str("   More info to add? ")+"\033[m")

otherName = []
otherValue = []
extra = False
while more in ["y","Y","yes","Yes","YES"]:
    extra = True
    otherName.append(raw_input("\033["+str(0)+";"+str(33)+"m"+str("     Enter the name of the next field: ")+"\033[m"))
    otherValue.append(raw_input("\033["+str(0)+";"+str(33)+"m"+str("     Enter the value of the next field: ")+"\033[m"))

    more = raw_input("\033["+str(0)+";"+str(36)+"m"+str("   More info to add? ")+"\033[m")
 
    
with open(filePath,"a") as wfile:
	wfile.write("#"+title+"\n")
	if len(user) > 0:
		wfile.write("user: "+user+"\n")
	if len(login) > 0:
		wfile.write("login: "+login+"\n")
	if len(email) > 0:
		wfile.write("email: "+email+"\n")
	if len(accNum) > 0:
		wfile.write("acc #: "+accNum+"\n")
	if len(pword) > 0:
		wfile.write("pword: "+pword+"\n")
	if extra == True:
		for i in xrange(len(otherName)):
			wfile.write(otherName[i]+": "+otherValue[i]+"\n")
	wfile.write("\n") #search doesn't work if there is not an empty line at the bottom of the page (for non-title searches it will miss the last line)

print "\n-------------- Completed ----------------\n"

#os.system("tail -f temp.txt")
