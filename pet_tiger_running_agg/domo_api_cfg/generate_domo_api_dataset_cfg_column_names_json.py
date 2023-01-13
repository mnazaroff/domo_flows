#generate_domo_api_dataset_cfg_column_names_json.py
#==============================================================================
#lookup tables pairing datasets and their column names and generates it as a
#JSON file
#==============================================================================							

import json

#lookup table of dataset name and column names
column_names_dict = {    #<description>
                         "MN_API_Pet_Tiger_Running_Agg"    :   [    "ExportIdentifier",
                                                                    "Employee_Name",
                                                                    "Crew_Name",
                                                                    "Job_Name",
                                                                    "RanchCounter",
                                                                    "BlockID",
                                                                    "DateIn",
                                                                    "DateTimeIn",
                                                                    "DateTimeOut",
                                                                    "NetTime",
                                                                    "Work_Time",
                                                                    "BreakTime",
                                                                    "Wage_HR",
                                                                    "Total_Pieces",
                                                                    "Pieces_per_Hour"
                                                                ]            
}

#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_names.json", 'w') as fp_save:
    json.dump(column_names_dict, fp_save)  

