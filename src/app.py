import sys
from PyQt5.QtWidgets import QApplication
from src.authorization_class import Authorization
from src.messenger_class import Messenger


def launch_messenger(username):
    app = QApplication(sys.argv)
    messenger_window = Messenger(username)
    messenger_window.show()
    sys.exit(app.exec_())


def launch_app():
    app = QApplication(sys.argv)
    authorization_window = Authorization()
    authorization_window.show()
    app.exec_()

    if authorization_window.successful_authorization:
        launch_messenger(authorization_window.username)
