#generate_domo_api_dataset_cfg_column_types_json.py
#==============================================================================
#lookup tables pairing datasets and their column types and generates it as a
#JSON file
#==============================================================================							

import json
from pydomo.datasets import ColumnType

#lookup table of dataset name and column types
column_types_dict = {  #<description>
                      "MN_API_CheckpointScans_PackageGeneric"            :   [  ColumnType.STRING,      #_id
                                                                                ColumnType.STRING,      #BlockID
                                                                              #  ColumnType.LONG,        #Checkpoints
                                                                                ColumnType.DOUBLE,      #CheckweigherResultAvg
                                                                                ColumnType.DATETIME,    #DateCreate
                                                                                ColumnType.LONG,        #OriginCheckpointID
                                                                                ColumnType.STRING,      #ProductComposite
                                                                                ColumnType.LONG,        #ProductID
                                                                                ColumnType.STRING,      #Size
                                                                                ColumnType.STRING,      #Style
                                                                                ColumnType.STRING       #Content
                                                                            ]

}

#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_types.json", 'w') as fp_save:
    json.dump(column_types_dict, fp_save)
