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

query_table_dict = {
    #crew data
    "query_crew"        :   """
                            SELECT
                                CrewCounter	    AS	CrewCounter,
                                Name            AS	Crew_Name	
                            FROM
                                Crew
                            """,

    #employee data
    "query_employee"    :   """
                            SELECT
                                EmployeeCounter     AS  EmployeeCounter,
                                Name 		    AS  Employee_Name,
                                ExportIdentifier    AS  ExportIdentifier

                            FROM
                                Employee
                            """,

    #field data
    "query_field"       :   """
                            SELECT
                                FieldCounter	    AS  FieldCounter,                                
                                ExportIdentifier    AS  Field_ExportIdentifier
                            FROM
                                Field
                            """,

    #job data
    "query_job"         :   """
                            SELECT
                                JobCounter 	AS  JobCounter,
                                Name		AS  Job_Name
                            FROM
                                Job
                            """,

    #job card data
    "query_job_card"    :   """
                            SELECT
                                JobCardCounter,
                                EmployeeCounter,
                                CrewCounter,
                                RanchCounter,
                                FieldCounter,
                                JobCounter,
                                Pieces,
                                DateTimeIn,
                                DateTimeOut,
                                Reference,
                                GrossTime,
                                NetTime,
                                RateSource,
                                HourlyRate,
                                AmountByTime,
                                NetTimeMinutes,
                                PieceRate,
                                AmountByPiece,
                                BreakTime,
                                PieceDiscrepancy,
                                Exported

                            FROM
                                JobCard
                            WHERE
                                    Deleted = 0
                                AND DateTimeIn >= DATEADD(year, -1, GETDATE())
                            """,

    #ranch data
    "query_ranch"       :   """
                            SELECT
                                RanchCounter    AS	RanchCounter,
                                Name 	        AS	Ranch_Name
                            FROM
                                Ranch
                            """
}
