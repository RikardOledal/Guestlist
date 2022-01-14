import pandas as pd
import glob
from datetime import datetime

location = "C:/Users/user/Python/Python-Rikard/Projects/excelfiler/*.xlsx"
excel_files = glob.glob(location)

pd.set_option("display.max_rows",183)


print(excel_files)

df1 = pd.DataFrame()

for file in excel_files:
    df2 = pd.read_excel(file, index_col=0)
    df1 = pd.concat([df1, df2])


id_date = datetime.strftime(datetime.now(), "20%y%m%d%H%M%S")
print(id_date)
file_name = "C:/Users/user/Python/Python-Rikard/Projects/excelfiler/Jobbat" + str(id_date) + ".xlsx"
df1.to_excel(file_name)
print(df1)


