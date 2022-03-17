import json
import uuid

from PyQt6.sip import delete
from pandas.core.frame import DataFrame
import pandas as pd


class GuestService:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.guests = []

        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                self.guests = json.load(f)
        except:
            self.guests = []
    
    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.guests, f, indent=2)

    def get_guests(self):
        return self.guests

    def get_guest(self, guest_id):
        for guest in self.guests:
            if guest["id"] == guest_id:
                return guest
        
        return None

    def create(self, guest):
        guest["id"] = str(uuid.uuid4())
        self.guests.append(guest)

        self.save()

    def update(self, guest):
        for guest_to_update in self.guests:
            if guest_to_update["id"] == guest["id"]:
                guest_to_update["name"] = guest["name"]
                guest_to_update["phone"] = guest["phone"]
                guest_to_update["email"] = guest["email"]
                guest_to_update["address"] = guest["address"]
                guest_to_update["attending"] = guest["attending"]
                guest_to_update["notes"] = guest["notes"]
        
        self.save()
    
    def delete(self, guest):
        self.guests.remove(guest)
        self.save()

    def export(self):
        name_list = []
        phone_list = []
        email_list = []
        address_list = []
        attending_list = []
        note_list = []
        for guest_to_export in self.guests:
            name_list.append(guest_to_export["name"])
            phone_list.append(guest_to_export["phone"])
            email_list.append(guest_to_export["email"])
            address_list.append(guest_to_export["address"])
            attending_list.append(guest_to_export["attending"])
            note_list.append(guest_to_export["notes"])
        export_dict = {
            "Name" : name_list,
            "Phone" : phone_list,
            "E-mail" : email_list,
            "Address" : address_list,
            "Attending" : attending_list,
            "Notes" : note_list
        }
        return export_dict

    def import_guests(self, urlfile):
        excel_file = pd.read_excel(urlfile)
        excel_file = excel_file.fillna(0)
        excel_file = excel_file.to_dict(orient="list")
        i = len(excel_file["Name"])    
        while i != 0:
            i -= 1
            phone_input = "" if excel_file["Name"][i] == 0.0 else "0" + str(excel_file["Phone"][i])
            email_input = "" if excel_file["E-mail"][i] == 0.0 else excel_file["E-mail"][i]
            address_input = "" if excel_file["Address"][i] == 0.0 else excel_file["Address"][i]
            attending_input = False if excel_file["Attending"][i] == 0.0 else excel_file["Attending"][i]
            notes_input = "" if excel_file["Notes"][i] == 0.0 else excel_file["Notes"][i]

            new_contact = {
                "name": excel_file["Name"][i],
                "phone": phone_input,
                "email": email_input,
                "address": address_input,
                "attending": attending_input,
                "notes": notes_input,
                "id": str(uuid.uuid4())
            }
            self.guests.append(new_contact)
            self.save()
    
