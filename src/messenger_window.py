# this file is generated in QtDesign and is used as a template

from PyQt5 import QtCore, QtGui, QtWidgets
import icons.resources_mess


class MessengerUi(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(640, 480)
        main_window.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 "
                                  "rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #2de2e6, "
                                  "stop:1 #ECC6A2);\n"
                                  "font-family: Ubuntu")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.user_icon = QtWidgets.QLabel(self.centralwidget)
        self.user_icon.setStyleSheet("background-color: none;\n"
                                     "border: none;")
        self.user_icon.setText("")
        self.user_icon.setPixmap(QtGui.QPixmap(":/newPrefix/person.svg"))
        self.user_icon.setObjectName("user_icon")
        self.gridLayout.addWidget(self.user_icon, 0, 0, 1, 1)
        self.username_field = QtWidgets.QLabel(self.centralwidget)
        self.username_field.setStyleSheet("background-color: none;\n"
                                          "border: none;\n"
                                          "font-size: 14pt;")
        self.username_field.setObjectName("username_field")
        self.gridLayout.addWidget(self.username_field, 0, 1, 1, 1)
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exit_button = QtWidgets.QPushButton(self.frame_1)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("QPushButton {\n"
                                       "color: black;\n"
                                       "background-color: none;\n"
                                       "border: none;\n"
                                       "font-size: 12 pt;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "color: white;\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "color: white;\n"
                                       "background-color: rgba(255, 255, 255, 70);\n"
                                       "border: 1px solid rgba(255, 255, 255, 80);\n"
                                       "border-radius: 3px;\n"
                                       "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logout.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QtCore.QSize(24, 24))
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout.addWidget(self.exit_button)
        self.delete_button = QtWidgets.QPushButton(self.frame_1)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("QPushButton {\n"
                                         "color: black;\n"
                                         "background-color: none;\n"
                                         "border: none;\n"
                                         "font-size: 12 pt;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "color: white;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "color: white;\n"
                                         "background-color: rgba(255, 255, 255, 70);\n"
                                         "border: 1px solid rgba(255, 255, 255, 80);\n"
                                         "border-radius: 3px;\n"
                                         "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setIconSize(QtCore.QSize(24, 24))
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.gridLayout.addWidget(self.frame_1, 0, 2, 1, 1)
        self.chat = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.chat.setFont(font)
        self.chat.setStyleSheet("background-color: rgba(255, 255, 255, 70);\n"
                                "border: 2px solid rgba(255, 255, 255, 80);\n"
                                "border-radius: 10px;")
        self.chat.setObjectName("chat")
        self.gridLayout.addWidget(self.chat, 1, 0, 1, 3)
        self.message_field = QtWidgets.QLineEdit(self.centralwidget)
        self.message_field.setMinimumSize(QtCore.QSize(0, 197))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.message_field.setFont(font)
        self.message_field.setStyleSheet("background-color: rgba(255, 255, 255, 70);\n"
                                         "border: 2px solid rgba(255, 255, 255, 80);\n"
                                         "border-radius: 10px;")
        self.message_field.setObjectName("message_field")
        self.gridLayout.addWidget(self.message_field, 2, 0, 1, 3)
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.send_button.setFont(font)
        self.send_button.setStyleSheet("QPushButton {\n"
                                       "color: black;\n"
                                       "background-color: none;\n"
                                       "border: none;\n"
                                       "font-size: 20 pt;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "color: white;\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "color: white;\n"
                                       "background-color: rgba(255, 255, 255, 70);\n"
                                       "border: 1px solid rgba(255, 255, 255, 80);\n"
                                       "border-radius: 3px;\n"
                                       "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/write.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_button.setIcon(icon2)
        self.send_button.setIconSize(QtCore.QSize(24, 24))
        self.send_button.setObjectName("send_button")
        self.gridLayout.addWidget(self.send_button, 3, 2, 1, 1)
        main_window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "SPU Messenger"))
        self.username_field.setText(_translate("main_window", "username"))
        self.exit_button.setText(_translate("main_window", "Exit"))
        self.delete_button.setText(_translate("main_window", "Delete account"))
        self.chat.setPlaceholderText(_translate("main_window", "No one sent a message. Be first!"))
        self.message_field.setPlaceholderText(_translate("main_window", "Type your text here"))
        self.send_button.setText(_translate("main_window", "Send message"))
