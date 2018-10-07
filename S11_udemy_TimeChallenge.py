# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.


import random
import time as time

from time import time as my_timer


#my_timer = time.time()

input("Press enter to start timer:")
start_timer = time.time()
start_perf_timer = time.perf_counter()
start_mono_timer = time.monotonic()
start_proc_timer = time.process_time()

time.sleep(random.randint(1, 6))

input("Press enter to stop timer:")
stop_timer = time.time()
stop_perf_timer = time.perf_counter()
stop_mono_timer = time.monotonic()
stop_proc_timer = time.process_time()

print("\n\nDifference between start and end time for time() function is: {}".format(stop_timer - start_timer))
print("Difference between start and end time for perf() function is: {}".format(stop_perf_timer - start_perf_timer))
print("Difference between start and end time for mono() function is: {}".format(stop_mono_timer - start_mono_timer))
print("Difference between start and end time for proc() function is: {}".format(stop_proc_timer - start_proc_timer))

print("\n\ntime()\t\t\t", time.get_clock_info('time'))
print("perf_counter()\t", time.get_clock_info('perf_counter'))
print("monotonic()\t\t", time.get_clock_info('monotonic'))
print("process_time()\t", time.get_clock_info('process_time'))

