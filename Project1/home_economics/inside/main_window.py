from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem, QStandardItemModel, QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QListView, QGroupBox, QLineEdit, QTextEdit, QLabel,
    QHBoxLayout, QVBoxLayout, QWidget, QMessageBox
)

class MainWindow(QMainWindow):
    def __init__(self, contacts_service: ContactsService) -> None:
        super().__init__()

        self.contacts_service = contacts_service
        self.contacts_model = QStandardItemModel(self)
        self.current_contact = None

        self.initUi()
        self.initActions()
        self.refreshContacts()
    
    def initUi(self):
        pass

    def initActions(self):
        pass

    def refreshContacts(self):
        pass
    

