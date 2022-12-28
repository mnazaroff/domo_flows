#generate_domo_api_dataset_cfg_column_types_json.py
#==============================================================================
#lookup tables pairing datasets and their column types and generates it as a
#JSON file
#==============================================================================							

import json
from pydomo.datasets import ColumnType

#lookup table of dataset name and column types
column_types_dict = {  #<description>
                      "MN_API_checkpoint_list"      :   [   ColumnType.LONG,        #ID
                                                            ColumnType.LONG,        #CheckpointID
                                                            ColumnType.STRING,      #LocationName
                                                            ColumnType.LONG,        #FarScanCheckpointID
                                                            ColumnType.LONG,        #ParentID
                                                            ColumnType.STRING,      #ParentLocationName
                                                            ColumnType.LONG,        #ParentRemoteID
                                                            ColumnType.LONG,        #ParentProcessIsEnabled
                                                            ColumnType.LONG,        #ParentProcessIsOnline
                                                            ColumnType.STRING,      #PluginClassName
                                                            ColumnType.STRING,      #RemoteID
                                                            ColumnType.LONG,        #IsVisible
                                                            ColumnType.STRING,      #DisplayName
                                                            ColumnType.STRING,      #Role
                                                            ColumnType.LONG,        #HasDebugInfo
                                                            ColumnType.LONG,        #RequireExplicitRouting
                                                            ColumnType.LONG,        #ProcessIsEnabled
                                                            ColumnType.LONG,        #ProcessIsOnline
                                                            ColumnType.LONG,        #ProcessIsRouteBlocked
                                                            ColumnType.DOUBLE,      #RouteWeight
                                                            ColumnType.STRING,      #UISide
                                                            ColumnType.STRING,      #Size
                                                            ColumnType.STRING,      #OutletStatus
                                                        ]
}

#save dataset name-id dictionary to json file
with open("domo_api_dataset_cfg_column_types.json", 'w') as fp_save:
    json.dump(column_types_dict, fp_save)
