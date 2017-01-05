#internet stuff search within terminal
# version 2.0
#--- only seach headings as default
#--- option to search all fields 

import os
import sys
import argparse

def filterResults(key,line):
# search for the key at the beginning of the line, return true if it's there
    searchSize = len(key)
    if line[0:searchSize] == key:
        return True
    else:
        return False

def findTop(lineNumbers,fileLocation):
# when field != "#", find how many lines above the field are needed for each found item
    newNumbers = []
    tempNum = 0
    with open(fileLocation, "r") as linefile:
        for n in lineNumbers:
            linefile.seek(0)
            for i,line in enumerate(linefile):
                if i < n:
                    if len(line) < 2:
                        tempNum = i+2
                else:
                    newNumbers.append(tempNum)
                    break
    return newNumbers
"""             
try:
    word = sys.argv[1]
except:
    print "Usage: 'web <search term> [e]'"
    print "Default is to search only titles, 'e' option searches all fields, including titles.\n"
    sys.exit()
"""

parser = argparse.ArgumentParser()
parser.add_argument("query", help="string to seach for in internet.txt")
parser.add_argument("-f","--full",help="search full file instead of just titles",action="store_true")
ifile = '/home/matt/Documents/NOTES/internet.txt'
args = parser.parse_args()
word = args.query

#check for a search field (default is title)
############################################################ NOTE
##### THIS DOESN"T WORK AS INTENDED. you either check just the title, or everywhere, no matter what you put as the field
# I "find the top" before checking where the text match was made. may fix this, may not. perhaps title or everywhere is good enough
KEY = "#" #used to denote the titles of entries in the file
try:
    field = sys.argv[2]
except:
    field = "#"



# search file for the keyword and store results in temp
os.system("grep -in '"+word+"' "+ifile+" >> web_temp")
# get line numbers from temp
lineNumbers = []
tc = ""
with open('web_temp','r') as tfile:
    for line in tfile:
        for c in line:
            if c == ":":
                break
            else:
                tc += c
        lineNumbers.append(int(tc))
        tc = ""

# adjust line numbers if field is not "#"
if field != "#":
    temps = findTop(lineNumbers,ifile)
    lineNumbers = temps



#open internet.txt to get appropriate lines
with open(ifile) as internet:
    start = False
# look in internet.txt at given line numbers and get that line plus the following until a blank line is reached
    print " " #make a space from the terminal line for readability
    for n in lineNumbers:
        internet.seek(0)
        first = True # color and underline the titles
        #go to line number n and find how many lines there are before a blank line
        for i,line in enumerate(internet):
            if i == n-1:
                if filterResults(KEY,line):
                    start = True 
                else:
                    break
            if start == True:
                if len(line) > 1:
                    if first == True:
                        print "\033["+str(4)+";"+str(33)+"m"+str(line[1:])+"\033[m",
                        first = False
                    else:
                        print "\b"+line, # the \b is a backspace because the color thing makes an extra space that is ugly and this fixes it
                else:
                    start = False
                    print "\n"
                    break
# remove the temp file
os.system("rm web_temp")
