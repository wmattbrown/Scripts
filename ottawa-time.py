# THIS IS A SMALL PROGRAM TO TELL ME WHAT TIME IT IS IN OTTAWA RIGHT NOW
from datetime import datetime
try:
    import pytz
except:
    print "FAILED\nmodule <pytz> could not be imported"


ottawa_zone = pytz.timezone('US/Eastern')
ottawa_date_time = str(datetime.now(ottawa_zone))
ottawa_time = ottawa_date_time[11:16]
ottawa_day = ottawa_date_time[8:10]

nz_zone = pytz.timezone('Pacific/Auckland')
nz_date_time = str(datetime.now(nz_zone))
nz_day = nz_date_time[8:10]

same_day = nz_day == ottawa_day

print "\n\033[91m===== CURRENT TIME IN OTTAWA =====\033[0m"
print "              \033[93m"+ottawa_time+"\033[0m"
if same_day:
    print "             \033[90m(today)\033[0m"
else:
    print "           \033[90m(yesterday)\033[0m"
print ""
