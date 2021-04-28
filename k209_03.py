import os
import csv
import pandas as pd

file = os.path.abspath("209-03.csv")
df_header = pd.read_csv(file, header=0)
print(df_header)