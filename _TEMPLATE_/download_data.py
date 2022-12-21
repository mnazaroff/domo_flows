#download_data.py
#==============================================================================
#downloads data using the Domo API from current data flow
#==============================================================================
import json
import sys
sys.path.append("..")   #load global config located up one directory
import config_global
import config
from domo_api import domo_api_config

category_list = ["category"]

for category in category_list:
    dir_dataset_download = config_global.dir_dataset_download_dict[category]
    
    with open(config.dir_domo_api_cfg + "dataset_id_table.json", 'r') as fp_open:
        dataflow_data_multi_load = json.load(fp_open)
    
    #merge multiple dataflow dataset table and id sets into a single set
    dataset_id_name_dict = {}
    
    
    for dataflow_table in dataflow_data_multi_load.values():        
        for dataset_name, dataset_id in dataflow_table[category].items():
            dataset_id_name_dict[dataset_name] = dataset_id
    
    domo_sess = domo_api_config.DomoStream(domo_api_config.client_ID, domo_api_config.client_secret, domo_api_config.api_host)        
    domo_sess.DatasetDownloadMultiple(dataset_id_name_dict, dir_dataset_download)

