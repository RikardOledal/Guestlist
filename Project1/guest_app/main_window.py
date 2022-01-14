from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem, QStandardItemModel, QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QListView, QGroupBox, QLineEdit, QTextEdit, QLabel,
    QHBoxLayout, QVBoxLayout, QWidget, QMessageBox, QCheckBox
)
import pandas as pd
from datetime import datetime

from pandas.core.frame import DataFrame

from .guests_services import GuestService
from Project1.guest_app import guests_services

class MainWindow(QMainWindow):
    def __init__(self, guests_service: GuestService) -> None:
        super().__init__()

        self.guests_service = guests_service
        self.guests_model = QStandardItemModel(self)
        self.current_guest = None

        self.initUi()
        self.initActions()
        self.refreshGuests()
    

    def initUi(self):
        self.guests_list = QListView(self)
        self.guests_list.setModel(self.guests_model)

        # Guests details form elements
        guest_details = QGroupBox("Guest details", self)
        name_label = QLabel("Name", guest_details)
        self.name_edit = QLineEdit(guest_details)
        phone_label = QLabel("Phone", guest_details)
        self.phone_edit = QLineEdit(guest_details)
        email_label = QLabel("Email", guest_details)
        self.email_edit = QLineEdit(guest_details)
        address_label = QLabel("Address", guest_details)
        self.address_edit = QLineEdit(guest_details)
        attending_label = QLabel("Attending", guest_details)
        self.attending_edit = QCheckBox(guest_details)
        notes_label = QLabel("Notes", guest_details)
        self.notes_edit = QTextEdit(guest_details)

        # Contact details form layout
        details_layout = QVBoxLayout()
        details_layout.addWidget(name_label)
        details_layout.addWidget(self.name_edit)
        details_layout.addWidget(phone_label)
        details_layout.addWidget(self.phone_edit)
        details_layout.addWidget(email_label)
        details_layout.addWidget(self.email_edit)
        details_layout.addWidget(address_label)
        details_layout.addWidget(self.address_edit)
        details_layout.addWidget(attending_label)
        details_layout.addWidget(self.attending_edit)
        details_layout.addWidget(notes_label)
        details_layout.addWidget(self.notes_edit)

        guest_details.setLayout(details_layout)

        # Buttons
        self.quit_btn = QPushButton("Quit", self)
        self.quit_btn.setHidden(True)
        
        self.delete_btn = QPushButton("Delete", self)
        self.delete_btn.setDisabled(True)

        self.save_btn = QPushButton("Save", self)

        # Buttons layout
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.delete_btn)
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.save_btn)
        # buttons_layout.addWidget(self.quit_btn)

        # Right column layout
        right_column = QVBoxLayout()
        right_column.addWidget(guest_details)
        right_column.addLayout(buttons_layout)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.guests_list)
        main_layout.addLayout(right_column)

        # Main widget
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Toolbars and actions
        main_toolbar = self.addToolBar("Main")
        main_toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.new_guest_action = QAction(QIcon("contacts_app/icons/add.png"), "Add guest", self)
        self.new_guest_action.setIconText("Add guest")
        self.new_guest_action.setToolTip("Add a new guest")

        self.quit_action = QAction(QIcon("contacts_app/icons/logout.png"), "Quit", self)
        self.quit_action.setIconText("Quit")

        self.export_action = QAction(QIcon("contacts_app/icons/logout.png"), "Export", self)
        self.export_action.setIconText("Export")

        main_toolbar.addAction(self.new_guest_action)
        main_toolbar.addSeparator()
        main_toolbar.addAction(self.quit_action)
        main_toolbar.addSeparator()
        main_toolbar.addAction(self.export_action)

        # Menubar
        main_menu = self.menuBar().addMenu("Guests")
        main_menu.addAction(self.new_guest_action)
        main_menu.addSeparator()
        main_menu.addAction(self.quit_action)

        self.resize(800, 600)
        self.setWindowTitle("My Guests")

    def initActions(self):
        self.quit_btn.clicked.connect(self.quit)
        self.quit_action.triggered.connect(self.quit)
        self.export_action.triggered.connect(self.export_guestlist)

        self.save_btn.clicked.connect(self.saveClicked)
        self.delete_btn.clicked.connect(self.deleteClicked)
        self.guests_list.activated.connect(self.guestActivated)
        self.guests_list.clicked.connect(self.guestActivated)
        self.new_guest_action.triggered.connect(self.newGuestActivated)

    def refreshGuests(self):
        guests = self.guests_service.get_guests()
        self.guests_model.clear()
        for guest in guests:
            name = QStandardItem(guest["name"])
            name.setData(guest["id"])

            email = QStandardItem(guest["email"])
            email.setData(guest["id"])

            self.guests_model.appendRow([name, email])

    def newGuestActivated(self):
        self.current_guest = None
        self.guests_list.clearSelection()
        self.clearFields()
        self.delete_btn.setDisabled(True)
        self.name_edit.setFocus()

    def guestActivated(self, index):
        contact_id = self.guests_model.itemFromIndex(index).data()
        self.current_guest = self.guests_service.get_guest(contact_id)

        self.name_edit.setText(self.current_guest["name"])
        self.phone_edit.setText(self.current_guest["phone"])
        self.email_edit.setText(self.current_guest["email"])
        self.address_edit.setText(self.current_guest["address"])
        self.attending_edit.setChecked(self.current_guest["attending"])
        self.notes_edit.setMarkdown(self.current_guest["notes"])
    
        self.delete_btn.setDisabled(False)

    def saveClicked(self):
        is_edit = False if self.current_guest is None else True

        if not is_edit:
            self.current_guest = {}

        self.current_guest["name"] = self.name_edit.text()
        self.current_guest["phone"] = self.phone_edit.text()
        self.current_guest["email"] = self.email_edit.text()
        self.current_guest["address"] = self.address_edit.text()
        self.current_guest["attending"] = self.attending_edit.isChecked()
        self.current_guest["notes"] = self.notes_edit.toMarkdown()

        if is_edit:
            self.guests_service.update(self.current_guest)
            QMessageBox.information(self, "Updated", "Your guest has been successfully updated")
        else:
            self.guests_service.create(self.current_guest)
            QMessageBox.information(self, "Created", "Your guest has been successfully created")

        self.refreshGuests()

    
    def deleteClicked(self):
        response = QMessageBox.question(
            self, 
            "Delete guest", 
            "Dou you really want to delete {} as a guest".format(self.current_guest["name"])
        )

        if response != QMessageBox.StandardButton.Yes:
            return

        self.guests_service.delete(self.current_guest)
        self.current_guest = None

        self.clearFields()

        self.refreshGuests()

        QMessageBox.information(self, "Removed", "Guest has been successfully removed")

    def quit(self):
        QApplication.instance().quit()

    def clearFields(self):
        self.name_edit.clear()
        self.phone_edit.clear()
        self.email_edit.clear()
        self.address_edit.clear()
        self.attending_edit.setCheckable(True)
        self.notes_edit.clear()
    
    def export_guestlist(self):
        export = self.guests_service.export()
        df_export = DataFrame.from_dict(export)
        id_date = datetime.strftime(datetime.now(), "20%y%m%d%H%M")
        print(id_date)
        file_name = "C:/Users/user/Python/Python-Rikard/Projects/excelfiler/Guests" + str(id_date) + ".xlsx"
        df_export.to_excel(file_name)
        