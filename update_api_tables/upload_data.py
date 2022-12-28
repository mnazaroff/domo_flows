#upload_data.py
#==============================================================================
#uploads data using the Domo API
#==============================================================================
import sys
sys.path.append("..")   #load global config located up one directory
import config_global
from domo_api import domo
import json

dir_dataset_upload = config_global.dir_dataset_download_dict["uploads"]

test_dataset_name_list = ["table_test_block_master_v2", "table_test_daily_projection", "table_test_dyn_helper_abc", "table_test_mpc_projections", "table_test_std_util_source_data"]
domo_sess = domo.DomoStream(domo.client_ID, domo.client_secret, domo.api_host)

#load data set column type configuration from JSON file
with open(config.dir_domo_api_cfg + "dataset_id_table.json", 'r') as fp_open:
    dataset_id_table_dict = json.load( fp_open)

for dataset_name in test_dataset_name_list:
    
    filename_upload = dir_dataset_upload + test_dataset_name + ".csv"
    dataset_id = dataset_id_table_dict[test_dataset_name]["uploads"][test_dataset_name]
 
    result = domo_sess.DatasetReplaceCSV( dataset_id, filename_upload)
    print(result)
    print("{0} uploaded to domo\n".format( test_dataset_name))
