from PyQt5.QtWidgets import QMainWindow, QMessageBox

from handler.database_handler import DataHandler
from src.authorization_window import AuthorizationUi


def check_input(func):  # decorator that checks fields for emptiness
    def wrapper(self):
        if len(self.ui.login.text()) == 0:
            return
        if len(self.ui.password.text()) == 0:
            return
        func(self)

    return wrapper


class Authorization(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = AuthorizationUi()
        self.ui.setup_ui(self)

        self.ui.sign_in.clicked.connect(self.authorization)
        self.ui.sign_up.clicked.connect(self.registration)

        self.data_handler = DataHandler()
        self.data_handler.signal.connect(self.signal_handler)

        self.successful_authorization = False  # indicator of successful authorization

        self.username = ""
        self.password = ""

    def signal_handler(self, value):
        if value == 'ok':
            self.successful_authorization = True
            self.close()
            return
        QMessageBox.about(self, "Error", value)
        # pop-up window in case of error
        # qt.qpa.xcb: QXcbConnection: XCB
        # error: 3(BadWindow), sequence: 864, resource
        # id: 11268920, major
        # code: 40(TranslateCoords), minor
        # code: 0
        # idk how to fix it (maybe only on ubuntu)

    @check_input
    def authorization(self):
        self.username = self.ui.login.text()
        self.password = self.ui.password.text()
        self.data_handler.user_authorization(self.username, self.password)

    @check_input
    def registration(self):
        self.username = self.ui.login.text()
        self.password = self.ui.password.text()
        self.data_handler.user_registration(self.username, self.password)
