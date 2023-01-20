#domo_send_datasets.py
#==============================================================================
#create Domo API dataset
#==============================================================================
import domo
#import domo_api_dataset_cfg_table
import json
import sys
sys.path.append("..")   #load global config located up one directory
import config_global
from pydomo.datasets import ColumnType

def main():   
    try:
        
        project_name = "production_block_list"
        dataset_name = "MN_API_production_block_list"

        dir_project_domo_cfg = config_global.dir_project_root + project_name + "/domo_api_cfg/"

        filename_dataset_cfg_column_names = dir_project_domo_cfg + "domo_api_dataset_cfg_column_names.json"
        filename_dataset_cfg_column_types = dir_project_domo_cfg + "domo_api_dataset_cfg_column_types.json"

        #load data set column name configuration from JSON file
        with open(filename_dataset_cfg_column_names, 'r') as fp_open:
            dataset_cfg_colum_names_dict = json.load( fp_open)

        #load data set column type configuration from JSON file
        with open(filename_dataset_cfg_column_types, 'r') as fp_open:
            dataset_cfg_colum_types_dict = json.load( fp_open)


        dataset_cfg_column_names = dataset_cfg_colum_names_dict[dataset_name]
        
        #the column type prefix "ColumnType." is currently getting lost in the JSON translation so this is a workaround
        dataset_cfg_colum_types = []
        json_columntype_mapper_dict = { "STRING" : ColumnType.STRING, 
                                        "DATE" : ColumnType.DATE,
                                        "DATETIME" : ColumnType.DATETIME,
                                        "LONG" : ColumnType.LONG,
                                        "DOUBLE" : ColumnType.DOUBLE
                                        }
        
        for column_type_suffix in dataset_cfg_colum_types_dict[dataset_name]:                                                                                                
           dataset_cfg_colum_types.append(json_columntype_mapper_dict[column_type_suffix])
           
        
        domo_sess = domo.DomoStream(domo.client_ID, domo.client_secret, domo.api_host)
        domo_sess.DatasetCreate(dataset_name, dataset_cfg_colum_types, dataset_cfg_column_names)            
        
        
    except Exception as e:
        template = "An exception oftype {0} occurred arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print(message)
               
if __name__ == "__main__":
    main()


