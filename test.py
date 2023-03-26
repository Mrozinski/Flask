import pandas as pd 

file_name = "dane/koszty.csv" 

dane = pd.read_csv(file_name, header=None, sep = ";")
print(dane.values)