import sqlite3
from urllib.request import urlopen
import json
import pandas as pd

db_filename = "game.db"

def main():
    print("Creating database")

    db = sqlite3.connect(db_filename)

    c = db.cursor()

    c.execute("""CREATE TABLE questions (
        quiz text,
        question text,
        correct_answer text,
        wrong_answer1 text,
        wrong_answer2 text,
        wrong_answer3 text,
        picture text
        )""")

    db.commit()
    db.close()

def add_question(quiz, question, correct_answer, wrong_answer1, wrong_answer2, wrong_answer3, picture):
    print("Lägger till frågor")

    conn = sqlite3.connect(db_filename)

    c = conn.cursor()

    c.execute("INSERT INTO questions VALUES (:quiz, :question, :correct_answer, :wrong_answer1, :wrong_answer2, :wrong_answer3, :picture)", {
        "quiz": quiz,
        "question": question,
        "correct_answer": correct_answer,
        "wrong_answer1": wrong_answer1,
        "wrong_answer2": wrong_answer2,
        "wrong_answer3": wrong_answer3,
        "picture": picture
    })
    conn.commit()
    conn.close()
    print("Databas stängd")

def select_questions():
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    c.execute("SELECT * FROM questions WHERE quiz='Namn'")
    question = []
    correct_answer = []
    wrong_answer1 = []
    wrong_answer2 = []
    wrong_answer3 = []
    picture = []
    
    for i in c.fetchall():
        question.append(i[1])
        correct_answer.append(i[2])
        wrong_answer1.append(i[3])
        wrong_answer2.append(i[4])
        wrong_answer3.append(i[5])
        picture.append(i[6])
    
    print("Frågor")
    print(question)
    print("Rätt svar")
    print(correct_answer)
    print("Fel svar")
    print(wrong_answer1)
    print(wrong_answer2)
    print(wrong_answer3)
    print("Bilder")
    print(picture)

    conn.commit()
    conn.close()

def temp_func():
    question_list = []
    correct_list = []
    wrong_answer1_list = []
    wrong_answer2_list = []
    wrong_answer3_list = []

    with urlopen("https://opentdb.com/api.php?amount=10&category=20&difficulty=easy&type=multiple") as webpage:
        j_data = json.loads(webpage.read().decode())
        df = pd.DataFrame(j_data["results"])

        i = 1
        while i < 10:
            a = df["question"][i]
            b = df["correct_answer"][i]
            c = df["incorrect_answers"][i]
#
            question_list.append(a)
            correct_list.append(b)
            wrong_answer1_list.append(c[0])
            wrong_answer2_list.append(c[1])
            wrong_answer3_list.append(c[2])

            i += 1
        
    for question in question_list:
        add_question("Mythology", question_list[question_list.index(question)], correct_list[question_list.index(question)], wrong_answer1_list[question_list.index(question)], wrong_answer2_list[question_list.index(question)], wrong_answer3_list[question_list.index(question)], "Title.png")
        print(question_list[-1])
        print(question)
if __name__ == "__main__":
    temp_func()