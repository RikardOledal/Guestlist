from sqlite3 import connect
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from functions import show_frame1, frame1, frame2, frame3, frame4, grid

#https://opentdb.com/api.php?amount=10&category=20&difficulty=easy&type=multiple

game_name = "Hotet"

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle(game_name)
window.resize(1000, 800)
window.move(200, 200)
window.setStyleSheet("background: #161219;")
print(window.width(), window.height())

show_frame1()

window.setLayout(grid)
window.show()
sys.exit(app.exec())