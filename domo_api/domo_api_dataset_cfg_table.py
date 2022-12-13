#domo_api_dataset_cfg_table.py
#==============================================================================
#lookup tables pairing datasets and their column types and names
#==============================================================================							
#may be better to split this monolithic file into separate simpler files for
#each data set
from pydomo.datasets import ColumnType

#lookup table of dataset name and column types
column_types_dict = {   #originally called "MN_JSON_QA_List_Test"
                        "MPC QA List"                           :   [   ColumnType.LONG,        #ControlID
                                                                        ColumnType.DATETIME,    #ControlDate
                                                                        ColumnType.STRING,      #GaBlockId
                                                                        ColumnType.STRING,      #Screen
                                                                        ColumnType.STRING,      #Size
                                                                        ColumnType.STRING,      #PackStyle
                                                                        ColumnType.STRING,      #Url
                                                    ],
                        #originally called "mpc_qa_ppi_carton_weight_sql_pull"
                        "MPC_QA_PPI_Carton_Weight"              :   [   ColumnType.LONG,        #ControlID
                                                                        ColumnType.DATETIME,    #ControlDate
                                                                        ColumnType.STRING,      #CmtyNm
                                                                        ColumnType.STRING,      #VarietyNm
                                                                        ColumnType.STRING,      #GaBlockId
                                                                        ColumnType.STRING,      #PackStyle
                                                                        ColumnType.STRING,      #Weight
                                                                        ColumnType.DOUBLE,      #BoxWeight
                                                                        ColumnType.LONG,        #BoxCount
                                                                        ColumnType.STRING,      #Size
                                                                        ColumnType.DOUBLE,      #WeightNumeric
                                                                    ],
                        #originally called "MN_Bag_Total_Count_Per_Shift"
                        "Production Bag Total Count Per Shift"  :   [   ColumnType.DATE,        #ShiftDate
                                                                        ColumnType.STRING,      #Shift
                                                                        ColumnType.LONG,        #TotalBags
                                                                        ColumnType.LONG,        #AvgBagPerHour
                                                                        ColumnType.LONG,        #AvgBagPerMin                                                                    
                                                                                                        ],
                        #originally called "MN_Bagger_Stats_Per_Shift"
                        "Production Bagger Stats Per Shift"     :   [   ColumnType.DATE,        #ShiftDate
                                                                        ColumnType.STRING,      #Shift
                                                                        ColumnType.STRING,      #Bagger
                                                                        ColumnType.LONG,        #TotalBagCount
                                                                        ColumnType.LONG,        #AvgBagPerHour
                                                                        ColumnType.LONG,        #AvgBagPerMin
                                                                        ColumnType.DATETIME,    #StartTime
                                                                        ColumnType.DATETIME,    #StopTime
                                                                     ]
                    }
                                    

#lookup table of dataset name and column names
column_names_dict = {   #totes to boxes & harvest pattern dynamic dynamic_utilization_helper_abc pre-filtered
                         "MPC QA List"                          :   [   "ControlID",
                                                                        "ControlDate",
                                                                        "GaBlockId",
                                                                        "Screen",
                                                                        "Size",
                                                                        "PackStyle",
                                                                        "Url"
                                                                    ],                                                                                
                        #originally called "mpc_qa_ppi_carton_weight_sql_pull"
                        "MPC_QA_PPI_Carton_Weight"              :   [    "ControlID",
                                                                         "ControlDate",
                                                                         "CmtyNm",
                                                                         "VarietyNm",
                                                                         "GaBlockId",
                                                                         "PackStyle",
                                                                         "Weight",
                                                                         "BoxWeight",
                                                                         "BoxCount",
                                                                         "Size",
                                                                         "WeightNumeric"
                                                                     ],
                        #originally called "MN_Bag_Total_Count_Per_Shift"
                        "Production Bag Total Count Per Shift"  :   [   "ShiftDate",
                                                                        "Shift",
                                                                        "TotalBags",
                                                                        "AvgBagPerHour",
                                                                        "AvgBagPerMin"
                                                                    ],
                        #originally called "MN_Bagger_Stats_Per_Shift"
                        "Production Bagger Stats Per Shift"     :   [   "ShiftDate",
                                                                        "Shift",
                                                                        "Bagger",
                                                                        "TotalBagCount",
                                                                        "AvgBagPerHour",
                                                                        "AvgBagPerMin",
                                                                        "StartTime",
                                                                        "StopTime"
                                                                    ]
  
                    }
