import os
import re

"""
takes all the files in the current directory and renames them by: 
    -replacing all periods (except the one before file extension) and underscores with spaces
    -putting brackets around the year
    -removing everything between the year and the file extension
"""

def rename(filename):
    #takes the filename (string) and returns a new filename (string) with all periods and underscores removed
    # also puts brackets around the year and removes everything between the year and the file extension
    parts = filter(None, re.split("[. _]+", filename))
    index = 0
    for i in xrange(len(parts)):
        try:
            date = int(parts[i])
            if len(parts[i]) == 4 and date != 1080:
                index = i
        except:
            pass
    new_filename = ""
    if index > 0:
        for i in xrange(index):
            new_filename += parts[i] + " "
        new_filename += "(" + parts[index] + ")." + parts[-1]
    else:
        #new_filename = filename
        for i in xrange(len(parts)-2):
            new_filename += parts[i] + " "
        new_filename += parts[-2] + "." + parts[-1]

    return new_filename


#test = "Magic.Mike.XXL.2015.720p.BluRay.x264.YIFY.mp4"
#print rename(test)

#present working directory. i.e. where YOU are in the terminal, not where the python script is
pwd = os.getcwd()

files = os.listdir(pwd)
#test2 = "The 100 Year Old Man Who Climbed Out The Window And Disappeared (2013).srt"
#print rename(test2)
for f in files:
    if os.path.isfile(f):
        os.system('mv "'+f+'" "'+rename(f)+'"')

