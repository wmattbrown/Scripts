#Timer program
# version 2.0
# this is badly out of date and isn't even an alarm...i guess i need to start over
# now have 3 options
#	-volume (current system sound is default)
#	-alarm sound (first track is default)
#	-big or small output (small is default)
#	-ONLY SMALL OUTPUT. 
# WHAT I NEED TO DO
#	-make it display the end time in the same format as the user input
#	-check for valid times. i.e. if pm/am provided, hours<=12, otherwise hours<24, min<60
"""
 A simple terminal timer
 User inputs a time in either h:m:s or m:s or s format.
 After user defined time, an audio clip is played
 OPTIONS:
 -v 	set the system volume before audio is played. integer values 0-8 are accepted. Default is current system volume.

 -a 	choose audio to be played. integer values of 1-11 are accepted. Default value is 1
"""
	

import time
import sys
import os
import argparse

def printDescription():
	print "Timer - A simple terminal timer\n\n timer <time> <options>\n"
 	print "User inputs a time in either h:m:s or m:s or s format."
 	print "After user defined time, an audio clip is played.\n"
 	print "OPTIONS:\n"
 	print "-v 	Set the system volume before audio is played."
 	print " 	Integer values 0-8 are accepted."
 	print " 	Default is current system volume.\n"

 	print "-a 	Choose audio to be played."
 	print " 	Integer values of 1-11 are accepted."
 	print " 	Default value is 1.\n"
 	print "CAUTION: only works for lengths of time less than 24 hours"
 	return None

def printColor(effect,color,text):
	"""display formatted text"""
#=== COLOURS
# black 	30
# red		31
# green		32
# yellow	33
# blue		34
# purple	35
# cyan		36
# white		37
#=== EFFECTS
# none		0
# bold		1
# underline	4
# blink		5
# inverse	7
# hidden	8
	print"\033["+str(effect)+";"+str(color)+"m"+str(text)+"\033[m"

def printTimeRemaining(timeLeft,timeIsLeft):
	""" Display the time remaining in regular font """
	if timeIsLeft == 1:
		print "\033[1A\033[K"+" REMAINING TIME: "+"\033[1;36m"+timeLeft+"\033[m"
	else:
		print "\033[1A\033[K"+" REMAINING TIME: "+"\033[7;36m"+timeLeft+"\033[m"
	return None

def printTimes(end):
	print "\n       END TIME: \033[1;31m"+str(end)+"\033[m"

def twoDigits(integer):
	"""Converts an integer into a 2 digit string of that integer"""
	if len(str(integer)) == 1:
		return "0"+str(integer)
	else:
		return str(integer)

def formatTime(inTime):
	"""make sure user input time is acceptable format and put into 24hr format"""
	#make sure it's h:mm or hh:mm
	#check for am/pm -- if it doesn't have a 'p' then take it as 24 hour
	if inTime[1] != ":" and inTime[2] != ":":
		print "ERROR: Time is not in the correct format. Please try again with 'hh:mm' format"
		sys.exit()
	else:
		temp = inTime.index(":")
		if len(inTime) > temp+3:
			if "p" in inTime or "P" in inTime:
				newh = int(inTime[0:temp]) + 12
				return str(newh)+inTime[temp:temp+3]
		return twoDigits(int(inTime[0:temp]))+inTime[temp:temp+3]	

def getTimeLeft(timeParts):
	""" calculates the time left in hh:mm:ss format and returns if there is still time left as boolean"""
	now = time.asctime()[11:20]
	nowHour = int(now[0:2])
	nowMin = int(now[3:5])
	nowSec = int(now[6:8])
	
	sleft = 60 - nowSec
	if sleft == 60:
		sleft = 0
	mleft = timeParts[1] - nowMin - 1
	if mleft == -1:
		mleft = 0
		extrah = 0
	elif mleft < -1:
		mleft = 60 + mleft
		extrah = 1
	else:
		extrah = 0
	hleft = timeParts[0] - nowHour - extrah
	if sleft+mleft+hleft < 1:
		return "00:00:00",True
	else:
		return twoDigits(hleft)+":"+twoDigits(mleft)+":"+twoDigits(sleft), False

def setVolume(level):
	"""Set the system volume before playing the sound
	any numeric value is acceptable but only integer values 0-8 are accepted"""
	os.system("amixer -q sset 'Master' "+str(level)+"\%")
	return None


###########################################################################################
###########################################################################################
###########################################################################################
######################################   MAIN   ###########################################
###########################################################################################
###########################################################################################
###########################################################################################


# parser for arguments

parser = argparse.ArgumentParser(description="get optional parameters from command line")
parser.add_argument('Time', help='Time in hh:mm format, either 24hr or am/pm')
parser.add_argument('-v','--volume',help='set volume %')
parser.add_argument('-a','--alarm',help='choose alarm sound (1-11, or 0 for no alarm')
args = parser.parse_args()

if args.volume:
	volume = int(args.volume)
else:
	volume = -1

if args.alarm:
	alarm = int(args.alarm)
else:
	alarm = 1


alarms = {1:"CT_fanfare_III.mp3",2:"600_AD.mp3",3:"avalanche.mp3",4:"bombom_1.mp3",5:"bombom_2.mp3",6:"Everything_is_Awesome.mp3",7:"Medina_1000AD.mp3",8:"passion.mp3",9:"the_funeral.mp3",10:"The_Walking_Dead.mp3",11:"time_scar.mp3"}
if alarm != 0:
	if alarm != "":
		audio_file = alarms[alarm]
	else:
		audio_file = alarms[1]

inTime = args.Time

endTime = formatTime(inTime)
timeParts = [int(endTime[0:2]),int(endTime[3:6])]

printTimes(inTime)
print " ========================\n\n\n\n\033[1A\033[1A\033[1A"

isDone = False
timeLeft,isDone = getTimeLeft(timeParts)
printTimeRemaining(timeLeft,1,)
while isDone == False:
	time.sleep(1)
	timeLeft,isDone = getTimeLeft(timeParts)
	printTimeRemaining(timeLeft,1)
printTimeRemaining(timeLeft,0)
print ""
	

if volume >= 0:
	setVolume(volume)
if alarm != 0:
   os.system("mpg321 -q ~/Programming/timer_alarms/"+audio_file)
