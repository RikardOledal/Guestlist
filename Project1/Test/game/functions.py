from PyQt6.QtWidgets import QLabel, QPushButton, QGridLayout
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt
from urllib.request import urlopen
import json
import pandas as pd
import random

with urlopen("https://opentdb.com/api.php?amount=10&category=20&difficulty=easy&type=multiple") as webpage:
    data = json.loads(webpage.read().decode())
    df = pd.DataFrame(data["results"])
    idx_start = len(df["question"])-1

def preload_data():
    idx = random.randint(0, parameters["index"][-1])
    question = df["question"][idx]
    correct = df["correct_answer"][idx]
    wrong = df["incorrect_answers"][idx]

    formatting = [
        ("#039;", "'"),
        ("&'", "'"),
        ("&quot;", '"'),
        ("&lt;", "<"),
        ("&gt;", ">")
        ]

    for tuple in formatting:
        question = question.replace(tuple[0], tuple[1])
        correct = correct.replace(tuple[0], tuple[1])

    for tuple in formatting:
        wrong = [char.replace(tuple[0], tuple[1]) for char in wrong]

    parameters["question"].append(question)
    parameters["correct"].append(correct)

    all_answers = wrong + [correct]
    random.shuffle(all_answers)

    parameters["answer1"].append(all_answers[0])
    parameters["answer2"].append(all_answers[1])
    parameters["answer3"].append(all_answers[2])
    parameters["answer4"].append(all_answers[3])


parameters = {
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "correct": [],
    "score": [0],
    "index": [idx_start]
}

widgets = {
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

grid = QGridLayout()

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def start_game():
    clear_widgets()
    preload_data()
    frame2()

def show_frame1():
    clear_widgets()
    frame1()

def create_buttons(answer, l_marg, r_marg):
    button = QPushButton(answer)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "margin-left: " + str(l_marg) + "px;" +
        "margin-right: " + str(r_marg) + "px;" 
        "color: 'white';" +
        "font-family: Lucida Handwriting;" +
        "font-size: 16px;" +
        "border-radius: 25px;"
        "padding: 15px 0;" +
        "margin-top: 20px}" +
        "*:hover{background: '#BC006C'}" 
    )
    button.clicked.connect(lambda x: is_correct(answer))
    return button

def is_correct(answer):
    if answer == parameters["correct"][-1]:
        temp_score = parameters["score"].pop(-1)
        new_score = temp_score + 10
        parameters["score"] = [new_score]
        idx = parameters["index"].pop(-1)
        idx -= 1
        parameters["index"].append(idx)
        clear_widgets()
        frame3()
    else:
        clear_widgets()
        frame4()

#*********************************************
#                  FRAME 1 - START
#*********************************************

def frame1():
    #display logo
    image = QPixmap("pics/Title.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet("margin-top: 100px")
    
    widgets["logo"].append(logo)

    # button widget
    button = QPushButton("PLAY")
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 45px;"
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 0;" +
        "margin: 100px 200px;}" +
        "*:hover{background: '#BC006C';}"
    )
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)



#*********************************************
#                  FRAME 2 - ANSWER
#*********************************************

def frame2():
    score = QLabel(str(parameters["score"][-1]))
    score.setAlignment(Qt.AlignmentFlag.AlignCenter)
    score.setStyleSheet(
        "font-size: 35px;" +
        "color: 'white';" +
        "margin: 20px 200px;" +
        "padding: 20px;"
        "background: '#64A314';" +
        "border: 1px solid '#64A314';" +
        "border-radius: 40px;"
    )
    widgets["score"].append(score)

    question = QLabel(parameters["question"][-1])
    question.setAlignment(Qt.AlignmentFlag.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: Lucida Handwriting;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 75px;"
    )
    widgets["question"].append(question)

    button1 = create_buttons(parameters["answer1"][-1], 85, 5)
    button2 = create_buttons(parameters["answer2"][-1], 5, 85)
    button3 = create_buttons(parameters["answer3"][-1], 85, 5)
    button4 = create_buttons(parameters["answer4"][-1], 5, 85)
    
    widgets["awswer1"].append(button1)
    widgets["awswer2"].append(button2)
    widgets["awswer3"].append(button3)
    widgets["awswer4"].append(button4)
    
    game_image = QPixmap("pics/Title.png")
    logo = QLabel()
    logo.setPixmap(game_image)
    logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet("margin-top: 75px; margin-bottom: 30px;")
    widgets["logo"].append(logo)
    
    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["awswer1"][-1], 2, 0)
    grid.addWidget(widgets["awswer2"][-1], 2, 1)
    grid.addWidget(widgets["awswer3"][-1], 3, 0)
    grid.addWidget(widgets["awswer4"][-1], 3, 1)
    grid.addWidget(widgets["logo"][-1], 4, 0, 1, 2)

    

#*********************************************
#                  FRAME 3 - WIN GAME
#*********************************************

def frame3():
    #congradulations widget    
    message = QLabel("Congradulations! You\nare a true programmer!\n your score is:")
    message.setAlignment(Qt.AlignmentFlag.AlignRight)
    message.setStyleSheet(
        "font-family: 'Lucida Handwriting';" +
        "font-size: 25px;" +
        "color: 'white';" +
        "margin: 100px 0px;"
        )
    widgets["message"].append(message)

    #score widget
    score = QLabel(str(parameters["score"][-1]))
    score.setStyleSheet(
        "font-size: 100px;" +
        "color: #8FC740;" +
        "margin: 0px 75px 0px 75px;"
    )
    widgets["score"].append(score)

    #go back to work widget
    message2 = QLabel("OK. Now go back to WORK.")
    message2.setAlignment(Qt.AlignmentFlag.AlignCenter)
    message2.setStyleSheet(
        "font-family: 'Lucida Handwriting';" +
        "font-size: 30px;" +
        "color: 'white';" +
        "margin-top:0px;" +
        "margin-bottom:75px;"
    )
    widgets["message2"].append(message2)    
    
    #button widget
    button = QPushButton('TRY AGAIN')
    button.setStyleSheet(
        "*{background:'#BC006C';" +
        "padding:25px 0px;" +
        "border: 1px solid '#BC006C';" +
        "color: 'white';" +
        "font-family: 'Arial';" +
        "font-size: 25px;" +
        "border-radius: 40px;" +
        "margin: 10px 300px;}" +
        "*:hover{background:'#ff1b9e';}"
    )
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.clicked.connect(start_game)

    widgets["button"].append(button)

    #logo widget
    game_image = QPixmap("pics/Title.png")
    logo = QLabel()
    logo.setPixmap(game_image)
    logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet(
        "padding :10px;" +
        "margin-top:75px;" +
        "margin-bottom: 20px;"
    )
    widgets["logo"].append(logo)

    #place widgets on the grid
    grid.addWidget(widgets["message"][-1], 2, 0)
    grid.addWidget(widgets["score"][-1], 2, 1)
    grid.addWidget(widgets["message2"][-1], 3, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 4, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 5, 0, 2, 2)

#*********************************************
#                  FRAME 4 - FAIL
#*********************************************
def frame4():
    #sorry widget
    message = QLabel("Sorry, this answer \nwas wrong\n your score is:")
    message.setAlignment(Qt.AlignmentFlag.AlignRight)
    message.setStyleSheet(
        "font-family: 'Lucida Handwriting';" +
        "font-size: 35px;" +
        "color: 'white';" +
        "margin: 75px 5px;" +
        "padding:20px;"
    )
    widgets["message"].append(message)

    #score widget
    score = QLabel(str(parameters["score"][-1]))
    score.setStyleSheet(
        "font-size: 100px;" +
        "color: white;" +
        "margin: 0 75px 0px 75px;"
    )
    widgets["score"].append(score)

    #button widget
    button = QPushButton('TRY AGAIN')
    button.setStyleSheet(
        "*{padding: 25px 0px;" +
        "background: '#BC006C';" +
        "color: 'white';" +
        "font-family: 'Arial';" +
        "font-size: 35px;" +
        "border-radius: 40px;" +
        "margin: 10px 200px;}" +
        "*:hover{background: '#ff1b9e';}"
    )
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.clicked.connect(start_game)

    widgets["button"].append(button)

    #logo widget
    game_image = QPixmap("pics/Title.png")
    logo = QLabel()
    logo.setPixmap(game_image)
    logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet(
        "margin-top: 75px;" +
        "padding :10px"
    )
    widgets["logo"].append(logo)
    
    #place widgets on the grid
    grid.addWidget(widgets["message"][-1], 1, 0)
    grid.addWidget(widgets["score"][-1], 1, 1)
    grid.addWidget(widgets["button"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 3, 0, 1, 2)
    