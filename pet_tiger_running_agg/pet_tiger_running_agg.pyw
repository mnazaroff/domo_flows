#PetTiger_Ranch.py
#==============================================================================
#<description>
#==============================================================================
import pyodbc
import config
import json
import pandas as pd
import sys
sys.path.append("..")   #load global config located up one directory
import config_global
from domo_api import domo

def main():
    try:
        project_name = "pet_tiger_running_agg"
        dataset_name = "pet_tiger_running_agg"    
        filename_save = config_global.dir_dataset_download_dict["uploads"]   + dataset_name + ".csv"
        filename_dataset_cfg = "./domo_api_cfg/dataset_id_table.json"

        #grab SQL data
        print("grabbing MPC QA PPI carton weight SQL data...")
        cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER=10.0.1.72;DATABASE=Moonlight;UID=sa;PWD=tc2018!")
        cursor=cnxn.cursor()

        print("executing query_crew...")
        DF_crew = pd.read_sql(config.query_table_dict["query_crew"], cnxn)        
        print("executing query_employee...")
        DF_employee = pd.read_sql(config.query_table_dict["query_employee"], cnxn)        
        print("executing query_field...")
        DF_field = pd.read_sql( config.query_table_dict["query_field"], cnxn)        
        print("executing query_job...")
        DF_job = pd.read_sql(config.query_table_dict["query_job"], cnxn)        
        print("executing query_job_card...")
        DF_job_card = pd.read_sql(config.query_table_dict["query_job_card"], cnxn)        
        print("executing query_ranch...")
        DF_ranch = pd.read_sql(config.query_table_dict["query_ranch"], cnxn)        

        #preprocess data
        DF_job_card["DateTimeIn"] = pd.to_datetime(DF_job_card["DateTimeIn"])
        DF_job_card["DateTimeOut"] = pd.to_datetime(DF_job_card["DateTimeOut"])
        DF_job_card["DateIn"] = DF_job_card["DateTimeIn"].dt.date
        DF_job_card["DateOut"] = DF_job_card["DateTimeOut"].dt.date
        DF_job_card = DF_job_card.sort_values(by=["EmployeeCounter", "DateTimeIn", "DateTimeOut"]).reset_index(drop=True)
        DF_job_card["Pieces"].fillna(0, inplace=True)
        # DF_job_card_test = DF_job_card[DF_job_card["EmployeeCounter"] == emp_cntr_test].copy()
        # DF_employee_test = DF_employee[DF_employee["ExportIdentifier"] == export_id_test].copy()

        #append employee information
        DF_data = pd.merge( DF_job_card, DF_employee,
                                 left_on = ["EmployeeCounter"],
                                 right_on = ["EmployeeCounter"],
                                 how = "left")

        #append crew information
        DF_data = pd.merge( DF_data, DF_crew,
                                 left_on=["CrewCounter"],
                                 right_on=["CrewCounter"],
                                 how="left")

        #append ranch information
        DF_data = pd.merge( DF_data, DF_ranch,
                                 left_on=["RanchCounter"],
                                 right_on=["RanchCounter"],
                                 how="left"
                                 )

        #append field information
        DF_data = pd.merge( DF_data, DF_field,
                                 left_on=["FieldCounter"],
                                 right_on=["FieldCounter"],
                                 how="left"
                                 )
        #append job information
        DF_data = pd.merge( DF_data, DF_job,
                                 left_on=["JobCounter"],
                                 right_on=["JobCounter"],
                                 how="left")

        DF_data = DF_data[[ "ExportIdentifier", "Employee_Name","Crew_Name", "Ranch_Name", "Field_Name",
                            "Job_Name", "DateIn", "DateOut", "DateTimeIn", "DateTimeOut",
                            "NetTime", "BreakTime", "HourlyRate", "Pieces"
                         ]]

        #an overall breakdon of aggregrate worker stats
        DF_data_overall_agg = DF_data.groupby(by=["ExportIdentifier",
                                                  "Employee_Name",
                                                  "Crew_Name",
                                                  "Ranch_Name",
                                                  "Field_Name",
                                                  "DateIn"
                                                  ],
                                                  as_index=False
                                              ).agg({ "DateTimeIn"  : "min",
                                                      "DateTimeOut" : "max",
                                                      "NetTime"     : "sum",
                                                      "BreakTime"   : "sum",
                                                      "HourlyRate"  : "max",
                                                      "Pieces"      : "sum"
                                              })

        DF_data_overall_agg["Work_Time"] = DF_data_overall_agg["NetTime"] - DF_data_overall_agg["BreakTime"]
        DF_data_overall_agg["Pieces_per_Hour"] = DF_data_overall_agg["Pieces"]/DF_data_overall_agg["Work_Time"]
        DF_data_overall_agg["Start_Time"] = DF_data_overall_agg["DateTimeIn"].dt.time
        DF_data_overall_agg["End_Time"] = DF_data_overall_agg["DateTimeOut"].dt.time

        DF_data_overall_agg.rename(columns={ "HourlyRate" : "Wage_HR", "Pieces" : "Total_Pieces"}, inplace=True)

        DF_data_overall_agg = DF_data_overall_agg[[ "ExportIdentifier", "Employee_Name", "Crew_Name", "Ranch_Name", "Field_Name",
                                              "DateIn", "Start_Time", "End_Time", "Wage_HR", "Total_Pieces",
                                              "Pieces_per_Hour"                  
                                           ]]

        DF_data_overall_agg = DF_data_overall_agg.sort_values(by=["ExportIdentifier", "DateIn", "Start_Time"]).reset_index(drop=True)
        DF_data_overall_agg.to_csv(filename_save, index = False)
        print("results saved to:\n{0}".format(filename_save))
        

        #upload data to Domo
        domo_sess = domo.DomoStream(domo.client_ID, domo.client_secret, domo.api_host)
        
        #load data set column type configuration from JSON file
        with open(filename_dataset_cfg, 'r') as fp_open:
            dataset_id_table_dict = json.load( fp_open)
        
        dataset_id = dataset_id_table_dict[project_name]["uploads"][dataset_name]        
        result = domo_sess.DatasetReplaceCSV( dataset_id, filename_save)
        print(result)
        print("{0} uploaded to domo\n".format( filename_save))
         
    except Exception as e:
        template = "An exception oftype {0} occurred arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print(message)
if __name__ == "__main__":
    main()






