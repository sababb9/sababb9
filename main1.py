from PyQt5 import QtCore, QtGui, QtWidgets
from customers import customers_window
import sqlite3

class login_page(object):
    def close_login(self):
        MainWindow.show()
        ui.loginwindow.hide()
    def setupUi(self, login_page):
        login_page.setObjectName("login_page")
        login_page.resize(600, 400)
        login_page.setMinimumSize(QtCore.QSize(600, 400))
        login_page.setMaximumSize(QtCore.QSize(600, 400))
        login_page.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(login_page)
        self.centralwidget.setObjectName("centralwidget")
        self.login_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.login_tab.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.login_tab.setMinimumSize(QtCore.QSize(600, 400))
        self.login_tab.setMaximumSize(QtCore.QSize(600, 400))
        self.login_tab.setStyleSheet("font: 75 12pt \"Orbitron\";\n"
"background-color: rgb(163, 200, 138);\n"
"border-radius:10px;\n"
"")
        self.login_tab.setObjectName("login_tab")
        self.customers = QtWidgets.QWidget()
