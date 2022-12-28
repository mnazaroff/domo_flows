#generate_dataset_id_table.py
#==============================================================================
#generate lookup table of dataset name and ids to JSON file
#==============================================================================

import json

#domo data set name and ID mappings
data_set_name_id_dict = {   "production_scan_anal"                :   {
                                                #
                            "uploads"    :   {      "MN_API_CheckpointScans_PackageGeneric"             :   "4eec421b-b009-4d0c-8829-9eed86fd17d3",
                                                    "MN_API_CheckpointScans_PackageGlobal"              :   "8bd2e245-a6e4-402d-afb2-6c5156342f50",
                                                    "MN_API_CheckpointScans_PackageGlobal_query_log"    :   "e05fddb4-5b43-48bd-8b56-2cca5d8a480b"
                            },
                            #
                            "outputs"    :   {       ""                   :   ""},
                            #
                            "processes" :   {      ""                   :   ""} 
                    }
}

#save dataset name-id dictionary to json file
with open("dataset_id_table.json", 'w') as fp_save:
    json.dump(data_set_name_id_dict, fp_save)
