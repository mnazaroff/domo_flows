
import config
import traceback
import json
import pandas as pd
import sys
sys.path.append("..")   #load global config located up one directory
import config_global
from domo_api import domo

try:    
    project_name = "production_scan_anal"
    dataset_name = "MN_API_CheckpointScans_PackageGeneric"    
    filename_save = config_global.dir_dataset_download_dict["uploads"]   + dataset_name + ".csv"
    filename_dataset_cfg = "./domo_api_cfg/dataset_id_table.json"
        
    
    
    #upload data to Domo
    #load data set column type configuration from JSON file
    with open(filename_dataset_cfg, 'r') as fp_open:
        dataset_id_table_dict = json.load( fp_open)
    
    dataset_id = dataset_id_table_dict[project_name]["uploads"][dataset_name]
    
   
except Exception as e:            
    if "Error uploading DataSet" in e.args[0]:        
        print("unable to upload file {0} to {1}".format(filename, api_table))
    input=("press any key to exit...")
