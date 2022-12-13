#mpc_qa_ppi_carton_weight.py
#==============================================================================
#queries QA PPI Carton Weight SQL data and streams it to a Domo cloud data set
#==============================================================================

import pyodbc
import pandas as pd
from domo_api import domo
from domo_api import domo_api_dataset_id_table

def main():
    try:
        #grab SQL data
        print("grabbing MPC QA PPI carton weight SQL data...")
        cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER=10.0.1.5;DATABASE=Moonlight;UID=sa;PWD=1!rofl$1")
        cursor=cnxn.cursor()
        
        query = """
        SELECT
                *, 
                TRY_CAST(Weight AS MONEY) 	AS	WeightNumeric

        FROM
                VW_PPI_Carton_Weight

        WHERE
                YEAR(ControlDate) >= 2022
        """

        DF_sql = pd.read_sql(query, cnxn)
        print(DF_sql)

        filename_save = "C:\\Users\\Administrator\\Documents\\Python\\data_pull\\mpc_qa_ppi_carton_weight.csv"
        DF_sql.to_csv(filename_save, index=False)
        print("data saved to {0}".format(filename_save))
        print("mpc_qa_ppi_carton_weight_sql_pull SQL data grab successful")

        #stream SQL data to Domo data set storage
        print("streaming data to domo...")
        domo_sess = domo.DomoStream(domo.client_ID, domo.client_secret, domo.api_host)
        dataset_name = "MPC_QA_PPI_Carton_Weight"        
        print("uploading {0}...".format(dataset_name))        
        result = domo_sess.DatasetReplaceCSV( domo_api_dataset_id_table.data_set_name_id_dict[dataset_name], filename_save)
        print(result)
        
    except Exception as e:
        template = "An exception oftype {0} occurred arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print(message)

if __name__ == "__main__":
    main()
