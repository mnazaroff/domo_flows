
import config
import traceback
import json
import pandas as pd
import sys
sys.path.append("..")   #load global config located up one directory
import config_global
import API
from domo_api import domo

try:    
    project_name = "update_api_tables"
    dataset_name = "MN_API_checkpoint_list"    
    filename_save = config_global.dir_dataset_download_dict["uploads"]   + dataset_name + ".csv"
    filename_dataset_cfg = "./domo_api_cfg/dataset_id_table.json"

    domo_sess = domo.DomoStream(domo.client_ID, domo.client_secret, domo.api_host)
            
##    DF_p_table = pd.DataFrame(API.Invoke("Product_List"))[["ID", "ProductName"]].rename(columns={"ID" : "ProductID"})
    DF_cp_table = pd.DataFrame(API.Invoke("Checkpoint_List"))
    DF_cp_table.to_csv(filename_save,index=False)
##    #upload data to Domo
    print("filename_save")
    #load data set column type configuration from JSON file
    with open(filename_dataset_cfg, 'r') as fp_open:
        dataset_id_table_dict = json.load( fp_open)
    
    dataset_id = dataset_id_table_dict[project_name]["uploads"][dataset_name]    
    print("test2")
    result = domo_sess.DatasetReplaceCSV( dataset_id, filename_save)
    print(result)
    print("{0} uploaded to domo\n".format( filename_save))
   
except Exception as e:            
    if "Error uploading DataSet" in e.args[0]:        
        print("unable to upload file {0} to {1}".format(filename, api_table))
    else:
        print(e)
