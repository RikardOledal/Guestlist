import sys

from PyQt6.QtWidgets import QApplication

from inside import main_window, economic

contacts_filename = "contacts.sqlite3"


def main():
    print("Welcome to HomeEconomics 1.0.0")

    app = QApplication(sys.argv)

    contacts_service = ContactsSecervice(contacts_filename)

    win = MainWindow(contacts_service)
    win.show()

    return app.exec()


if __name__ == "__main__":
    main()