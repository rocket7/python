#STORE DATE AS UTC


import time

import datetime

# TIMEZONE GIVES NUMBER OF SECONDS OFF GMT/UTC and NEED TO CHECK DST

# NEED TO CHECK VALUE OF DST_TIME_DAYLIGHT

#GET EPOCH and FORMAT %c WITH LOCALE SPECIFIC FORMAT - STRFTIME()
# GMTIME - Convert a time expressed in seconds since the epoch to a struct_time in UTC in which the dst flag is always zero.
# If secs is not provided or None, the current time as returned by time() is used.
print("Epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

# TIME.DAYLIGHT (NONZERO if DST TIMEZONE DEFINED)
# TIME.TIMEZONE - The offset of the local (non-DST) timezone in seconds
# TIME.TZNAME - TUPLE OF TWO STRINGS - NAME OF LOCAL NON-DST TZ - SECONDS IS LOCAL DSt TZ
print("The current timezone is {0} with an offset of {1} seconds".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight Savings Time is in effect for this location")
    print("\tThe DST Timezone is " + time.tzname[1])

print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))


# DATETIME IS A MODULE AND A CLASS
print("Print TODAY date: ", datetime.datetime.today())

print("Print NOW date:    ", datetime.datetime.now())

print("Print UTCNOW date: ", datetime.datetime.utcnow()) #CAN TAKE TZINFO

# TZINFO is an ABSTRACT BASE CLASS
# DEFINED BUT NOT IMPLEMENTED?

# INSTALL - PIP3 INSTALL PYTZ

import pytz

# INSTALL PIP3 ON LINUX - SUDO APT-GET INSTALL PYTHON3-PIP

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)

local_time = datetime.datetime.now(tz=tz_to_display)

print("The time in {} is {}".format(country, local_time))

print("The UTC time is {} ".format(datetime.datetime.utcnow()))

for x in pytz.all_timezones:
    print(x)

for y in sorted(pytz.country_names):
    print(y + ": " + pytz.country_names[y])

#for z in sorted(pytz.country_names):
#    print("{}: {}: {}".format(z, pytz.country_names[z], pytz.country_timezones[z]))

# ELIMINATES ERROR IN PREVIOUS IF MISSING TZ
for z in sorted(pytz.country_names):
    print("{}: {}: {}".format(z, pytz.country_names[z], pytz.country_timezones.get(z)))

# GO THROUGH ALL THE COUNTRY NAMES
for t in sorted(pytz.country_names):
    print("{}: {}".format(t, pytz.country_names[t], end=': '))
    if t in pytz.country_timezones:
        for n in sorted(pytz.country_timezones[t]):
            tz_to_display = pytz.timezone(n)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(n, local_time))
    else:
        print("No Timezone defined")




