#download_data.py
#==============================================================================
#downloads data using the Domo API from current data flow
#==============================================================================
import json
import sys
sys.path.append("..")   #load global config located up one directory
import config_global
import config
from domo_api import domo

#caregories are the keys for a given flow name in dictionary
#data_set_name_id_dict in ./domo_api_cfg/generate_dataset_id_table.py:
#uploads, inputs, processes, and outputs
category_list = [""]
domo_sess = domo.DomoStream(domo.client_ID, domo.client_secret, domo.api_host)

for category in category_list:
    dir_dataset_download = config_global.dir_dataset_download_dict[category]
    
    with open(config.dir_domo_api_cfg + "dataset_id_table.json", 'r') as fp_open:
        dataflow_data_multi_load = json.load(fp_open)
    
    #merge multiple dataflow dataset table and id sets into a single set
    dataset_id_name_dict = {}    
    
    for dataflow_table in dataflow_data_multi_load.values():        
        for dataset_name, dataset_id in dataflow_table[category].items():
            dataset_id_name_dict[dataset_name] = dataset_id   
    
    domo_sess.DatasetDownloadMultiple(dataset_id_name_dict, dir_dataset_download)

