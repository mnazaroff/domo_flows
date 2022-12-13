#domo_api_dataset_id_table.py

#==============================================================================

#lookup table of dataset name and ids

#==============================================================================

#may be better to split this monolithic file into separate simpler files in

#their respective domo project folders



#domo data set name and ID mappings

data_set_name_id_dict = {   "MN_SQL_Flow_test_Utilization PVA Helper Dynamic"       :   {

                

                                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic input data sets

                                "inputs"    :   {   "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_in_block_master_v2"                            :   "e3e6865b-3162-4b3b-96a0-2e5e7bacd0cf",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_in_daily_projection"                           :   "4a05212d-33eb-4b19-a7f7-1a6f6c9d479f",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_in_dynamic_utilization_helper_bm2_summer"      :   "dc847a57-ea1e-40e7-a1cd-d0b3edc78562",
                                                    #"MN_SQL_Flow_test_Utilization PVA Helper Dynamic_in_mpc_company_7_packout"                      :   "b7c10ab5-202b-43bb-9544-1af3ba762dfe",
                                                    #"MN_SQL_Flow_test_Utilization PVA Helper Dynamic_in_mpc_eq_sizes"                               :   "cc2a7a29-a498-4aa7-9233-9dbb2c1a914f",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_in_mpc_faceforward_packout"                    :   "e5b99ffd-54d9-4f99-a3c3-49e5a90408a8",
                                                    #"MN_SQL_Flow_test_Utilization PVA Helper Dynamic_in_mpc_faceforward_inventory"                  :   "e61d2f17-022b-4913-ae10-85b458226086",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_in_mpc_projections"                            :   "33864404-e6a9-488d-b3e0-4a67c07d6550",
                                                    #"MN_SQL_Flow_test_Utilization PVA Helper Dynamic_in_output_stone_fruit"                         :   "76393467-e333-41cf-b53d-c90fe030a343"                                  

                                },

                                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic output data sets

                                "outputs"   :   {   "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_out_3y_bm2_summer"                             :   "00d18992-1ac5-44c4-9400-871f6dfb1951",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_out_ab"                                        :   "50ae82d8-fbfd-47b7-a7f6-bedcc30464ea",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_out_abc"                                       :   "e5857419-cb3c-4d80-b28c-830a9d1139e1",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_out_bm2_summer"                                :   "198d77ef-a3ba-40f2-8da6-7724cfb0c6fe",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_out_c"                                         :   "fc2ffa0a-336e-40f4-a829-44a04de89188",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_out_ff_ab"                                     :   "51f8abff-95ea-4505-9823-bc0ae6ba2b28",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_out_ff_ab_debug1"                              :   "bde21339-4f79-4025-bddf-d7488d401826",
                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_out_ff_ab_debug2"                              :   "82a84488-c85e-4f20-b464-f3bd6531b2df"                                

                                },

                                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic internal table calculations

                                "processes" :   {   "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_3y_bm2_summer"                           :   "75940b74-e741-48ac-a063-bea6e7cb6324",

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_3y_projection_summer"                    :   "d03b5ca3-ef5d-4fc4-bd8d-7fb6307cd499",

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_bm2"                                     :   "8a49a255-2d14-4231-9779-9e848d2941f3",

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_bm2_summer"                              :   "98999543-fa6a-4bb3-84ff-e3af573b9a8f",                                               

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_daily_projection"                        :   "b0569a45-96d0-40d6-85e1-af44470f3084",

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_projections_summer"                      :   "c33ef27b-d2bd-497c-b3cb-6d723de28869"                            

                                },

                                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic uploaded test data

                                "uploads"   :   {   "MN_Table_test_u_pva_h_dyn_data_pf_bm2"                                                         :   "73bd0ddb-47e4-440b-8f03-283ef8b98725",

                                                    "MN_Table_test_u_pva_h_dyn_data_pf_bm2s"                                                        :   "ce3bbfef-9afe-48df-a3c9-e7d468753dff",

                                                    "MN_Table_test_u_pva_h_dyn_data_pf_dp"                                                          :   "2e3b0d46-9d8f-4d23-84d0-2f9407044c25",

                                                    "MN_Table_test_u_pva_h_dyn_data_pf_mp"                                                          :   "e8250cff-e397-46d0-b448-c7257a527fb7" 

                                                    

                                },

                                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic lookup table data sets

                                "tables"    :   {   "MN_Table_override_blockID_commodity"                                                           :   "b409d6de-034a-43cc-811c-6601f0b41300",

                                                    "MPC EQ SIZES"                                                                                  :   "67fcff0e-d9e2-4d78-a8b8-b512cdd34a91"

                                    

                                }

                                

                        },

                        "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic"     :   {

                            

                                #MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic input data sets

                                "inputs"    :   {   "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_in_dp"                               :   "cb7d9409-25d4-4ad6-9bbe-1b52f6a256ad",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_in_numbers"                          :   "deb98321-311a-4b16-8cd1-8f154386ba1e",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_in_hrvst_pttrn_hlpr"                 :   "af0c6e12-d7be-453f-9f8d-a0bbb39bd004",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_in_dyn_util_hlpr_bm2s"               :   "7fc92a1c-cc37-448d-aeeb-ed015d7640d8",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_in_dyn_util_hlpr_abc"                :   "777bb383-5a66-4319-a45d-eef863326dba",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_in_mpc_eq_sizes"                     :   "59c6d4e0-7866-416a-a615-9389109727ed"

                                },

                                #MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic output data sets

                                "outputs"   :   {   "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_hrvst_pttrn_proj"   :   "63e76c18-fe6e-4cb1-b90e-4b2fa1f1aeaf",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_hrvst_pttrn_proj_mod"            :   "b77d945b-d21a-454c-a92d-b11fd6d297d5"

                                },

                                #MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic internal table calculations

                                "processes" :   {   "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_data_a"                        :   "96c94e48-ecb5-4953-8afb-34d2fe9030de",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_data_new_blocks"               :   "b520101b-4c67-4e67-b5ac-8188b3df0a44",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_data"                          :   "40201c6b-7657-4ffc-828f-efe015096e23",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_commodity_averages"            :   "3df10248-d19c-4f41-8a23-74bb36a296df",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_data_commodity_sum"            :   "14068d5e-e83d-4b3e-a3e7-e0ad0c780b08",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_numbers"                       :   "e1226b7c-e560-4448-8192-bf4f30ebf19e",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_daily_commodity_norm_helper"   :   "0c685cc5-7d33-43a2-85c4-18e08b947767",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_daily_commodity_norm"          :   "0f52128c-f1ae-4082-994b-8a3a666ce597",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_commodity_default"             :   "1e3770d3-8a4f-4bb9-82ee-453f7e92f57f",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_harvest_pattern_helper"        :   "0b25b4ce-e92f-4867-bc03-0de4507bf6ed",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_data_c"                        :   "7d9fcf90-393a-4289-9531-eb98cbe64cbf",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_data_current_pack"             :   "6b5ee5eb-6b79-407d-a68c-6c5fa2d88809",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_data_previous_bulk"            :   "103c4f1b-37c0-4e47-b081-5698d32582c4",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_data_stage_data_current_bulk"             :   "f0a77d48-9010-4048-aea1-8ec63db0f7e7",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_data_dly_proj"          :   "830c229f-c8a5-47af-9809-5e7fe41a480c",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_dp_derive"              :   "688ee118-781d-4be2-bf4d-3e8e4b53c849",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_chris_1"                :   "18925427-a4b1-4664-a043-4eabc7d42ab7",

                                                    # "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_chris_1_mod"       :   "0fb1a799-f8b9-40c7-943a-2a0574531236",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_chris_agg"              :   "d4cabce4-5134-421c-aedf-1f8df32253ed",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_max_pick_day"           :   "4850a2ed-ff6f-4a27-a264-ae2fafbcdf22",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_chris_2"                :   "614d2395-cfc1-42db-8efd-4436705f559a",

                                                    # "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_chris_2_mod"       :   "5606ba71-d119-4f58-9759-175117e55485",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_chris_3"                :   "d5289f5c-f771-4a91-9be2-65c442dcd291",

                                                    # "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_chris_3_mod"       :   "70965cf6-d596-437a-90e9-e07107b1d5c6",

                                                    "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_hrvst_pttrn_proj"       :   "63e76c18-fe6e-4cb1-b90e-4b2fa1f1aeaf"

                                                    # "MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic_projections_stage_hrvst_pttrn_proj_mod" :   "b77d945b-d21a-454c-a92d-b11fd6d297d5"

                                },

                                #MN_SQL_Flow_test_Totes to Boxes & Harvest Pattern Dynamic uploaded test data

                                "uploads"   :   {   "MN_Table_test_tb_n_hpd_data_pf_abc"                                                            :   "29b08366-cba1-4c14-975a-d92ae8e11ce4",

                                                    "MN_Table_test_tb_n_hpd_data_pf_bm2s"                                                           :   "289473b4-3e71-4203-9d08-edb8cf062074",

                                                    "MN_Table_test_tb_n_hpd_data_pf_dp"                                                             :   "c45a09e3-9725-4a84-bc2a-9e100e751a56"

                                    

                                }

                                

                        },

                        "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab"    :   {

                                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab input data sets

                                "inputs"    :   {   "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab_in_bm2"                     :   "946a5eb0-408b-4c56-b721-29dcd11658b7",

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_in_eqs"                        :   "a1993f85-17e2-446f-bf8f-758aa8ccba15",

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab_in_ff_po"                   :   "737f44ba-4790-4a22-bef6-4d733648ba5e"

                                                     

                                },

                                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab output data sets

                                "oututs"    :   {

                                },

                                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab internal table calculations

                                "processes" :   {   "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab_proc_agg"                   :   "e487bf35-5096-4c1d-9473-0c3e6613ff42",

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab_proc_join1"                 :   "d2c67479-6b95-488e-9941-d48b3dca982f",

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab_proc_join2"                 :   "4807376b-8822-4330-b893-11ad928edc88",                                                    

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab_proc_h_ab"                  :   "78ec1e72-5b0b-4dc9-92f4-04c88eb5c10f",

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab_proc_ssm"                   :   "de73b0db-22a0-428f-b89e-15ac22cf4b91",

                                                    "MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab_proc_pf_ff_po"              :   "6e109bd0-568c-40bb-a103-3200e6939f8b"

                                } 

                    },

                    "MN_SQL_Flow_test_Stone Fruit_bvc_calc_only"                                :   {

                            #MN_SQL_Flow_test_Stone Fruit_bvc_calc_only input data sets

                            "inputs"    :   {       "MN_SQL_Data_test_Stone Fruit_bvc_calc_only_in_abc"                                             :   "cc17f345-f828-442a-83c3-2ecb2182f883",

                                                    "MN_SQL_Data_test_Stone Fruit_bvc_calc_only_in_bm2s"                                            :   "4ca7c16b-49b2-47d6-b891-beebc150ce8e"

                            },

                            #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab output data sets

                            "outputs"    :   {      "MN_SQL_Data_test_Stone Fruit_stage_output_bvc_calc_only"                                      :   "55ff4051-15ef-4962-b63e-3b88f7d7a0b1"

                            },

                            #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab internal table calculations

                            "processes" :   {   ""                   :   ""

                                                

                            } 

                },

                "MN_ETL_Flow_totes_to_boxes_&_harvest_pattern_dynamic_data"                     :   {

                        #MN_SQL_Flow_test_Stone Fruit_bvc_calc_only input data sets

                        "inputs"    :   {       ""                                             :   ""                                               

                        },

                        #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab output data sets

                        "outputs"    :   {        "MN_ETL_Data_totes_to_boxes_&_harvest_pattern_dynamic_data_prefilter_bm2s"                        :   "26057722-66e2-4040-8f58-8231a6d06ef2",

                                                  "MN_ETL_Data_totes_to_boxes_&_harvest_pattern_dynamic_data_stage_commodity_default"               :   "c177686f-22df-4a34-be68-ab972a10d5a3"

                        },

                        #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab internal table calculations

                        "processes" :   {       "MN_ETL_Data_totes_to_boxes_&_harvest_pattern_dynamic_data_prefilter_abc"                           :   "52958d11-f1f2-4c04-8778-19f0056d56b7",                                                

                                                "MN_ETL_Data_totes_to_boxes_&_harvest_pattern_dynamic_data_stage_data_new_blocks"                   :   "ef64b6a7-1106-4198-b552-d5be08dfb933"

                                            

                        } 

            },

            "MN_ETL_Flow_totes_to_boxes_&_harvest_pattern_dynamic_proj"                         :   {

                    #MN_SQL_Flow_test_Stone Fruit_bvc_calc_only input data sets

                    "inputs"    :   {       ""                                             :   ""                                               

                    },

                    #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab output data sets

                    "outputs"    :   {        "MN_ETL_Data_totes_to_boxes_&_harvest_pattern_dynamic_data_prefilter_bm2s"                        :   "26057722-66e2-4040-8f58-8231a6d06ef2",

                                              "MN_ETL_Data_totes_to_boxes_&_harvest_pattern_dynamic_data_stage_commodity_default"               :   "c177686f-22df-4a34-be68-ab972a10d5a3"

                    },

                    #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab internal table calculations

                    "processes" :   {       "MN_ETL_Data_totes_to_boxes_&_harvest_pattern_dynamic_data_prefilter_abc"                           :   "52958d11-f1f2-4c04-8778-19f0056d56b7",                                                

                                            "MN_ETL_Data_totes_to_boxes_&_harvest_pattern_dynamic_data_stage_data_new_blocks"                   :   "ef64b6a7-1106-4198-b552-d5be08dfb933"

                                        

                    } 

        },

        "MN_SQL_Flow_Test_stone_fruit_data_post_proc"                         :   {

                #MN_SQL_Flow_test_Stone Fruit_bvc_calc_only input data sets

                "inputs"    :   {       ""                                             :   ""                                               

                },

                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab output data sets

                "outputs"    :   {        "MN_SQL_Data_Test_stone_fruit_data_post_proc_agg_util_b_1yr"                          :   "f19a1242-12bf-4e18-80fd-a18dc29775c1",

                                          "MN_SQL_Data_Test_stone_fruit_data_post_proc_agg_util_b_2yr"                          :   "a5e87698-8973-4268-b7f1-dd79e4f75323",

                                          "MN_SQL_Data_Test_stone_fruit_data_post_proc_agg_util_b_3yr"                          :   "b84df064-4b7d-4cad-a963-12091d5196e4",

                                          "MN_SQL_Data_Test_stone_fruit_data_post_proc_agg_util_c_1yr"                          :   "0a91f454-02f6-4c7b-859e-73c57df88f39",

                                          "MN_SQL_Data_Test_stone_fruit_data_post_proc_agg_util_c_2yr"                          :   "f18ed8b8-f0dc-45d5-8555-9536fc8b400b",

                                          "MN_SQL_Data_Test_stone_fruit_data_post_proc_agg_util_c_3yr"                          :   "ed2d375d-e356-4fbe-8f52-da589a87ab89",

                                          "MN_SQL_Data_Test_stone_fruit_data_post_proc_agg_util_cv_1yr"                         :   "a15980a4-4b8c-4e0d-8ed8-40136a10051e",

                                          "MN_SQL_Data_Test_stone_fruit_data_post_proc_agg_util_cv_2yr"                         :   "1b32be48-7c1d-45b1-ae54-f074e062fadd",

                                          "MN_SQL_Data_Test_stone_fruit_data_post_proc_agg_util_cv_3yr"                         :   "e963436d-49f7-46cc-bdc5-2a5930e27fec"

                                                                                              

                },

                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab internal table calculations

                "processes" :   {       ""                                              :   ""

                                    

                } 

        },

        "MN_ETL_Flow_test_std"                         :   {

                #MN_ETL_Flow_test_std input data sets

                "inputs"    :   {       ""                                             :   ""                                               

                },

                #MN_SQL_Flow_test_Utilization PVA Helper Dynamic_stage_ff_helper_ab output data sets

                "outputs"    :   {        "MN_ETL_Data_test_std_block_info"                                                     :   "330c8bd3-aac2-40c0-b1cf-07aed0a2a767",

                                          "MN_ETL_Data_test_std_block_info_prefiltered"                                         :   "00e3d31a-9f88-4488-8b14-3ff3dfbd94fd",

                                          "MN_ETL_Data_test_std_block"                                                          :   "b8d65293-2dc1-4b9c-9ea6-11fde67ae7ff",

                                          "MN_ETL_Data_test_std_commodity"                                                      :   "817fd34e-3757-42be-a53b-d811344db80c",

                                          "MN_ETL_Data_test_std_commodityvariety"                                               :   "72df5f33-f00c-4961-a7b3-4811ec98efc0",

                                          "MN_ETL_Data_test_std_block_prefiltered"                                              :   "23e2ff1d-ff52-45b1-9275-f43e66110133",

                                          "MN_ETL_Data_test_std_commodity_prefiltered"                                          :   "64fc64dd-387d-443c-aca4-762c72cccd92",

                                          "MN_ETL_Data_test_std_commodityvariety_prefiltered"                                   :   "76083413-9bd8-469e-95d7-ccd9b85eef31"

                },

                #MN_ETL_Flow_test_std  internal table calculations

                "processes" :   {       ""                                              :   ""

                                    

                } 

        }

                

                    

}
