#domo_etl_library.py
##commonly used Python code in Domo ETL flows
import pandas as pd

#appends new rows to an existing table based on existing keys
def append_checked(DF_new, DF_hist, constraint_list, constraint_flag = "Existing"):
    DF_hist_checked = DF_hist[constraint_list].copy()
    DF_hist_checked.drop_duplicates(inplace=True)
    DF_hist_checked[constraint_flag] = True
    
    DF_new_check_checked = pd.merge(DF_new, DF_hist_checked,
                   left_on = constraint_list,
                   right_on = constraint_list,
                   how="left").copy()

    DF_new_check_checked = DF_new_check_checked[pd.isna(DF_new_check_checked[constraint_flag])]

    return pd.concat([DF_hist, DF_new_check_checked.drop(labels=[constraint_flag], axis=1)])
    
    
#filter dataframe using date column to be within given months ago
def filter_date_min_months(DF, col_date, del_months_filter):
    DF[col_date] = pd.to_datetime(DF[col_date])
    filter_date = pd.to_datetime("now") - pd.DateOffset(months=del_months_filter)
    
    return DF[ DF[col_date] >= filter_date ]

#convert timestamp day to Moonlight day
def GetMoonlightDay(timestamp):
  #moonlight days are from 600 hrs to 600 hrs
  if timestamp.hour<6:
    timestamp = timestamp - pd.Timedelta(hours=24)

  return timestamp.date()

#merge MoonlightDate and Hour into single datetime
def GetMoonlightDayHour(date, hour):
  
  print("{0} ({1})".format(date, type(date)))
  print("{0} ({1})".format(hour, type(hour)))
  
  if(hour<10):
    hour_str = "0" + str(hour)
  else:
    hour_str = str(hour)
  
  return pd.to_datetime( str(date).replace('-','') + hour_str + "0000", format='%Y%m%d%H%M%S' ) 

#get shift from hour
def GetShiftFromTimestamp(timestamp):
  hour_day_start = 6	#day shift start hour(inclusive)
  hour_day_stop = 17	#day shift stop hour(inclusive)
  
  if timestamp.hour in range(hour_day_start, hour_day_stop + 1):
    return "Day"
  else:
    return "Night"
