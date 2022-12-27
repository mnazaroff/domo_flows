#generate_domo_api_dataset_cfg_column_types_json.py
#==============================================================================
#lookup tables pairing datasets and their column types and generates it as a
#JSON file
#==============================================================================							

import json
from pydomo.datasets import ColumnType

#lookup table of dataset name and column types
column_types_dict = {  #<description>
                      ""            :   [   ColumnType.LONG,      #col_name                                             
                                            ColumnType.DOUBLE,    #col_name
                                            ColumnType.STRING,    #col_namecol_name
                                            ColumnType.DATETIME   #col_name
                                        ]

}

#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_types.json", 'w') as fp_save:
    json.dump(column_types_dict, fp_save)  

