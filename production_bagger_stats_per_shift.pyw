#production_bagger_stats_per_shift.py
#==============================================================================
#queries production bag count stats per shift JSON data and streams it to a
#Domo cloud data set
#==============================================================================

import requests
import pandas as pd
from domo_api import domo
from domo_api import domo_api_dataset_id_table

def main():
    try:
        #grab JSON data
        print("grabbing bagger_stats_per_shift JSON data...")
    
        url = 'https://io.moonlightcompanies.com/Bagger_Stats_Per_Shift?Token=CAB160DD-55C1-4AA9-9E28-2DBC55E91C2A'
        resp = requests.get(url=url)
        data = resp.json()
        DF_json = pd.DataFrame(data)

        filename_save = "C:\\Users\\Administrator\\Documents\\Python\\data_pull\\production_bagger_stats_per_shift.csv"
        DF_json.to_csv(filename_save, index=False)
        print("data saved to {0}".format(filename_save))
        print("bagger_stats_per_shift_json_pull JSON data grab successful")

        #stream JSON data to Domo data set storage
        print("streaming data to domo...")
        domo_sess = domo.DomoStream(domo.client_ID, domo.client_secret, domo.api_host)
        dataset_name = "Production Bagger Stats Per Shift"        
        print("uploading {0}...".format(dataset_name))        
        result = domo_sess.DatasetReplaceCSV( domo_api_dataset_id_table.data_set_name_id_dict[dataset_name], filename_save)
        print(result)
        
    except Exception as e:
        template = "An exception oftype {0} occurred arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print(message)
        
if __name__ == "__main__":
    main()
