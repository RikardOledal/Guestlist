from cmath import nan
from os import getcwd
import pandas as pd
from pandas.core.frame import DataFrame
import uuid
import json
from PyQt6.QtWidgets import QFileDialog

the_dict = [
    {
  "name": "Kristina Nileman",
  "phone": "0703719893",
  "email": "",
  "address": "Gr/u00e4n/u00f6stigen 3, 135 69, Tyres/u00f6",
  "attending": False,
  "notes": "",
  "id": "18401957-3f60-4f6f-a22a-9ca2230830dd"
},
{
  "name": "Curt Nileman",
  "phone": "",
  "email": "",
  "address": "Gr/u00e4n/u00f6stigen 3, 135 69, Tyres/u00f6",
  "attending": False,
  "notes": "",
  "id": "417aebed-a915-4989-9eba-2380e05ca1a7"
},
{
  "name": "Svante Oledal",
  "phone": "0705344110",
  "email": "svante@vat.se",
  "address": "Mellby Byv/u00e4g 2, 277 35, Kivik",
  "attending": False,
  "notes": "",
  "id": "f3b17a21-0ce6-47b4-beef-92739fa0f33e"
},
{
  "name": "Margareta Tyd/u00e9n",
  "phone": "0730915505",
  "email": "",
  "address": "Gal/u00e4rv/u00e4gen 14, 393 59, Kalmar",
  "attending": True,
  "notes": "",
  "id": "1627b00f-a458-459b-8852-2f49c5c964ff"
},
{
  "name": "Jan Danielsson",
  "phone": "",
  "email": "",
  "address": "Gal/u00e4rv/u00e4gen 14, 393 59, Kalmar",
  "attending": True,
  "notes": "",
  "id": "c846cab1-3e87-4dd0-99ad-3ae4bb1cd691"
},
{
  "name": "Ylva Oledal",
  "phone": "",
  "email": "",
  "address": "Ljungv/u00e4gen 96, 194 60, Upplands V/u00e4sby",
  "attending": True,
  "notes": "Barn/n/n",
  "id": "e7bb7265-ab14-4ce6-af19-26bf30b74cbb"
},
{
  "name": "Zelda Oledal",
  "phone": "",
  "email": "",
  "address": "Ljungv/u00e4gen 96, 194 60, Upplands V/u00e4sby",
  "attending": True,
  "notes": "Barn/n/n",
  "id": "6931de64-99b1-4397-bf03-c60f852f27c1"
}
]

excel_file = pd.read_excel("C:/Users/user/Python/Python-Rikard/Projects/excelfiler/Guests202201150025.xlsx")
nan_value = float("NaN")
excel_file.replace("", nan_value, inplace=True)
excel_file = excel_file.to_dict(orient="list")

print(excel_file["Name"][0])
i = len(excel_file["Name"])    
while i != 0:
    i -= 1
    if excel_file["Notes"][i] is nan:
        notes = ""
    else:
        notes = excel_file["Notes"][i]
    new_contact = {
        "name": excel_file["Name"][i],
        "phone": "0" + str(excel_file["Phone"][i]),
        "email": excel_file["E-mail"][i],
        "address": excel_file["Address"][i],
        "attending": excel_file["Attending"][i],
        "notes": "",
        "id": str(uuid.uuid4())
    }
    the_dict.append(new_contact)

print(the_dict)

with open("rikard.json", "w") as f:
    json.dump(the_dict, f, indent=2)