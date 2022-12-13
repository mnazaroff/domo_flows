#domo.py
#==============================================================================
#domo API configuration file and setup
#==============================================================================
import logging
from pydomo import Domo
from pydomo.datasets import Column, DataSetRequest, Schema, Sorting#, ColumnType
from pydomo.streams import  UpdateMethod#, CreateStreamRequest

#would be better to separate API details and class definition
client_ID = "7a67595d-2fec-4e79-820f-5492878da054"
client_secret = "5ce9816431da53199fbabd98a0f368605a7d9d66b203fc8a96744b1557bc027c"
scope = "data"
api_host = "api.domo.com"
user_ID = 545469307

#DOMO streaming interface
'''
suggested change to use local variables to store results to save time with
repeatedly used functions
'''
class DomoStream:
    #constructor
    def __init__(self, client_ID = client_ID, client_secret = client_secret, hostname = api_host):
        self.domo = self.init_domo_client(client_ID, client_secret, hostname)
        self.datasets = self.domo.datasets
    
    #constructor
    def init_domo_client(self, clientID, clientSecret, hostname, **kwargs):
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logging.getLogger().addHandler(handler)    
        
        return Domo(clientID, clientSecret, logger_name = "foo", log_level = logging.INFO, api_host=hostname, **kwargs)
    
    #append to given dataset data loaded from CSV file        
    def DatasetAppendCSV(self, datasetID, filename):        
        result = self.datasets.data_import_from_file(datasetID, filename, update_method=UpdateMethod.APPEND)                          
        print(result)    
    
    #create new dataset for given name and schema
    def DatasetCreate(self, dataset_name, column_types, column_names):
    
        #check if data set name already exists
        if(  self.DatasetFind(dataset_name, sort_find=True)):
            print("data set {0} already exists".format(dataset_name))
            return
        
        dsr = DataSetRequest()        
        dsr.name = dataset_name
        schema_list = []
        for column_type, column_name in zip(column_types, column_names):
            schema_list.append( Column(column_type, column_name) )
        dsr.schema = Schema(schema_list)
   
        #create dataset with given schema
        dataset = self.datasets.create(dsr)
        self.domo.logger.info("created dataset " + dataset["id"])
    
    #return sorted or unsorted list of dataset names stored in Domo
    def DatasetGetList(self, sort=False):    
        if sort:
            return list(self.datasets.list(sort=Sorting.NAME))
        return list(self.datasets.list())
    
    #download given dataset as a CSV file
    def DatasetDownload(self, datasetID, filename_download="domo_dataset_download.csv", flag_include_csv_header=True, verbose=False):
        file_download = self.datasets.data_export_to_file(datasetID, filename_download, flag_include_csv_header)
        
        if(verbose):
            print("dataset id {0} saved to:\n{1}\n".format(datasetID, filename_download))
        
        file_download.close()
    
    #downloads multiple datasets identified by dataset name and id
    def DatasetDownloadMultiple(self, dataset_name_id_dict, directory_download, verbose=False):    
       
        for dataset_name, dataset_id in dataset_name_id_dict.items():
            
            if(verbose):
                print("processing dataset {0}...".format(dataset_name))
                
            self.DatasetDownload(dataset_id, directory_download + dataset_name + ".csv", verbose=verbose)
    
    def DatasetLookup(self, datasetID):
        download = self.datasets.data_export(dataset_id = datasetID, include_csv_header = True)
        print(download)
        print(type(download))
    
    #download datsets associated with a dataflow speicifed by category(input, processes, output, or table)
    #this is an incomplete work in progress
    def DataflowDownload(self, flow_dataset_dict, category, directory_download):        
        for flow_table in flow_dataset_dict.values():
            for dataset_name, dataset_id in flow_table[category].items():
                print(dataset_name)
                print(dataset_id)
            
    #replace dataset with data loaded from CSV file
    def DatasetReplaceCSV(self, datasetID, filename):
        print("DatasetReplaceCSV filename:\n{0}".format(filename))
        result = self.datasets.data_import_from_file(datasetID, filename, update_method=UpdateMethod.REPLACE)
        print(result)

    #searches for a data set and returns flag indicating whether or not data set exists
    def DatasetFind(self, dataset_name, sort_find=False):
        print("getting dataset list...")
        datasets_list = self.DatasetGetList(sort=sort_find)
        print("parsing dataset list...")        
        
        for dataset in datasets_list:
            if dataset["name"]==dataset_name:
                return True #flag data set exists
        
        return False    #flag data set does not exist
    
#for testing purposes
def main():
    print()
    test = DomoStream()
    
    
if __name__ == "__main__":
    main()
