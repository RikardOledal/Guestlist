import datetime as dt

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

        with open("logs.txt", "a") as f:
            f.write(f"[{dt.datetime.now()}]: {msg}\n")

raise CustomException("It's a custom exception time")
