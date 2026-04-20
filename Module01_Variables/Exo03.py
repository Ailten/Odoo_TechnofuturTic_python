#import time
#import datetime

# (3) second format.

print("enter a number of secondes.")
input_sec = int(input())

hours = input_sec // 3600
minutes = (input_sec % 3600) // 60
sec = (input_sec % 60)


#sec = input_sec % 60
#input_sec -= sec
#
#minutes = input_sec % (60*60)  # err.
#input_sec -= minutes
#minutes //= 60
#
#hours = input_sec  # err.
#minutes //= (60*60)

print(f"time is : {hours:02d}:{minutes:0>2}:{str(sec).zfill(2)}")