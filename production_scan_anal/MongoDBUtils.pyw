#!usr/bin/env python3
#MongoDBUtils/py


import pandas as pd 
import config
import pymongo
import sys
import traceback
#import Api
#import utils


def docs_to_table_package_generic_monolithic(docs):
    doc_dict_CheckpointScans_list = []
    print(" test at docs_to_table_package_generic_monolithic start")
    cnt_read = 0
    cnt_success = 0
    for doc in docs:
            
        try:
            # weight_sum = 0
            # weight_count = 0
            
            # for weight_sample in doc["CheckweigherResult"]["Weights"]:
            #     weight_sum += weight_sample
            #     weight_count += 1
                
            if "CheckweigherResult"  in doc.keys():
                if "Weight" in doc["CheckweigherResult"].keys():
                    CheckweigherResultAvg = doc["CheckweigherResult"]["Weight"]
                else:
                    CheckweigherResultAvg = None
            else:
                CheckweigherResultAvg = None
                
            cnt_read = cnt_read+1                
            #print(cnt_read)
            
            for key in doc["Checkpoints"].keys():
                checkpoint_id = key
            
            doc_dict_CheckpointScan = {  "_id"                      :   doc["_id"] if ("_id" in doc.keys()) else None,
                                         "BlockID"                  :   doc["BlockID"] if ("BlockID" in doc.keys()) else None,
                                         #"Checkpoints"              :   checkpoint_id if ("Checkpoints" in doc.keys()) else None, #delete this from the domo api data set
                                         # "CheckweigherResultAvg"    :   weight_sum/weight_count if weight_count>0 else None,                                         
                                         # "CheckweigherResultAvg"    :   doc["CheckweigherResult"]["Weight"] if ("Weight" in doc["CheckweigherResult"].keys()) else None,
                                         "CheckweigherResultAvg"    :   CheckweigherResultAvg,
                                         "DateCreate"               :   doc["DateCreate"] if ("DateCreate" in doc.keys()) else None,
                                         "OriginCheckpointID"       :   doc["OriginCheckpointID"] if ("OriginCheckpointID" in doc.keys()) else None,
                                         "ProductComposite"         :   doc["ProductComposite"] if ("ProductComposite" in doc.keys()) else None,
                                         "ProductID"                :   doc["ProductID"] if ("ProductID" in doc.keys()) else None,                                         
                                         "Size"                     :   doc["Size"] if ("Size" in doc.keys()) else None,
                                         "Style"                    :   doc["Style"] if ("Style" in doc.keys()) else None,                                         
                                         "Content"                  :   doc["Content"] if ("Content" in doc.keys()) else None
                                     }               


            doc_dict_CheckpointScans_list.append( doc_dict_CheckpointScan )       
            
            cnt_success = cnt_success + 1
            
        except KeyError as e:            
            #print("{0}: {1} missing field {2}".format(cnt_read,  doc["_id"], e), end="\r", flush=True)
            continue
            # return

    print("{0} records read".format(cnt_read))
    print("{0} records processed successfully".format(cnt_success))

    return doc_dict_CheckpointScans_list


def docs_to_table_package_global_monolithic(docs):
    doc_dict_CheckpointScans_list = []    
    cnt_read = 0
    cnt_success = 0
    
    for doc in docs:    
        try:
            
            cnt_read = cnt_read+1             
            # print("{0}".format(cnt_read), end="\r", flush=True)            
            # if not cnt_read%1:
            #     print("{0}".format(cnt_read), end="\r", flush=True)                      

            if "CheckweigherResult"  in doc.keys():
                if "Weight" in doc["CheckweigherResult"].keys():
                    CheckweigherResultAvg = doc["CheckweigherResult"]["Weight"]
                else:
                    CheckweigherResultAvg = None
            else:
                CheckweigherResultAvg = None
           
            #check if AttributeDataMatrix scan scores are available
            DataMatrixExists = False
            #if "AttributeDataMatrix" in doc.keys():
            if "AttributeDATAMATRIX" in doc:#.keys():
                DataMatrixExists = True
            elif "AttributeDataMatrix" in doc.keys():
                DataMatrixExists = True            
        
            doc_dict_CheckpointScans_list.append({  "_id"                       :   doc["_id"],
                                                    "PK"                        :   doc["PK"] if ("PK" in doc.keys()) else None,
                                                    "Code"                      :   str(doc["Code"]) if ("Code" in doc.keys()) else None,
                                                    "BlockID"                   :   doc["BlockID"] if ("BlockID" in doc.keys()) else None,
                                                    "CheckpointID"              :   doc["CheckpointID"] if ("CheckpointID" in doc.keys()) else None,
                                                    "DateCreate"                :   doc["DateCreate"] if ("DateCreate" in doc.keys()) else None,
                                                    "ProductComposite"          :   doc["ProductComposite"] if ("ProductComposite" in doc.keys()) else None,
                                                    "ProductID"                 :   doc["ProductID"] if ("ProductID" in doc.keys()) else None,
                                                    "Size"                      :   doc["Size"] if ("Size" in doc.keys()) else None,
                                                    "Style"                     :   doc["Style"] if ("Style" in doc.keys()) else None,
                                                    "Content"                   :   doc["Content"] if ("Content" in doc.keys()) else None,
                                                    "OriginCheckpointID"        :   doc["OriginCheckpointID"] if ("OriginCheckpointID" in doc.keys()) else None,
                                                    "PrintSize"                 :   doc["PrintSize"] if ("PrintSize" in doc.keys()) else None,
                                                    "FruitCount"                :   doc["FruitCount"] if ("FruitCount" in doc.keys()) else None,
                                                    "CheckweigherResultAvg"     :   CheckweigherResultAvg,
                                                    "DataMatrixExists"          :   DataMatrixExists,
                                                    "PTIExists"                 :   "AttributePTI" in doc.keys()
                                                }
            )       
            
            cnt_success = cnt_success + 1
            

        except KeyError as e:            
            print("{0}: {1} missing field {2}".format(cnt_read,  doc["_id"], e), end="\r", flush=True)
            print(doc["_id"])
            continue
            #return
            
    print("{0} records read".format(cnt_read))
    print("{0} records processed successfully".format(cnt_success))

    return { "Data"             :   doc_dict_CheckpointScans_list,
             "count_read"       :   cnt_read,
             "count_success"    :   cnt_success,
             "ratio_success"    :   0 if(cnt_read == 0) else cnt_success/cnt_read
           }



def print_dict(dict_in):
    for key, val in dict_in.items() :
        print("{0}\t:\t{1}".format(key, val))

#get list of field names and value types with count their occurrences is a
#group of documents
def docs_field_count(docs):
    d_field_cnt_dict = {}

    for doc in docs:
        for key in doc.keys():
            key_val_type = str(key) + "_" + type(doc[key]).__name__
            
            if( key_val_type not in d_field_cnt_dict.keys()):
                d_field_cnt_dict[key_val_type] = 1
            else:
                d_field_cnt_dict[key_val_type] += 1     
        
    return d_field_cnt_dict
    
def docs_anal(docs):    
    cnt_read = 0
    cnt_success = 0
    cnt_fail = 0
    id_success_list = []    
    id_fail_list = []

    for doc in docs:        
        try:   

            DataMatrixExists_og = False
            if "AttributeDATAMATRIX" in doc.keys():
                DataMatrixExists_og = True
           
            doc_lower = dict((k.lower(), v) for k, v in doc.items())            
            DataMatrixExists_new = False
                
            if "attributedatamatrix" in doc_lower.keys():
                DataMatrixExists_new = True
                
            if DataMatrixExists_og != DataMatrixExists_new:
                cnt_fail = cnt_fail + 1
                id_fail_list.append(doc['_id'])     
            else:
                cnt_success = cnt_success + 1
                id_success_list.append(doc['_id'])
            
        except KeyError as e:            
            print("{0}: {1} missing field {2}".format(cnt_read,  doc["_id"], e), end="\r", flush=True)
            # continue
            return

    print("{0} records read".format(cnt_read))
    print("{0} records processed successfully".format(cnt_success))
    print("{0} records processed unsuccessfully".format(cnt_fail))
    
    with open("dme_success_ids.txt", "w") as output:
        for id in id_success_list:
            output.write( str(id) + "\n")

    with open("dme_failed_ids.txt", "w") as output:        
        for id in id_fail_list:
            output.write( str(id) + "\n" )
