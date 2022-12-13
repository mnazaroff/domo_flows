#config_global.py
#==============================================================================
#configuration file containing parameters used throughout all files
#==============================================================================

dir_project_root = "C:/Users/Administrator/Documents/Python/domo_flows/"   #root directory containing domo api project folders

dir_dataset_root = "C:/Users/Administrator/Documents/Python/domo_flows/"       #root directory for downloaded data
dir_dataset_test = dir_dataset_root + "datasets/"                                      #directory for test data

#directories where data sets downloaded using Domo API are saved
dir_dataset_download_dict = { "inputs"      :   dir_dataset_test + "inputs/",           #directory for input test data
                              "processes"   :   dir_dataset_test + "processes/",        #directory for process test data
                              "outputs"     :   dir_dataset_test + "outputs/",          #directory for output test data
                              "tables"      :   dir_dataset_test + "tables/",           #directory for lookup table test data
                              "uploads"     :   dir_dataset_test + "uploads/"           #directory for upload test data
                             }
#directories where sourcing files uploaded using Domo API are saved
dir_dataset_upload = dir_dataset_test + "uploads/"

