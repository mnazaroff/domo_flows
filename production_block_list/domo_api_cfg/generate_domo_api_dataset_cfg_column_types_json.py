#generate_domo_api_dataset_cfg_column_types_json.py
#==============================================================================
#lookup tables pairing datasets and their column types and generates it as a
#JSON file
#==============================================================================							

import json
from pydomo.datasets import ColumnType

#lookup table of dataset name and column types
column_types_dict = {  #<description>
                      "MN_API_production_block_list"    :   [   ColumnType.DATETIME,    #StartTime
                                                                ColumnType.DATETIME,    #StopTime
                                                                ColumnType.STRING,      #BlockID
                                                                ColumnType.STRING,      #BlockName
                                                                ColumnType.STRING,      #CommodityName
                                                                ColumnType.STRING,      #CommodityNameLong
                                                                ColumnType.STRING,      #VarietyName
                                                                ColumnType.STRING,      #VarietyNameLong
                                                                ColumnType.DOUBLE,      #SecondsSince
                                                                ColumnType.DOUBLE       #ActiveSS
                                        ]

}

#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_types.json", 'w') as fp_save:
    json.dump(column_types_dict, fp_save)  

