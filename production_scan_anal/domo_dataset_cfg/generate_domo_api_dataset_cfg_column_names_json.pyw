#generate_domo_api_dataset_cfg_column_names_json.py
#==============================================================================
#lookup tables pairing datasets and their column names and generates it as a
#JSON file
#==============================================================================							

import json

#lookup table of dataset name and column names
column_names_dict = {    #<description>
                         "MN_API_CheckpointScans_PackageGeneric"            :   [    "_id",
                                                                                     "BlockID",
                                                                                  #   "Checkpoints",
                                                                                     "CheckweigherResultAvg",
                                                                                     "DateCreate",
                                                                                     "OriginCheckpointID",
                                                                                     "ProductComposite",
                                                                                     "ProductID",
                                                                                     "Size",
                                                                                     "Style",
                                                                                     "Content"
                                                                                ]
}



#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_names.json", 'w') as fp_save:
    json.dump(column_names_dict, fp_save)  
