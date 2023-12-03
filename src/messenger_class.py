from datetime import datetime
from math import floor
from threading import Thread
from time import sleep

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow

from handler.database_handler import DataHandler
from src.messenger_window import MessengerUi


def check_input(func):  # decorator that checks fields for emptiness
    def wrapper(self):
        if len(self.message_field.text()) == 0:
            return
        func(self)

    return wrapper


class Messenger(MessengerUi, QMainWindow):
    def __init__(self, username=0):
        super(Messenger, self).__init__()
        self.setup_ui(self)

        self.username = username
        self.message = ""

        self.set_send_button()
        self.set_exit_button()
        self.set_delete_button()
        self.set_username_field()

        self.data_handler = DataHandler()
        Thread(target=self.refresh_messages).start()  # we launch a parallel thread that regularly updates messages

    def set_username_field(self):
        self.username_field.setText(self.username)  # put username in top of window

    def set_send_button(self):
        self.send_button.setShortcut(QKeySequence("Return"))  # set hotkeys combination for sending message
        self.send_button.clicked.connect(self.send_message)

    def set_exit_button(self):
        self.exit_button.setShortcut(QKeySequence("Ctrl+Shift+Q"))  # set hotkey for exit
        self.exit_button.clicked.connect(self.exit)

    def set_delete_button(self):
        self.delete_button.clicked.connect(self.delete_account)

    @check_input
    def send_message(self):
        self.message = self.message_field.text()
        self.data_handler.send_message(self.username, self.message)
        self.message_field.setText("")

    def print_message(self, info):
        username = info[1]
        message = info[2]
        time = datetime.fromtimestamp(floor(info[3]))
        self.chat.append(f'{username} [{time}]:')
        self.chat.append(message)  # QObject::connect: Cannot queue arguments of type 'QTextCursor'
        self.chat.append("")  # (Make sure 'QTextCursor' is registered using qRegisterMetaType().)
        # idk how to fix it

    def refresh_messages(self):
        while True:
            new_messages = self.data_handler.new_messages()
            if new_messages:
                for info in new_messages:
                    self.print_message(info)
            sleep(0.2)  # let make requests every 200ms

    def delete_account(self):
        self.close()
        self.data_handler.user_deletion(self.username)

    def exit(self):
        self.close()
