import pandas as pd
import glob

location = "C:/Users/user/Python/Python-Rikard/Projects/excelfiler/*.xlsx"
excel_files = glob.glob(location)

pd.set_option("display.max_rows",183)


print(excel_files)

df1 = pd.DataFrame()

for file in excel_files:
    df2 = pd.read_excel(file, index_col=0)
    df1 = pd.concat([df1, df2])

df1.to_excel("C:/Users/user/Python/Python-Rikard/Projects/Temp/Jobbat2020.xlsx")
print(df1)
