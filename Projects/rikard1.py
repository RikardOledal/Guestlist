from os import name
import pandas as pd
from pandas.core.frame import DataFrame

excel_file = pd.read_excel("C:/Users/user/Python/Python-Rikard/Projects/excelfiler/svardop.xlsx", usecols="A")
list_names= []

for row in excel_file.iteritems():
    list_names.append(row["Namn"])

print(list_names)
    
    


