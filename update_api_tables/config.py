#config.py
#==============================================================================
#local configuration for this dataflow
#==============================================================================
import sys
sys.path.append("..")   #load global config located up one directory
import config_global

flag_filtered = False

#grab data filtered down to particular test parameters
if flag_filtered:    
    filename_dummy = ".csv"

#grab original data
else:
    filename_dummy = ".csv"

dir_data_inputs = config_global.dir_dataset_download_dict["inputs"]         #directory containing domo input data sets
dir_data_processes = config_global.dir_dataset_download_dict["processes"]   #directory containing domo processes data sets
dir_data_outputs = config_global.dir_dataset_download_dict["outputs"]       #directory containing domo output data sets
dir_data_uploads = config_global.dir_dataset_download_dict["uploads"]       #directory containing domo output data sets
dir_tables_lookup = config_global.dir_dataset_download_dict["tables"]       #directory containing lookup tables
dir_domo_api_cfg = "./domo_api_cfg/"                                        #directory where project domo api configurations are stored
dir_results = "./results_data/"                                             #directory where results are saved

