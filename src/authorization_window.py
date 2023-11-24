# this file is generated in QtDesign and is used as a template

from PyQt5 import QtCore, QtGui, QtWidgets
import icons.resources_auth


class AuthorizationUi(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(320, 240)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        main_window.setFont(font)
        main_window.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 "
                                  "rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #2de2e6, "
                                  "stop:1 #ECC6A2);\n"
                                  "font-family: Ubuntu")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.login.setFont(font)
        self.login.setStyleSheet("background-color: rgba(255, 255, 255, 70);\n"
                                 "border: 2px solid rgba(255, 255, 255, 80);\n"
                                 "border-radius: 5px;")
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 0, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgba(255, 255, 255, 70);\n"
                                    "border: 2px solid rgba(255, 255, 255, 80);\n"
                                    "border-radius: 5px;")
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 0, 1, 1)
        self.sign_in = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.sign_in.setFont(font)
        self.sign_in.setStyleSheet("QPushButton {\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/login.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sign_in.setIcon(icon)
        self.sign_in.setIconSize(QtCore.QSize(24, 24))
        self.sign_in.setAutoRepeatInterval(100)
        self.sign_in.setObjectName("sign_in")
        self.gridLayout.addWidget(self.sign_in, 2, 0, 1, 1)
        self.sign_up = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.sign_up.setFont(font)
        self.sign_up.setStyleSheet("QPushButton {\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/person_add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sign_up.setIcon(icon1)
        self.sign_up.setIconSize(QtCore.QSize(24, 24))
        self.sign_up.setObjectName("sign_up")
        self.gridLayout.addWidget(self.sign_up, 3, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Authorization"))
        self.login.setPlaceholderText(_translate("main_window", "Login"))
        self.password.setPlaceholderText(_translate("main_window", "Password"))
        self.sign_in.setText(_translate("main_window", "Sign In"))
        self.sign_up.setText(_translate("main_window", "Sign Up"))
