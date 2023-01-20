#production_block_list.py
#==============================================================================
#queries production block counts JSON data and streams it to a Domo cloud data
#set
#==============================================================================

import requests
import json
import pandas as pd
import sys
sys.path.append("..")   #load global config located up one directory
import config_global
from domo_api import domo

def main():
    try:        
        project_name = "production_block_list"
        dataset_name = "MN_API_production_block_list"    
        filename_save = config_global.dir_dataset_download_dict["uploads"] + dataset_name + ".csv"    
        filename_dataset_cfg = "./domo_api_cfg/dataset_id_table.json"
        
        #grab JSON data
        print("grabbing production_block_list JSON data...")
        
        url = "https://io.moonlightcompanies.com/Production_Block_List?Token=3E4C792C-E6EC-489D-AEC0-174E057B9DFA"
        resp = requests.get(url=url)
        data = resp.json()
        DF_json = pd.DataFrame(data)

        if "StopTime" not in DF_json:
            print("StopTime not found in JSON grab. Inserting dummy col instead...")
            DF_json.insert(1, "StopTime", None)

        filename_save = "C:\\Users\\Administrator\\Documents\\Python\\data_pull\\production_bag_total_count_per_shift.csv" 
        DF_json.to_csv(filename_save, index=False)
        print("production_block_list JSON data grab successful")
        print("data saved to {0}".format(filename_save))

        #stream JSON data to Domo data set storage        
        #load data set column type configuration from JSON file
        with open(filename_dataset_cfg, 'r') as fp_open:
            dataset_id_table_dict = json.load( fp_open) 

        dataset_id = dataset_id_table_dict[project_name]["uploads"][dataset_name]

        print("streaming data to domo...")
        domo_sess = domo.DomoStream(domo.client_ID, domo.client_secret, domo.api_host)
        
        print("uploading {0}...".format(dataset_name))        
        result = domo_sess.DatasetReplaceCSV( dataset_id, filename_save)
        print(result)

    except Exception as e:
        template = "An exception oftype {0} occurred arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print(message)
        
if __name__ == "__main__":
    main()
