#STORE DATE AS UTC


import time


# timedate1 = time.gmtime() #UTC
# time_est = time.localtime() #EPOCH IN SECONDS
#
#
# print(time.gmtime())
# print(time.localtime())
# print(time.time()) #Seconds from epoch
#
# print("Year:", time_est[0], time_est.tm_year)
# print("Month:", time_est[1], time_est.tm_mon)
# print("Day:", time_est[2], time_est.tm_mday)


#UNIX EPOCH - Jan 1st 1970

# TIMER
from time import time as my_timer
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

# %X - display time in locale timezone
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))

#for performance measurements
from time import perf_counter as my_perf_timer
from time import monotonic as my_mono_timer
from time import process_time as my_proc_timer





