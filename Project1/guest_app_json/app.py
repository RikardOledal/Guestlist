import sys

from PyQt6.QtWidgets import QApplication

from guest_app import MainWindow, GuestService

guests_filename = "C:/Users/user/Python/Python-Rikard/Project1/guest_app/save_files/guests.json"

def main():
    print("Welcome to Guests 1.0.0")

    app = QApplication(sys.argv)

    guests_service = GuestService(guests_filename)

    win = MainWindow(guests_service)
    win.show()

    return app.exec()




if __name__ == "__main__":
    main()