#generate_domo_api_dataset_cfg_column_names_json.py
#==============================================================================
#lookup tables pairing datasets and their column names and generates it as a
#JSON file
#==============================================================================							

import json

#lookup table of dataset name and column names
column_names_dict = {    #<description>
                         "pet_tiger_running_agg"    :   [   "ExportIdentifier",
                                                            "Employee_Name",
                                                            "Crew_Name",
                                                            "Ranch_Name",
                                                            "Field_Name",
                                                            "DateIn",
                                                            "Start_Time",
                                                            "End_Time",
                                                            "Wage_HR",
                                                            "Total_Pieces",
                                                            "Pieces_per_Hour"
                                                        ]            
}

#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_names.json", 'w') as fp_save:
    json.dump(column_names_dict, fp_save)  

