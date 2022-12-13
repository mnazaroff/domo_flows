#domo_api_dataset_id_table.py
#==============================================================================
#lookup table of dataset name and ids
#==============================================================================
#may be better to split this monolithic file into separate simpler files in
#their respective domo project folders

#domo data set name and ID mappings
data_set_name_id_dict = {   "MPC QA List"                           :   "0b15783b-e360-49d9-bc67-92f82293cd9a",
                            "MPC_QA_PPI_Carton_Weight"              :   "7146b968-6f5b-4607-b317-e319c72c5c43",
                            "Production Bag Total Count Per Shift"  :   "fe30cdb7-8df2-4f27-b11b-ebd9f7ebfe25",
                            "Production Bagger Stats Per Shift"     :   "8558dbe5-2dbe-41e2-aa05-0cb68acf51fe"
                                
                              }
#domo data flow name and ID mappings
data_flow_name_id_dict = {   "data_flow_name"   :   {   #input data sets
                                                        "inputs"    :   {   "data_set_name"     :   "data_set_key"  },
                                                        #output data sets
                                                        "outputs"   :   {   "data_set_name"     :   "data_set_key"  },
                                                        #internal table calculations
                                                        "processes" :   {   "data_set_name"     :   "data_set_key"  },
                                                        #uploaded test data
                                                        "uploads"   :   {   "data_set_name"      :   "data_set_key"  },
                                                        #lookup table data sets
                                                        "tables"    :   {   "data_set_name"     :   "data_set_key"  }
                                                    }
                        }
