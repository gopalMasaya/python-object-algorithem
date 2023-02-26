import csv
import pandas as pd

data = pd.read_csv("close_objects_seq.csv")
# Preview the first 5 lines of the loaded data

print(data.head(10))
