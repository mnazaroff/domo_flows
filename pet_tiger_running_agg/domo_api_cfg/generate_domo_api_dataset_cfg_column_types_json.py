#generate_domo_api_dataset_cfg_column_types_json.py
#==============================================================================
#lookup tables pairing datasets and their column types and generates it as a
#JSON file
#==============================================================================							

import json
from pydomo.datasets import ColumnType

#lookup table of dataset name and column types
column_types_dict = {  #<description>
                      "pet_tiger_running_agg"   :   [   ColumnType.STRING,    #ExportIdentifier
                                                        ColumnType.STRING,    #Employee_Name
                                                        ColumnType.STRING,    #Crew_Name
                                                        ColumnType.STRING,    #Ranch_Name
                                                        ColumnType.STRING,    #Field_Name
                                                        ColumnType.DATETIME,  #DateIn
                                                        ColumnType.DATETIME,  #Start_Time
                                                        ColumnType.DATETIME,  #End_Time
                                                        ColumnType.DOUBLE,    #Wage_HR
                                                        ColumnType.DOUBLE,    #Total_Pieces
                                                        ColumnType.DOUBLE,    #Pieces_per_Hour
                                        ]

}

#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_types.json", 'w') as fp_save:
    json.dump(column_types_dict, fp_save)  

