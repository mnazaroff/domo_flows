#config.py

import datetime

flag_filtered = False

#time filter settings
#-------------------------------------------------------------------------------------------    
ts_now = datetime.datetime.utcnow()                 #UTC time
ts_now_local = ts_now - datetime.timedelta(hours=8) #Pacific time

#cummulative time filter settings
#-------------------------------------------------------------------------------------------    
del_ts = datetime.timedelta(hours=1*24)               #how far back in time to grab records
filter_date_start = ts_now - del_ts                 #starting timestamp for MongoDB filter
filter_date_start_local = ts_now_local - del_ts

#real-time time filter settings
#-------------------------------------------------------------------------------------------    
# del_ts_realtime = datetime.timedelta(hours = .25)   #how far back in time to grab records
del_ts_realtime = datetime.timedelta(hours = 1*24)   #how far back in time to grab records
filter_date_start_realtime = ts_now - del_ts_realtime        #starting timestamp for MongoDB filter
filter_date_start_local_realtime = ts_now_local - del_ts_realtime

print(filter_date_start_local)
print(datetime.datetime.now())
print(filter_date_start_realtime)
print()
print()
