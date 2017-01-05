
#ADD BOOKS TO LIST OF BOOKS OWNED
##################
############
# IDEA
#--------------- MAKE SURE NOT REPEATING AN ENTRY
#   -check if title and author are the same
#   -check if str.lowercase() are the same, to increase chance of catching duplicates
#   -show both entries and ask if user wants to save it or not


############## it's al fucked up
################ this is why i need version control.....FUCK ME
# i tried to make it so when you mess up an entry (invalid unpit) it doesn't quit the program, it lets you just start over with a new book or quit
# the only check that still works is the check if blank one


import os
import sys

YESNO = ['y','Y','n','N']
another = 'y'
# check that input is a number
def is_num(string,field): #not working
    try: 
        int(string) + 1
        return True
    except:
        return False

def invalid_input():
    print "\033["+str(0)+";"+str(31)+"m"+str("\n ERROR! INVALID INPUT!\n")+"\033[m"
    return None

def is_char(string,chars):# not working
    #string is  what the user input
    #chars is a list of acceptable inputs
    if string in chars:
        return True
    else:
        print "\033["+str(0)+";"+str(31)+"m"+str("\n ERROR! INVALID INPUT!\n")+"\033[m"
        return False

def not_blank(string):
    if len(string) > 0:
        return True
    else:
        print "\033["+str(0)+";"+str(31)+"m"+str("\n ERROR! < "+f+" > CANNOT BE LEFT BLANK!\n")+"\033[m"
        return False

def check_duplicate(author,title,filename):
    with open(filename,"r") as infile:
        for line in infile:
            book = line.split("|")
            if book[0].lower() == title.lower():
                record = ""
                while record not in YESNO:
                    record = raw_input("\033["+str(0)+";"+str(31)+"m"+str("There is already an entry with the title '"+book[0]+"' by '"+book[1]+"'\nRecord new entry anyway?(y/n) ")+"\033[m")
                if record in ['y','Y']:
                    return True
                else:
                    return False
    return True


#FILEPATH FOR INTERNET.TXT
filePath = "/home/matt/Documents/NOTES/book_list.txt"

while another.lower() == 'y':
    skip = False
    #### fields
    fields = ["Title",
        "Author",  
        "Series",
        "Number in Series",
        "Publication Date",
        "# Pages",
        "Hardcover/Paperback (h/p)",
        "Read by Matt (y/n)",
        "Read by Janessa (y/n)"]  
    inputs = []
    for f in fields:
        if f == fields[3] and len(inputs[2]) < 1:
            inputs.append("")
            continue
        inputs.append(raw_input("\033["+str(0)+";"+str(33)+"m"+str(f+": ").rjust(27)+"\033[m"))

        if f != fields[2]:
            if not not_blank(inputs[-1]):
                invalid_input()
                skip = True
                break
            elif f in [fields[3],fields[4],fields[5]]:
                if not is_num(inputs[-1],f):
                    invalid_input()
                    skip = True
                    break
            elif f == fields[6]:
                if inputs[-1].lower() not in ['h','p']:
                    invalid_input()
                    skip = True
                    break
            elif f in [fields[7],fields[8]]:
                if inputs[-1] not in YESNO:
                    invalid_input()
                    skip = True
                    break
        
    ### after it's checked to be a valid entry, capitalize the h/p and y/n's
    if skip == False:
        for i in xrange(6,9):
            inputs[i] = inputs[i].capitalize()
        #check to see if the book is alreayd in the list (by checking the titles only - very basic, not very reliable because of typos)
        if check_duplicate(inputs[1],inputs[0],filePath):
            # write to file
            with open(filePath,"a") as wfile:
                wfile.write("|".join(inputs)+"\n")

    another = raw_input("\nEnter another book?(y/n) ")# ADD COLOUR TO THIS LINE
    print ""



print "ALL DONE!"
