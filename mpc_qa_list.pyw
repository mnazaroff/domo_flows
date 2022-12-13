#mpc_qa_list.py
#==============================================================================
#queries QA List JSON data and streams it to a Domo cloud data set
#==============================================================================

import requests
import pandas as pd
from domo_api import domo
from domo_api import domo_api_dataset_id_table

def main():
    try:
        #grab JSON data
        print("grabbing QA list test JSON data...")
        
        #url = 'https://system.moonlightcompanies.com/api/control/list.page.lite?PageSize=30000' #minimal version
        url = "https://system.moonlightcompanies.com/api/control/list.page?PageSize=30000" #maximum version
        
        resp = requests.get(url=url)
        data = resp.json()
        DF_json = pd.DataFrame(data)

        DF_json["ControlID"] = DF_json["data"].apply(lambda x: x["ControlID"])
        DF_json["ControlDate"] = DF_json["data"].apply(lambda x: pd.to_datetime(x["ControlDate"]["date"]).tz_localize(x["ControlDate"]["timezone"])).dt.tz_convert("UTC")    
        DF_json["GaBlockId" ] = DF_json["data"].apply(lambda x:  x["GaBlockId"])
        DF_json["Screen"] = DF_json["data"].apply(lambda x: x["Screen"])
        DF_json["Size"] = DF_json["data"].apply(lambda x: x["Size"])
        DF_json["PackStyle" ] = DF_json["data"].apply(lambda x: x["PackStyle"])
        DF_json["Url"] = DF_json["data"].apply(lambda x: x["Url"])

        DF_json.drop(labels=["draw", "recordsTotal", "recordsFiltered", "data"], axis=1, inplace=True)

        filename_save = "C:\\Users\\Administrator\\Documents\\Python\\data_pull\\mpc_qa_list.csv"
        DF_json.to_csv(filename_save, index=False)
        print("QA list test JSON data grab successful")

        #stream JSON data to Domo data set storage
        print("streaming data to domo...")
        domo_sess = domo.DomoStream(domo.client_ID, domo.client_secret, domo.api_host)
        dataset_name = "MPC QA List"        
        print("uploading {0}...".format(dataset_name))        
        result = domo_sess.DatasetReplaceCSV( domo_api_dataset_id_table.data_set_name_id_dict[dataset_name], filename_save)
        print(result)
        
    except Exception as e:
        template = "An exception oftype {0} occurred arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print(message)
    
if __name__ == "__main__":
    main()
