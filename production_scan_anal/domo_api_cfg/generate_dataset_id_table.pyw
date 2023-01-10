#generate_dataset_id_table.py
#==============================================================================
#generate lookup table of dataset name and ids to JSON file
#==============================================================================

import json

#domo data set name and ID mappings
data_set_name_id_dict = {   "production_scan_anal"                :   {
                                                #
                            "uploads"    :   {      "MN_API_CheckpointScans_PackageGeneric"             :   "4eec421b-b009-4d0c-8829-9eed86fd17d3",
                                                    "MN_API_CheckpointScans_PackageGlobal"              :   "1c53e13f-00c5-4ded-836e-0773c267be02",
                                                    "MN_API_CheckpointScans_PackageGlobal_query_log"    :   "12f031d0-099d-4f07-b013-92667d4937b2"
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
