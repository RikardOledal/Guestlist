import json
import uuid

from PyQt6.sip import delete
from pandas.core.frame import DataFrame


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
    
