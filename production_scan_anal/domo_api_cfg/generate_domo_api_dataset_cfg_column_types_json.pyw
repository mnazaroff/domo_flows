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
                                                                ],
                      "MN_API_CheckpointScans_PackageGlobal"            :   [   ColumnType.STRING,      #_id
                                                                                ColumnType.STRING,      #PK
                                                                                ColumnType.STRING,      #Code
                                                                                ColumnType.STRING,      #BlockID
                                                                                ColumnType.LONG,        #CheckpointID
                                                                                ColumnType.DATETIME,    #DateCreate
                                                                                ColumnType.STRING,      #ProductComposite
                                                                                ColumnType.LONG,        #ProductID
                                                                                ColumnType.STRING,      #Size
                                                                                ColumnType.STRING,      #Style
                                                                                ColumnType.STRING,      #Content
                                                                                ColumnType.LONG,        #OriginCheckpointID
                                                                                ColumnType.STRING,      #PrintSize
                                                                                ColumnType.LONG,        #FruitCount
                                                                                ColumnType.DOUBLE,      #CheckweigherResultAvg
                                                                                ColumnType.DOUBLE,      #TareWeight
                                                                                ColumnType.DOUBLE,      #NetWeight
                                                                                ColumnType.STRING,      #DataMatrixExists
                                                                                ColumnType.STRING,      #PTIExists
                                                                                ColumnType.STRING       #ProductName
                                                                            ],
                      "MN_API_CheckpointScans_PackageGlobal_query_log"  :   [   ColumnType.DATETIME,    #DateTime_start
                                                                                ColumnType.DATETIME,    #DateTime_stop
                                                                                ColumnType.DATETIME,    #DateTime_query
                                                                                ColumnType.DOUBLE,      #duration_proc_mins
                                                                                ColumnType.LONG,        #count_read
                                                                                ColumnType.LONG,        #count_success
                                                                                ColumnType.DOUBLE,      #ratio_success  
                                                                            ]

}

#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_types.json", 'w') as fp_save:
    json.dump(column_types_dict, fp_save)
