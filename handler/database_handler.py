from PyQt5.QtCore import QThread, pyqtSignal
from requests import get, post, exceptions


class DataHandler(QThread):  # class that forms requests to the server based on user actions
    signal = pyqtSignal(str)

    def __init__(self):
        super(DataHandler, self).__init__()
        self.previous_send = 0

    def user_authorization(self, username, password):
        try:
            result = get("http://127.0.0.1:5000/authorization", params={"username": username, "password": password})

            if result.json()[0]:
                self.signal.emit("ok")
            else:
                self.signal.emit("Incorrect login or password")

        except exceptions.ConnectionError:
            self.signal.emit("Server is not available")

    def user_registration(self, username, password):
        try:
            info = {"username": username, "password": password}
            result = post("http://127.0.0.1:5000/registration", json=info)

            if result:
                print(f'Successfully registration by {username}')
                self.signal.emit(f'User {username} succesfully registered')
            else:
                self.signal.emit(f'User with name {username} already exists')

        except exceptions.ConnectionError:
            self.signal.emit("Server is not available")

    def user_deletion(self, username):
        try:
            info = {"username": username}
            post("http://127.0.0.1:5000/deletion", json=info)

        except exceptions.ConnectionError:
            self.signal.emit("Server is not available")

    def send_message(self, username, message):
        info = {"username": username, "message": message}

        try:
            post("http://127.0.0.1:5000/upload_message", json=info)

        except exceptions.ConnectionError:
            self.signal.emit("Server is not available")

    def new_messages(self):
        try:
            result = get("http://127.0.0.1:5000/load_messages",
                         params={"previous_send": self.previous_send}).json()["messages"]
            self.previous_send = result[-1][3]  # we request messages that appeared after the previous request
            return result

        except IndexError or exceptions.ConnectionError:
            return
