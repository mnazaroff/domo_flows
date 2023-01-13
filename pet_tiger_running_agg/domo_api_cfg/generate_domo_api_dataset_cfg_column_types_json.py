#generate_domo_api_dataset_cfg_column_types_json.py
#==============================================================================
#lookup tables pairing datasets and their column types and generates it as a
#JSON file
#==============================================================================							

import json
from pydomo.datasets import ColumnType

#lookup table of dataset name and column types
column_types_dict = {  #<description>
                      "MN_API_Pet_Tiger_Running_Agg"   :   [    ColumnType.STRING,      #ExportIdentifier
                                                                ColumnType.STRING,      #Employee_Name
                                                                ColumnType.STRING,      #Crew_Name
                                                                ColumnType.STRING,      #Job_Name

                                                                ColumnType.LONG,        #RanchCounter
                                                                ColumnType.STRING,      #BlockID

                                                                ColumnType.STRING,      #DateIn
                                                                ColumnType.DATETIME,    #DateTimeIn
                                                                ColumnType.DATETIME,    #DateTimeOut
                                                                ColumnType.DOUBLE,      #NetTime
                                                                ColumnType.DOUBLE,      #Work_Time
                                                                ColumnType.DOUBLE,      #BreakTime

                                                                #ColumnType.STRING,     #Start_Time
                                                                #ColumnType.STRING,     #End_Time

                                                                ColumnType.DOUBLE,      #Wage_HR
                                                                ColumnType.DOUBLE,      #Total_Pieces
                                                                ColumnType.DOUBLE       #Pieces_per_Hour
                                                            ]

}

#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_types.json", 'w') as fp_save:
    json.dump(column_types_dict, fp_save)  

