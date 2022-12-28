#generate_domo_api_dataset_cfg_column_names_json.py
#==============================================================================
#lookup tables pairing datasets and their column names and generates it as a
#JSON file
#==============================================================================							

import json

#lookup table of dataset name and column names
column_names_dict = {    #<description>
                         "MN_API_checkpoint_list"      :   [    "ID",
                                                                "CheckpointID",
                                                                "LocationName",
                                                                "FarScanCheckpointID",
                                                                "ParentID",
                                                                "ParentLocationName",
                                                                "ParentRemoteID",
                                                                "ParentProcessIsEnabled",
                                                                "ParentProcessIsOnline",
                                                                "PluginClassName",
                                                                "RemoteID",
                                                                "IsVisible",
                                                                "DisplayName",
                                                                "Role",
                                                                "HasDebugInfo",
                                                                "RequireExplicitRouting",
                                                                "ProcessIsEnabled",
                                                                "ProcessIsOnline",
                                                                "ProcessIsRouteBlocked",
                                                                "RouteWeight",
                                                                "UISide",
                                                                "Size",
                                                                "OutletStatus"
                                                        ]        
}



#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_names.json", 'w') as fp_save:
    json.dump(column_names_dict, fp_save)  

