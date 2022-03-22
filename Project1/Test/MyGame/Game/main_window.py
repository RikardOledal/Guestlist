from sqlite3 import connect
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QMainWindow
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self)
        super().__init__()

        self.parameters = {
            "question": [],
            "answer1": [],
            "answer2": [],
            "answer3": [],
            "answer4": [],
            "correct": [],
            "score": [],
            "index": []
        }

        self.widgets = {
            "logo": [],
            "button": [],
            "score": [],
            "question": [],
            "awswer1": [],
            "awswer2": [],
            "awswer3": [],
            "awswer4": [],
            "message": [],
            "message2": []
        }

        self.title_frame()

    def title_frame():
        clear_widgets()
        frame1()
    
    def clear_widgets(self):
        for widget in self.widgets:
            if widgets[widget] != []:
                widgets[widget][-1].hide()
            for i in range(0, len(widgets[widget])):
                widgets[widget].pop()
    

    
    
