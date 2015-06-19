"""
This program changes nz time to ontario time and vice versa
user inputs a time and place and the program returns the corresponding time in the other place
"""

#import time
from datetime import datetime
import pytz
import argparse


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


def formatZone(zone):
	if zone.lower() in ['on','ontario','ottawa','toronto','bowmanville','colborne','colbourne','canada','can']:
		return "on"
	elif zone.lower() in ['nz','new','new zealand','kiwi','gisborne','gizzy','auckland','wellington']:
		return "nz"
	else:
		print "ERROR -- INVALID TIME ZONE. Please try again with either 'on' or 'nz' after the time"
		sys.exit()


def get_time_diff():
	onz = pytz.timezone("US/Eastern")
	nzz = pytz.timezone("Pacific/Auckland")
	ont = datetime.now(onz)
	nzt = datetime.now(nzz)
#	ontt = ont.timetuple()
#	nztt = nzt.timetuple()
#	print "     current NZ time:",nzt
#	print "current Ontario time:",ont
	odif = int(str(nzt)[-5:-3]) # this is the UTC (or maybe GMT) offset, it will be negative 3-4
	ndif = int(str(ont)[-5:-3]) # this is the UTC (or maybe GMT) offset, it will be positive 12-13
#	print "time difference is",odif+ndif
	return odif+ndif


def get_other_time(time1,zone1,td):
	day_change={-1:" the day before in ",0:" the same day in ",1:" the day after in "}
	day = 0
	if zone1 == 'nz':
		td = -1*td
	h1 = int(time1[:2])
	h2 = h1 + td
	if h2 < 0:
		h2 = 24 + h2
		day = -1
	elif h2 >= 24:
		h2 = h2 - 24
		day = 1
	return twoDigits(h2)+time1[2:]+day_change[day]


def print_conversion(time1,zone1,time2):
	if zone1 == 'on':
		zone2 = "New Zealand"
		zone1 = "Ontario"
	else:
		zone2 = "Ontario"
		zone1 = "New Zealand"
	print "\n","-"*64
	print "---  "+time1+" in "+zone1+" is "+time2+zone2+"  ---"
	print "-"*64,"\n"

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="get time and time location from command line")
	parser.add_argument('time', help="time in either h:m or h:m<a/p> format")
	parser.add_argument('zone', help="the zone is either 'nz' or 'on'")
	args = parser.parse_args()

	base_time = formatTime(args.time)		
	base_zone = formatZone(args.zone)		

	time_diff = get_time_diff()

	other_time = get_other_time(base_time,base_zone,time_diff)

	print_conversion(base_time,base_zone,other_time)




