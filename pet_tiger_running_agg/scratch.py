import pandas as pd

DF = pd.read_csv("DF_data_overall_agg_test.csv")
for col in DF:
    print(col)
print(DF[["DateIn", "DateTimeIn", "DateTimeOut"]])
