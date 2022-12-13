
import config
import pymongo
import sys
import traceback
import MongoDBUtils
import json
import pandas as pd
import datetime
import sys
sys.path.append("..")   #load global config located up one directory
import utils
import config_global
from domo_api import domo

try:
    mdb_db = "PackageGeneric"
    mdb_collect = "PackageGeneric"
    project_name = "production_scan_anal"
    dataset_name = "MN_API_CheckpointScans_PackageGeneric"    
    filename_save = config_global.dir_dataset_download_dict["uploads"]   + dataset_name + ".csv"
    filename_dataset_cfg = "./domo_dataset_cfg/dataset_id_table.json"
        
    print("real-time data process")
    domo_sess = domo.DomoStream(domo.client_ID, domo.client_secret, domo.api_host)  
    
    ts_proc_start = datetime.datetime.now()
    utils.print_hr()
    print(ts_proc_start)
    print("connecting to {0}:{1}".format(config.mdb_server, config.mdb_port))
    mongo_client = pymongo.MongoClient(config.mdb_server + ":" + config.mdb_port)        
    resp = mongo_client.list_database_names()
    
    print("database names:")
    print(resp)
    utils.print_hr("-")
      
    print("using database {0}".format(mdb_db))        
    mongo_db = mongo_client[mdb_db] 
    print(type(mongo_db))
    
    print("using collection {0}".format(mdb_collect))
    mongo_collect = mongo_db[mdb_collect]
    print(mongo_collect)            
    
    docs = mongo_collect.find({ 'DateCreate': { '$gt': config.filter_date_start } })      
    table_dicts = MongoDBUtils.docs_to_table_package_generic_monolithic(docs)
    
    DF_package_generic = pd.DataFrame(table_dicts)
    print(DF_package_generic[["_id", "DateCreate"]])
##    print(DF_package_generic[["_id", "DateCreate","CheckWeigherResultAvg"]])
##    DF_package_generic.to_csv(filename_save, index=False)
##    print("data saved to:\n{0}".format(filename_save))
##    
##    #upload data to Domo
##    #load data set column type configuration from JSON file
##    with open(filename_dataset_cfg, 'r') as fp_open:
##        dataset_id_table_dict = json.load( fp_open)
##    
##    dataset_id = dataset_id_table_dict[project_name]["uploads"][dataset_name]
##    
##    result = domo_sess.DatasetReplaceCSV( dataset_id, filename_save)
##    print(result)
##    print("{0} uploaded to domo\n".format( filename_save))
##    
##    #grab timestamps of when script started and how far back in time we went    
##    ts_o = config.filter_date_start_local
##    ts_f = datetime.datetime.now()
##    print("MongoDB timestamp start: {0}".format(ts_o))
##    print("MongoDB timestamp stop:  {0}".format(ts_f))
##    
##    date_o = str(ts_o.year) + "-" + str(ts_o.month) + "-" + str(ts_o.day)
##    date_f = str(ts_f.year) + "-" + str(ts_f.month) + "-" + str(ts_f.day)
##    
##    print("elapsed processing time: {:.2f} minutes".format( (datetime.datetime.now() - ts_proc_start ).seconds/60 ))


except Exception as e:            
    if "Error uploading DataSet" in e.args[0]:        
        print("unable to upload file {0} to {1}".format(filename, api_table))
    input=("press any key to exit...")
