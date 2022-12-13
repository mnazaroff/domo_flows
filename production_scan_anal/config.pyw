
#config.py
#==============================================================================
#local configuration for this dataflow
#==============================================================================
import sys
sys.path.append("..")   #load global config located up one directory
import config_global
import datetime

flag_filtered = False

#grab data filtered down to a particular test block
if flag_filtered:    
    dummy = ".csv"

#grab original data
else:     
   filename_data = ".csv"   

dir_data_inputs = config_global.dir_dataset_download_dict["inputs"]         #directory containing domo input data sets
dir_data_processes = config_global.dir_dataset_download_dict["processes"]   #directory containing domo processes data sets
dir_data_outputs = config_global.dir_dataset_download_dict["outputs"]       #directory containing domo output data sets
dir_tables_lookup = config_global.dir_dataset_download_dict["tables"]       #directory containing lookup tables
dir_domo_api_cfg = "./domo_api_cfg'"                                                    #directory where project domo api configurations are stored
dir_results = "./results_data/"                                             #directory where results are saved

# mdb_server = "docker3"
mdb_server = "10.2.150.233"
mdb_port = "27021" #as of 1*8*2020 this works but no coded boxes
# mdb_port = "27020" #as of 1*8*2020 this is not in operation

mdb_db = "PackageGeneric"       #PackageGeneric does not grab every code
mdb_collect = "PackageGeneric"  #PackageGeneric does not grab every code

#mdb_db = "PackageGlobal"       #Packageglobal is now used as of 1*19*21
#mdb_collect = "PackageGlobal"  #Packagelobal is now used as of 1*19*21

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
del_ts_realtime = datetime.timedelta(hours = .25)   #how far back in time to grab records
filter_date_start_realtime = ts_now - del_ts_realtime        #starting timestamp for MongoDB filter
filter_date_start_local_realtime = ts_now_local - del_ts_realtime

#FILE IO CONFIG
#===========================================================================================    
#file IO config
filename_checkpointMAP = f"/home/it/Documents/Programming/Python/data_anal/data/checkpoint_ID_name_map.csv"
folder_dataload = f"/home/it/Documents/Programming/Python/data_anal/"
folder_datasave = f"/home/it/Documents/Programming/Python/data_anal/data/"
filename_dataload = f"test_rows.json"

hour_day_start = 1
hour_day_stop = 19
