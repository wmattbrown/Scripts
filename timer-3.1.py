#Timer program
#VERSION 3.1 
#	-option of big or small timer display
#	-uses argparse instead of sys.argv to get options
"""
 A simple terminal timer for Linux
 User inputs a time in either h:m:s or m:s or s format.
 After user defined time, an audio clip is played
 OPTIONS:
 -v 	set the system volume before audio is played. integer values 0-100 are accepted. Default is current system volume.

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
 	print " 	Integer values 0-100 are accepted."
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

def printBanner():
	""" Display the 'Timer' banner on screen"""
	color = 34
	effect = 1
	os.system("clear") 
	indent = "         "
	print ""
	printColor(effect,color,indent+"############")
#	printColor(effect,color,indent+"     ##")
	printColor(effect,color,indent+"     ##        ##")
	printColor(effect,color,indent+"     ##                 ##    ##         #######      ## ######")
	printColor(effect,color,indent+"     ##        ##      ## ## ## ##      ##     ##     ####    ##")
	printColor(effect,color,indent+"     ##        ##     ##   ##    ##     #########     ##")
	printColor(effect,color,indent+"     ##        ##     ##         ##     ##            ##")
	printColor(effect,color,indent+"     ##        ##     ##         ##      ########     ##")
#	print ""


def printTimeRemaining(seconds,digits,limit):
	"""Display the time remaining if very large font (8x8 characters)"""
	if seconds >= limit:
		effect = 1
		color = 36
		effect2 = 1
		color2 = 35
	else:
		effect = 5
		color = 31
		effect2 = 7
		color2 = 31
	print "      "+"\033["+str(effect2)+";"+str(color2)+"m"+str("==========================  Time Remaining  ============================")+"\033[m"
	timeDigits = getTimeDigits(seconds)
	for i in xrange(7):
		print "         "+"\033["+str(effect)+";"+str(color)+"m"+str(" "+digits[timeDigits[0]][i]+digits[timeDigits[1]][i]+digits[timeDigits[2]][i]+digits[timeDigits[3]][i]+digits[timeDigits[4]][i]+digits[timeDigits[5]][i]+digits[timeDigits[6]][i]+digits[timeDigits[7]][i])+"\033[m"
	print "      "+"\033["+str(effect2)+";"+str(color2)+"m"+str("========================================================================")+"\033[m"
	return None

def printTimeRemaining2(seconds,timeLeft):
	""" Display the time remaining in regular font """
	if timeLeft == 1:
		print "\033[1A\033[K"+" REMAINING: "+"\033[1;36m"+secondsToTime(seconds)+"\033[m"
	else:
		print "\033[1A\033[K"+" REMAINING: "+"\033[7;36m"+secondsToTime(seconds)+"\033[m"
	return None

def getTimeDigits(seconds):
	"""takes a time in seconds and returns the digits of hh:mm:ss as corresponds to their digits key for large display"""
	timeDigits = []
	longTime = secondsToTime(seconds)
	if longTime.index('h') == 1:
		timeDigits.append(0)
	for c in longTime:
		if c not in ['h','m','s']:
			timeDigits.append(int(c))
		elif c != 's':
			timeDigits.append('colon')
	return timeDigits


def secondsToTime(seconds):
	"""Convert time in seconds to hmmss format
	Returns string as ##h##m##s"""
	hours = seconds/3600
	minutes = (seconds - 3600*hours)/60
	seconds = seconds - 3600*hours - 60*minutes
	return str(hours)+"h"+twoDigits(minutes)+"m"+twoDigits(seconds)+"s"

def printTimes(start,end,total):
	"""display start, end, and total times"""
	print "          Start \033["+str(0)+";"+str(32)+"m"+str(start)+"\033[m"+"         "+"Finish \033["+str(0)+";"+str(31)+"m"+str(end)+"\033[m"+"         "+" Total \033["+str(0)+";"+str(33)+"m"+str(total)+"\033[m"

def printTimes2(start,end,total):
	"""display start, end, and total times"""
	print ""
	print "     START: \033[0;32m"+str(start)+"\033[m"
	print "       END: \033[0;31m"+str(end)+"\033[m"
	print "     TOTAL: \033[0;33m"+str(total)+"\033[m"

def twoDigits(integer):
	"""Converts an integer into a 2 digit string of that integer"""
	if len(str(integer)) == 1:
		return "0"+str(integer)
	else:
		return str(integer)

def getEndTime(sh,sm,ss,ts):
	"""Calculates the end time, given the start time in hours, minutes, seconds, and total time in seconds 
	Returns end time as string in format hh:mm:ss and the endday (0=today, 1=tomorrow)"""
	temp = int(ts)/3600
	eh = int(sh) + temp
	temp2 = (ts - temp*3600)/60
	em = int(sm) + temp2
	es = int(ss) + ts - temp*3600 - temp2*60
	# make sure seconds are under 60
	if es > 59:
		temp = es/60
		es -= 60
		em += temp
		if em > 59:
			temp = em/60
			em -= 60
			eh += temp
	if eh >= 24:
		eh -= 24
		ed = 1
	else:
		ed = 0
	return twoDigits(eh)+":"+twoDigits(em)+":"+twoDigits(es),ed

def getTimes(totalSeconds):
	"""using the total time of the timer in seconds (totalSeconds, an integer) this calculates the start, end, and total time
	Returns startTime and endTime in hh:mm:ss format and total time in #h##m##s format"""
	startTime = time.strftime("%H:%M:%S")
	startHour = time.strftime("%H")
	startMinute = time.strftime("%M")
	startSecond = time.strftime("%S")
	endTime,endDay = getEndTime(startHour,startMinute,startSecond,totalSeconds)
	totalTime = secondsToTime(totalSeconds)
	return startTime,endTime,totalTime,endDay


def getSeconds(text):
	""" text is the time as a string in h:mm:ss format
	Returns the total number of seconds to represent that time"""
	hours = ""
	minutes = ""
	seconds = ""
	if ":" in text:
		count = 0
		for c in text:
			if c == ":":
				count += 1
		temp = ""
		for c in text:
			if c != ":":
				temp += c
			elif count == 2:
				hours = temp
				temp = ""
				count -= 1
			elif count == 1:
				minutes = temp
				temp = ""
		seconds = temp
		if hours != "":
			totalSeconds = int(seconds) + int(minutes)*60 + int(hours)*3600
		elif minutes != "":
			totalSeconds = int(seconds) + int(minutes)*60
		else:
			totalSeconds = int(seconds)
	else:
		totalSeconds = int(text)
	return totalSeconds

def setVolume(level):
    """Set the system volume before playing the alarm.
    any whole number value 0-100 is accepted"""
    os.system("amixer -q sset 'Master' "+str(level)+"\%")
    return None

def getDigits():
	"""the definition of the digits 0-9 and a colon for the purpose of large display on screen"""
	digits = {}
	digits[0] = [" ------  ","|      | ","|      | ","|      | ","|      | ","|      | "," ------  "]
	digits[1] = ["    /    ","   /|    ","    |    ","    |    ","    |    ","    |    ","   _|_   "]
	digits[2] = [" ------  ","       | ","       | "," ------  ","|        ","|        "," ------  "]
	digits[3] = [" ------  ","       | ","       | ","  -----  ","       | ","       | "," ------  "]
	digits[4] = ["|    |   ","|    |   ","|    |   ","|------- ","     |   ","     |   ","     |   "]
	digits[5] = [" ------  ","|        ","|        "," ------  ","       | ","       | "," ------  "]
	digits[6] = [" ------  ","|        ","|        ","|------  ","|      | ","|      | "," ------  "]
	digits[7] = [" ------  ","|      | ","       | ","      |  ","     |   ","    |    ","   |     "]
	digits[8] = [" ------  ","|      | ","|      | "," ------  ","|      | ","|      | "," ------  "]
	digits[9] = [" ------  ","|      | ","|      | "," ------| ","       | ","       | "," ------  "]
	digits['colon'] = ["      ","      ","  o   ","      ","  o   ","      ","      "]
	return digits

def getLimit(seconds):
	"""Defines the time remaining (in seconds) when the display should change colour and start flashing
	Returns an integer of seconds"""
	if seconds > 3600: # if more than 1 hour, start flashing at 5 minutes to go
		return 300
	elif seconds > 600: # if more than 10 minutes, start flashing at 1 minute to go
		return 60
	elif seconds > 60: # if more than 1 minute, start flashing at 10 seconds to go
		return 10
	else: # if less than 1 minute, don't flash until done
		return 1


def getTimeRemaining(endTime,endDay):
	"""uses system current time and previously calculated endTime to calculate time remaining
	ch,cm,cs are the hour, minute, and second values of the current time
	eh,em,es are the hour, minute, and second values of the endTime (previously calculated)
	Returns the remaining time in seconds as an integer
	"""
	ch = int(time.strftime("%H"))
	cm = int(time.strftime("%M"))
	cs = int(time.strftime("%S"))
	eh = int(endTime[0:2])
	em = int(endTime[3:5])
	es = int(endTime[6:8])

	if endDay == 1:
		rh = 24 + eh-ch
	else:
		rh = eh-ch
	rm = em-cm
	rs = es-cs
	if rs < 0 and (rm > 0 or rh > 0):
		rs = 60+rs
		rm -= 1
	if rm < 0:
		rm = 60+rm
		rh -= 1
	return rh*3600+rm*60+rs


###########################################################################################
###########################################################################################
###########################################################################################
######################################   MAIN   ###########################################
###########################################################################################
###########################################################################################
###########################################################################################

# parser for arguments

parser = argparse.ArgumentParser(description="get optional parameters from command line")
parser.add_argument('Time', help='Time in either seconds, m:s, or h:m:s format')
parser.add_argument('-v','--volume',help='set volume %')
parser.add_argument('-a','--alarm',help='choose alarm sound (1-11, or 0 for no alarm')
parser.add_argument('-b','--big',help='turn on large clock face for timer',action="store_true")
args = parser.parse_args()

if args.volume:
	volume = int(args.volume)
else:
	volume = -1

if args.alarm:
	alarm = int(args.alarm)
else:
	alarm = 1
totalSeconds = getSeconds(args.Time)
limit = getLimit(totalSeconds)

alarms = {1:"CT_fanfare_III.mp3",2:"600_AD.mp3",3:"avalanche.mp3",4:"bombom_1.mp3",5:"bombom_2.mp3",6:"Everything_is_Awesome.mp3",7:"Medina_1000AD.mp3",8:"passion.mp3",9:"the_funeral.mp3",10:"The_Walking_Dead.mp3",11:"time_scar.mp3"}
if alarm != 0:
	audio_file = alarms[alarm]

startTime,endTime,totalTime,endDay = getTimes(totalSeconds)

seconds = getTimeRemaining(endTime,endDay)
if args.big: ############################ BIG CLOCK STYLE TIMER
	digits = getDigits()
	while seconds > 0:
		printBanner()
		printTimes(startTime,endTime,totalTime)
		printTimeRemaining(seconds,digits,limit)
		time.sleep(1)
		seconds = getTimeRemaining(endTime,endDay)
	printBanner()
	printTimes(startTime,endTime,totalTime)
	printTimeRemaining(seconds,digits,limit)
	printColor(5,35,"                                  TIME IS UP!!!")
else: ########################## SMALL CLOCK STYLE TIMER
	printTimes2(startTime,endTime,totalTime)
	print "==========================\n\n\n\033[1A\033[1A"
	while seconds > 0:
		printTimeRemaining2(seconds,1)
		time.sleep(1)
		seconds = getTimeRemaining(endTime,endDay)
	printTimeRemaining2(seconds,0)
	print ""
if volume >= 0:
	setVolume(volume)
if alarm != 0:
   os.system("mpg321 -q ~/Programming/timer_alarms/"+audio_file)

