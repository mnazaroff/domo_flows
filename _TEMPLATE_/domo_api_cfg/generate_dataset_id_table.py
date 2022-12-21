#generate_dataset_id_table.py
#==============================================================================
#generate lookup table of dataset name and ids to JSON file
#==============================================================================

import json

#domo data set name and ID mappings
data_set_name_id_dict = {   "flow_name"                :   {
                                                #
                            "uploads"    :   {       ""                   :   ""
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

