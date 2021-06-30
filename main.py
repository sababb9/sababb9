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
        self.customers.setStyleSheet("background-color: rgb(141, 200, 140);")
        self.customers.setObjectName("customers")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.customers)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 50, 391, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineedit_user_customers = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineedit_user_customers.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineedit_user_customers.setPlaceholderText("")
        self.lineedit_user_customers.setObjectName("lineedit_user_customers")
        self.verticalLayout.addWidget(self.lineedit_user_customers)
        self.lineedit_password_customers = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineedit_password_customers.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineedit_password_customers.setObjectName("lineedit_password_customers")
        self.lineedit_password_customers.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.lineedit_password_customers)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.customers)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 50, 100, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_custimers_user = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_custimers_user.setObjectName("label_custimers_user")
        self.verticalLayout_2.addWidget(self.label_custimers_user)
        self.label_customers_password = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_customers_password.setObjectName("label_customers_password")
        self.verticalLayout_2.addWidget(self.label_customers_password)
        self.login_btn_customers = QtWidgets.QPushButton(self.customers)
        self.login_btn_customers.setGeometry(QtCore.QRect(240, 172, 261, 41))
        self.login_btn_customers.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 75 14pt \"Orbitron\";")
        self.login_btn_customers.setObjectName("login_btn_customers")
        self.login_btn_customers.clicked.connect(self.login_func_customers)
        self.back_btn_customers = QtWidgets.QPushButton(self.customers)
        self.back_btn_customers.setGeometry(QtCore.QRect(10, 300, 75, 23))
        self.back_btn_customers.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.back_btn_customers.setObjectName("back_btn_customers")
        self.back_btn_customers.clicked.connect(self.close_login)
        self.label_state_customers = QtWidgets.QLabel(self.customers)
        self.label_state_customers.setGeometry(QtCore.QRect(180, 20, 351, 20))
        self.label_state_customers.setText("")
        self.label_state_customers.setObjectName("label_state_customers")
        self.login_tab.addTab(self.customers, "")
        self.employee = QtWidgets.QWidget()
        self.employee.setStyleSheet("background-color: rgb(200, 181, 182);")
        self.employee.setObjectName("employee")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.employee)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(160, 60, 381, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineedit_seller_username = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineedit_seller_username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineedit_seller_username.setObjectName("lineedit_seller_username")
        self.verticalLayout_3.addWidget(self.lineedit_seller_username)
        self.lineedit_seller_password = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineedit_seller_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineedit_seller_password.setObjectName("lineedit_seller_password")
        self.verticalLayout_3.addWidget(self.lineedit_seller_password)
        self.login_btn_seller = QtWidgets.QPushButton(self.employee)
        self.login_btn_seller.setGeometry(QtCore.QRect(230, 170, 231, 41))
        self.login_btn_seller.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.login_btn_seller.setObjectName("login_btn_seller")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.employee)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(50, 59, 101, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_seller_username = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_seller_username.setObjectName("label_seller_username")
        self.verticalLayout_4.addWidget(self.label_seller_username)
        self.lablel_seller_password = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.lablel_seller_password.setObjectName("lablel_seller_password")
        self.verticalLayout_4.addWidget(self.lablel_seller_password)
        self.Back_btn_seller = QtWidgets.QPushButton(self.employee)
        self.Back_btn_seller.setGeometry(QtCore.QRect(10, 300, 75, 23))
        self.Back_btn_seller.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Back_btn_seller.setObjectName("Back_btn_seller")
        self.Back_btn_seller.clicked.connect(self.close_login)
        self.label_state_seller = QtWidgets.QLabel(self.employee)
        self.label_state_seller.setGeometry(QtCore.QRect(160, 30, 381, 20))
        self.label_state_seller.setText("")
        self.label_state_seller.setObjectName("label_state_seller")
        self.login_tab.addTab(self.employee, "")
        self.Management = QtWidgets.QWidget()
        self.Management.setObjectName("Management")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.Management)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(160, 59, 401, 91))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineedit_operator_username = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineedit_operator_username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineedit_operator_username.setObjectName("lineedit_operator_username")
        self.verticalLayout_5.addWidget(self.lineedit_operator_username)
        self.lineedit_operator_password = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineedit_operator_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineedit_operator_password.setObjectName("lineedit_operator_password")
        self.verticalLayout_5.addWidget(self.lineedit_operator_password)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.Management)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(50, 60, 100, 91))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_oparator_username = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_oparator_username.setObjectName("label_oparator_username")
        self.verticalLayout_6.addWidget(self.label_oparator_username)
        self.label_operator_password = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_operator_password.setObjectName("label_operator_password")
        self.verticalLayout_6.addWidget(self.label_operator_password)
        self.login_btn_operator = QtWidgets.QPushButton(self.Management)
        self.login_btn_operator.setGeometry(QtCore.QRect(240, 160, 231, 41))
        self.login_btn_operator.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"border-radius:10px;")
        self.login_btn_operator.setObjectName("login_btn_operator")
        self.Back_btn_operator = QtWidgets.QPushButton(self.Management)
        self.Back_btn_operator.setGeometry(QtCore.QRect(10, 300, 75, 23))
        self.Back_btn_operator.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.Back_btn_operator.setObjectName("Back_btn_operator")
        self.Back_btn_operator.clicked.connect(self.close_login)
        self.label_state_operator = QtWidgets.QLabel(self.Management)
        self.label_state_operator.setGeometry(QtCore.QRect(160, 40, 401, 20))
        self.label_state_operator.setText("")
        self.label_state_operator.setObjectName("label_state_operator")
        self.login_tab.addTab(self.Management, "")
        login_page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login_page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        login_page.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login_page)
        self.statusbar.setObjectName("statusbar")
        login_page.setStatusBar(self.statusbar)

        self.retranslateUi(login_page)
        self.login_tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(login_page)

    def retranslateUi(self, login_page):
        _translate = QtCore.QCoreApplication.translate
        login_page.setWindowTitle(_translate("login_page", "MainWindow"))
        self.label_custimers_user.setText(_translate("login_page", "User Name"))
        self.label_customers_password.setText(_translate("login_page", "Password"))
        self.login_btn_customers.setText(_translate("login_page", "Login"))
        self.back_btn_customers.setText(_translate("login_page", "Back"))
        self.login_tab.setTabText(self.login_tab.indexOf(self.customers), _translate("login_page", "customers"))
        self.login_btn_seller.setText(_translate("login_page", "Login"))
        self.label_seller_username.setText(_translate("login_page", "User Name"))
        self.lablel_seller_password.setText(_translate("login_page", "Password"))
        self.Back_btn_seller.setText(_translate("login_page", "Back"))
        self.login_tab.setTabText(self.login_tab.indexOf(self.employee), _translate("login_page", "Seller"))
        self.label_oparator_username.setText(_translate("login_page", "User Name"))
        self.label_operator_password.setText(_translate("login_page", "Password"))
        self.login_btn_operator.setText(_translate("login_page", "Login"))
        self.Back_btn_operator.setText(_translate("login_page", "Back"))
        self.login_tab.setTabText(self.login_tab.indexOf(self.Management), _translate("login_page", "Operator"))
    
    def login_func_customers(self):
        self.customer_name=self.lineedit_user_customers.text()
        self.customer_password=self.lineedit_password_customers.text()
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM customers;''')
        rows = c.fetchall()
        for row in rows:
            if row[1]==self.customer_name and row[2]==self.customer_password:
                self.label_state_customers.setText("login soccesful")
                conn.close()
                self.window=QtWidgets.QMainWindow()
                self.cu_ui=customers_window(self.customer_name)
                self.cu_ui.setupUi(self.window)
                self.window.show()
                ui.loginwindow.hide()
                return
        self.label_state_customers.setText("login failed!")
        conn.close()  
    




class sign_up(object):
    def  close_signup(self):
        MainWindow.show()
        ui.signupwindow.hide()
        
    def setupUi(self, sign_up):
        sign_up.setObjectName("sign_up")
        sign_up.resize(600, 400)
        sign_up.setMinimumSize(QtCore.QSize(600, 400))
        sign_up.setMaximumSize(QtCore.QSize(600, 400))
        sign_up.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(sign_up)
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
        self.customers.setStyleSheet("background-color: rgb(141, 200, 140);")
        self.customers.setObjectName("customers")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.customers)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 50, 391, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineedit_username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineedit_username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineedit_username.setPlaceholderText("")
        self.lineedit_username.setObjectName("lineedit_username")
        self.verticalLayout.addWidget(self.lineedit_username)
        self.lineEdit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.customers)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 50, 100, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_username = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_username.setObjectName("label_username")
        self.verticalLayout_2.addWidget(self.label_username)
        self.label_password = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_password.setObjectName("label_password")
        self.verticalLayout_2.addWidget(self.label_password)
        self.signup_btn = QtWidgets.QPushButton(self.customers)
        self.signup_btn.setGeometry(QtCore.QRect(240, 172, 261, 41))
        self.signup_btn.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 75 14pt \"Orbitron\";")
        self.signup_btn.setObjectName("signup_btn")
        self.signup_btn.clicked.connect(self.signup_func)
        self.label_state = QtWidgets.QLabel(self.customers)
        self.label_state.setGeometry(QtCore.QRect(170, 20, 381, 20))
        self.label_state.setText("")
        self.label_state.setObjectName("label_state")
        self.back_btn = QtWidgets.QPushButton(self.customers)
        self.back_btn.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.back_btn.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(self.close_signup)
        self.login_tab.addTab(self.customers, "")
        sign_up.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sign_up)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        sign_up.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sign_up)
        self.statusbar.setObjectName("statusbar")
        sign_up.setStatusBar(self.statusbar)

        self.retranslateUi(sign_up)
        self.login_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(sign_up)

    def retranslateUi(self, signup):
        _translate = QtCore.QCoreApplication.translate
        signup.setWindowTitle(_translate("signup", "MainWindow"))
        self.label_username.setText(_translate("signup", "User Name"))
        self.label_password.setText(_translate("signup", "Password"))
        self.signup_btn.setText(_translate("signup", "sign up"))
        self.back_btn.setText(_translate("signup", "Back"))
        self.login_tab.setTabText(self.login_tab.indexOf(self.customers), _translate("signup", "customers"))
    
    def signup_func(self):
        self.username=self.lineedit_username.text()
        self.password=self.lineEdit_password.text()
        if len(self.username)>15 or len(self.username)<5:
            self.label_state.setText("username is too long or too short!")
            return
        elif len(self.password)>15 or len(self.password)<5:
            self.label_state.setText("password is too long or too short!")
            return
        elif ' ' in self.username or ' ' in self.password:
            self.label_state.setText("invalid username or password!")
            return 
        
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM customers;''')
        row =c.fetchall()
        
        ID='CU'+str(int(row[-1][0][2:])+1)
        first=5
        email=''
        try:
            sqlite_insert_with_param = """INSERT INTO customers(id, username,password,wallet,email,address) 
                          VALUES (?, ?, ?, ?,?,?);"""
            c.execute(sqlite_insert_with_param,(ID,self.username,self.password,first,email,email)) 
            conn.commit()
            conn.close()
            self.label_state.setText("your account is added")
            self.window=QtWidgets.QMainWindow()
            self.cu_ui=customers_window(self.username)
            self.cu_ui.setupUi(self.window)
            self.window.show()
            ui.signupwindow.hide()
        except sqlite3.Error as error:
            conn.close()
            self.label_state.setText("your username taken before") 



class Ui_MainWindow(object):
    def open_login(self):
        self.loginwindow=QtWidgets.QMainWindow()
        self.login=login_page()
        self.login.setupUi(self.loginwindow)
        self.loginwindow.show()
        MainWindow.hide()
        
    def open_signup(self):
        self.signupwindow=QtWidgets.QMainWindow()
        self.signup=sign_up()
        self.signup.setupUi(self.signupwindow)
        self.signupwindow.show()
        MainWindow.hide() 
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(0, 0, 900, 900))
        self.main_label.setMinimumSize(QtCore.QSize(900, 900))
        self.main_label.setMaximumSize(QtCore.QSize(900, 900))
        self.main_label.setStyleSheet("background-color: rgb(203, 255, 252);")
        self.main_label.setText("")
        self.main_label.setObjectName("main_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(129, 429, 541, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.login_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.login_btn.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 75 16pt \"Orbitron\";\n"
"border-radius: 10px;\n"
"")
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)
        
        
        self.login_btn.clicked.connect(self.open_login)
        
        self.signup_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.signup_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.signup_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.signup_btn.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 75 16pt \"Orbitron\";\n"
"border-radius: 10px;\n"
"")
        self.signup_btn.setObjectName("signup_btn")
        self.horizontalLayout.addWidget(self.signup_btn)
        
        self.signup_btn.clicked.connect(self.open_signup)
        
        self.pix_label = QtWidgets.QLabel(self.centralwidget)
        self.pix_label.setGeometry(QtCore.QRect(100, 20, 600, 400))
        self.pix_label.setMinimumSize(QtCore.QSize(600, 400))
        self.pix_label.setMaximumSize(QtCore.QSize(600, 400))
        self.pix_label.setText("")
        self.pix_label.setPixmap(QtGui.QPixmap("../images/ims.jpg"))
        self.pix_label.setObjectName("pix_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) #commit

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.signup_btn.setText(_translate("MainWindow", "sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class customers_window(object):
    def __init__(self,username):
        self.username=username
    def setupUi(self, customer_window):
        customer_window.setObjectName("customer_window")
        customer_window.resize(1250, 600)
        customer_window.setMinimumSize(QtCore.QSize(1250, 600))
        customer_window.setMaximumSize(QtCore.QSize(1250, 600))
        customer_window.setStyleSheet("background-color: rgb(176, 255, 222);")
        self.centralwidget = QtWidgets.QWidget(customer_window)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 235, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 75 20pt \"Orbitron\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.table_information = QtWidgets.QFormLayout()
        self.table_information.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.table_information.setContentsMargins(5, 5, 5, 5)
        self.table_information.setHorizontalSpacing(5)
        self.table_information.setVerticalSpacing(35)
        self.table_information.setObjectName("table_information")
        self.id_label = QtWidgets.QLabel(self.layoutWidget)
        self.id_label.setObjectName("id_label")
        self.table_information.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.id_label)
        self.id_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.id_label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Orbitron\";")
        self.id_label_2.setText("")
        self.id_label_2.setObjectName("id_label_2")
        self.table_information.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.id_label_2)
        self.username_label = QtWidgets.QLabel(self.layoutWidget)
        self.username_label.setObjectName("username_label")
        self.table_information.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.lineEdit_username = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.table_information.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_username)
        self.password_label = QtWidgets.QLabel(self.layoutWidget)
        self.password_label.setObjectName("password_label")
        self.table_information.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.table_information.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        self.Email_label = QtWidgets.QLabel(self.layoutWidget)
        self.Email_label.setObjectName("Email_label")
        self.table_information.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Email_label)
        self.lineEdit_email = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.table_information.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_email)
        self.address_label = QtWidgets.QLabel(self.layoutWidget)
        self.address_label.setObjectName("address_label")
        self.table_information.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.address_label)
        self.lineEdit_address = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_address.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.table_information.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_address)
        self.wallet_label = QtWidgets.QLabel(self.layoutWidget)
        self.wallet_label.setObjectName("wallet_label")
        self.table_information.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.wallet_label)
        self.Wallet_show_label = QtWidgets.QLabel(self.layoutWidget)
        self.Wallet_show_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Orbitron\";")
        self.Wallet_show_label.setText("")
        self.Wallet_show_label.setObjectName("Wallet_show_label")
        self.table_information.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Wallet_show_label)
        self.verticalLayout.addLayout(self.table_information)
        self.edit_info_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.edit_info_btn.setStyleSheet("font: 75 12pt \"Orbitron\";\n"
"background-color: rgb(0, 170, 0);")
        self.edit_info_btn.setObjectName("edit_info_btn")
        self.verticalLayout.addWidget(self.edit_info_btn)
        self.state_edit = QtWidgets.QLabel(self.layoutWidget)
        self.state_edit.setStyleSheet("font: 75 9pt \"Orbitron\";")
        self.state_edit.setText("")
        self.state_edit.setObjectName("state_edit")
        self.verticalLayout.addWidget(self.state_edit)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(950, 440, 281, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.product_btn= QtWidgets.QPushButton(self.layoutWidget1)
        self.product_btn.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"font: 75 8pt \"Orbitron\";")
        self.product_btn.setObjectName("product_btn")
        self.verticalLayout_2.addWidget(self.product_btn)
        self.shop_list_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.shop_list_btn.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 8pt \"Orbitron\";")
        self.shop_list_btn.setObjectName("shop_list_btn")
        self.shop_list_btn.clicked.connect(self.shop_products)
        self.verticalLayout_2.addWidget(self.shop_list_btn)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(830, 0, 411, 431))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"Orbitron\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.layoutWidget2)
        self.tableWidget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 255, 0);\n"
"gridline-color: rgb(85, 255, 255);")
        self.tableWidget_3.setRowCount(20)
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setObjectName("tableWidget_3")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.verticalLayout_4.addWidget(self.tableWidget_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 0, 107, 16))
        self.label_2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"Orbitron\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 220, 147, 16))
        self.label_3.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"Orbitron\";")
        self.label_3.setObjectName("label_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(270, 241, 541, 181))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(85, 255, 255);\n"
"alternate-background-color: rgb(0, 255, 0);")
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(270, 20, 421, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(85, 255, 255);\n"
"alternate-background-color: rgb(0, 255, 0);")
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(400, 490, 221, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.charge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.charge_btn.setGeometry(QtCore.QRect(500, 530, 121, 31))
        self.charge_btn.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.charge_btn.setObjectName("charge_btn")
        customer_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(customer_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 21))
        self.menubar.setObjectName("menubar")
        customer_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(customer_window)
        self.statusbar.setObjectName("statusbar")
        customer_window.setStatusBar(self.statusbar)
        self.show_info(self.username)
        self.show_favorite(self.username)
        self.show_Previous(self.username)
        self.edit_info_btn.clicked.connect(lambda: self.edit_info(self.username))
        self.charge_btn.clicked.connect(self.charge)
        self.product_btn.clicked.connect(self.show_products)

        self.retranslateUi(customer_window)
        QtCore.QMetaObject.connectSlotsByName(customer_window)

    def retranslateUi(self, customer_window):
        _translate = QtCore.QCoreApplication.translate
        customer_window.setWindowTitle(_translate("customer_window", "MainWindow"))
        self.label.setText(_translate("customer_window", "Information"))
        self.id_label.setText(_translate("customer_window", "ID"))
        self.username_label.setText(_translate("customer_window", "UserName"))
        self.password_label.setText(_translate("customer_window", "Password"))
        self.Email_label.setText(_translate("customer_window", "Email"))
        self.address_label.setText(_translate("customer_window", "Address"))
        self.wallet_label.setText(_translate("customer_window", "Wallet"))
        self.edit_info_btn.setText(_translate("customer_window", "Edit info with new data"))
        self.product_btn.setText(_translate("customer_window", "Show Product"))
        self.shop_list_btn.setText(_translate("customer_window", "Shop list"))
        self.label_4.setText(_translate("customer_window", "Shopping List"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("customer_window", "ID"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("customer_window", "Name"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("customer_window", "Price"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("customer_window", "Seller"))
        self.label_2.setText(_translate("customer_window", "My Favorite List "))
        self.label_3.setText(_translate("customer_window", "Previous Shopping List"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("customer_window", "Product Id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("customer_window", "Product Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("customer_window", "Seller Id"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("customer_window", "Seller Name"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("customer_window", "Price"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("customer_window", "Product Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("customer_window", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("customer_window", "Seller"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("customer_window", "Price"))
        self.lineEdit.setPlaceholderText(_translate("customer_window", "Enter The Amount of charge"))
        self.charge_btn.setText(_translate("customer_window", "Charge"))

    def show_info(self,username):
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_select_query = """select * from customers where username = ?"""
        c.execute(sql_select_query, (username,))
        row_info = c.fetchall()
        self.id_label_2.setText(row_info[0][0])
        self.lineEdit_username.setText(row_info[0][1])
        self.lineEdit_password.setText(row_info[0][2])
        self.Wallet_show_label.setText(str(row_info[0][3]))
        self.lineEdit_email.setText(row_info[0][4])
        self.lineEdit_address.setText(row_info[0][5])
        c.close()
        conn.close()
        
    def show_favorite(self,username):
        self.tableWidget.clearContents()
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_select_query = """select pr_id,pr_name,pr_seller_name,pr_price from favorite_list where cu_name = ?"""
        c.execute(sql_select_query, (username,))
        row_favorite = c.fetchall()
        for row_number,row_data in enumerate(row_favorite):
            self.tableWidget.insertRow(row_number+1)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        
        c.close()
        conn.close()
                
    def show_shoplist(self,username):
        self.tableWidget_3.clearContents()
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_select_query = """select pr_id,name,price,seller from shop_list where cu_name=?"""
        c.execute(sql_select_query,(username,))
        row_shoplist = c.fetchall()
        for row_number,row_data in enumerate(row_shoplist):
            self.tableWidget_3.insertRow(row_number+1)
            for column_number,data in enumerate(row_data):
                self.tableWidget_3.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        

                
    def show_Previous(self,username):
        self.tableWidget_2.clearContents()
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_select_query = """select pr_id,pr_name,seller_id,seller_name,pr_price from previous_shoping where cu_name = ?"""
        c.execute(sql_select_query, (username,))
        row_previous = c.fetchall()
        for row_number,row_data in enumerate(row_previous):
            self.tableWidget_2.insertRow(row_number+1)
            for column_number,data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        c.close()
        conn.close()
    def edit_info(self,username):
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_select_query ="""UPDATE customers SET address=?,password=?,email=? WHERE username=?"""
        if(self.lineEdit_username.text() != self.username):
            self.state_edit.setText("you cant change username!")
            c.close()
            conn.close
            return
        else:
            c.execute(sql_select_query,(self.lineEdit_address.text(),self.lineEdit_password.text(),self.lineEdit_email.text(),self.username))
            conn.commit()
            c.close()
            conn.close()
            self.show_info(self.username)
            self.state_edit.setText("Done")
            return
    def charge(self):
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_select_query = """select wallet from customers where username = ?"""
        sql_select_query2 ="""UPDATE customers SET wallet=? WHERE username=?"""
        c.execute(sql_select_query,(self.username,))
        n=c.fetchall()
        wallet=int(n[0][0])
        wallet=wallet+int(self.lineEdit.text())
        c.execute(sql_select_query2,(wallet,self.username))
        conn.commit()
        c.close()
        conn.close()
        self.show_info(self.username)
        
    def show_products(self):
        self.product_window=QtWidgets.QMainWindow()
        self.product=products(self,self.username)
        self.product.setupUi(self.product_window)
        self.product_window.show()
            
    def shop_products(self):
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_select_query="""SELECT * FROM shop_list WHERE cu_name=?"""
        c.execute(sql_select_query,(self.username,))  
        rows_shop=c.fetchall()
        sum_of_price=0
        wallet=int(self.Wallet_show_label.text())
        for i in rows_shop:
            sum_of_price=sum_of_price+int(i[2])
        if(wallet<sum_of_price):
            return
        wallet=wallet-sum_of_price
        sql_select_query2 ="""UPDATE customers SET wallet=? WHERE username=?"""
        c.execute(sql_select_query2,(wallet,self.username))
        conn.commit()
        c.close()
        conn.close()
        self.show_info(self.username)
        self.tableWidget_3.clearContents()
        self.add_to_previous()
        
    def add_to_previous(self):
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_select_query="""SELECT * FROM shop_list WHERE cu_name=?"""
        c.execute(sql_select_query,(self.username,))  
        rows_shop=c.fetchall()
        for row in rows_shop:
            sql_select_query2="""SELECT id FROM seller WHERE username=?"""
            c.execute(sql_select_query2,(row[3],))
            seller_id=c.fetchall()[0][0]
            sql_select_query2="""SELECT id FROM customers WHERE username=?"""
            c.execute(sql_select_query2,(self.username,))
            cu_id=c.fetchall()[0][0]
            sql_update_query="""INSERT INTO previous_shoping(cu_id,pr_id,seller_id,seller_name,pr_name,pr_price,cu_name) VALUES(?,?,?,?,?,?,?)"""
            data=(cu_id,row[0],seller_id,row[3],row[1],row[2],self.username)
            c.execute(sql_update_query,data)
            conn.commit()
        self.show_Previous(self.username)
        
        sql_delete_query="""DELETE FROM shop_list"""
        c.execute(sql_delete_query) 
        conn.commit()
        c.close()
        conn.close()
        
        
class products(object):
    def __init__(self,cu_win,username):
        self.index=0
        self.username=username
        self.comments2=''
        self.super_window=cu_win
    def setupUi(self, product_window):
        product_window.setObjectName("product_window")
        product_window.resize(546, 443)
        product_window.setMinimumSize(QtCore.QSize(546, 443))
        product_window.setMaximumSize(QtCore.QSize(546, 443))
        product_window.setStyleSheet("background-color: rgb(144, 255, 93);")
        self.centralwidget = QtWidgets.QWidget(product_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_comment = QtWidgets.QLabel(self.centralwidget)
        self.label_comment.setGeometry(QtCore.QRect(10, 280, 101, 18))
        self.label_comment.setStyleSheet("font: 75 11pt \"Orbitron\";\n"
"background-color: rgb(255, 85, 127);")
        self.label_comment.setObjectName("label_comment")
        self.Back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Back_btn.setGeometry(QtCore.QRect(10, 400, 75, 23))
        self.Back_btn.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 75 10pt \"Orbitron\";")
        self.Back_btn.setObjectName("Back_btn")
        self.Back_btn.clicked.connect(self.mines)
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(460, 400, 75, 23))
        self.next_btn.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 75 10pt \"Orbitron\";")
        self.next_btn.setObjectName("next_btn")
        self.next_btn.clicked.connect(self.plus)
        self.textedit_comments = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit_comments.setGeometry(QtCore.QRect(10, 300, 521, 91))
        self.textedit_comments.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textedit_comments.setReadOnly(True)
        self.textedit_comments.setObjectName("textedit_comments")

        self.add_favorite_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_favorite_btn.setGeometry(QtCore.QRect(120, 180, 161, 23))
        self.add_favorite_btn.setStyleSheet("font: 75 10pt \"Orbitron\";\n"
"background-color: rgb(255, 255, 127);")
        self.add_favorite_btn.setObjectName("add_favorite_btn")
        self.add_favorite_btn.clicked.connect(self.add_favorite)
        self.add_shoplist_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_shoplist_btn.setGeometry(QtCore.QRect(290, 180, 171, 23))
        self.add_shoplist_btn.setStyleSheet("font: 75 10pt \"Orbitron\";\n"
"background-color: rgb(0, 255, 255);\n"
"")
        self.add_shoplist_btn.setObjectName("add_shoplist_btn")
        self.add_shoplist_btn.clicked.connect(self.add_shoplist)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 511, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"\n"
"font: 75 10pt \"Orbitron\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 75 10pt \"Orbitron\";\n"
"background-color: rgb(0, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 75 10pt \"Orbitron\";\n"
"background-color: rgb(0, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font: 75 10pt \"Orbitron\";\n"
"background-color: rgb(0, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_show_id = QtWidgets.QLabel(self.layoutWidget)
        self.label_show_id.setStyleSheet("font: 75 10pt \"Orbitron\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_show_id.setText("")
        self.label_show_id.setObjectName("label_show_id")
        self.horizontalLayout_2.addWidget(self.label_show_id)
        self.label_show_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_show_name.setStyleSheet("font: 75 10pt \"Orbitron\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_show_name.setText("")
        self.label_show_name.setObjectName("label_show_name")
        self.horizontalLayout_2.addWidget(self.label_show_name)
        self.label_show_seller = QtWidgets.QLabel(self.layoutWidget)
        self.label_show_seller.setStyleSheet("font: 75 10pt \"Orbitron\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_show_seller.setText("")
        self.label_show_seller.setObjectName("label_show_seller")
        self.horizontalLayout_2.addWidget(self.label_show_seller)
        self.label_show_price = QtWidgets.QLabel(self.layoutWidget)
        self.label_show_price.setStyleSheet("font: 75 10pt \"Orbitron\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_show_price.setText("")
        self.label_show_price.setObjectName("label_show_price")
        self.horizontalLayout_2.addWidget(self.label_show_price)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        product_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(product_window)
        self.statusbar.setObjectName("statusbar")
        product_window.setStatusBar(self.statusbar)
        self.show_products()

        self.retranslateUi(product_window)
        QtCore.QMetaObject.connectSlotsByName(product_window)

    def retranslateUi(self, product_window):
        _translate = QtCore.QCoreApplication.translate
        product_window.setWindowTitle(_translate("product_window", "MainWindow"))
        self.label_comment.setText(_translate("product_window", "comments"))
        self.Back_btn.setText(_translate("product_window", "Back"))
        self.next_btn.setText(_translate("product_window", "Next"))
        self.add_favorite_btn.setText(_translate("product_window", "Add to my favorite"))
        self.add_shoplist_btn.setText(_translate("product_window", "Add to shpping list"))
        self.label.setText(_translate("product_window", "ID"))
        self.label_2.setText(_translate("product_window", "Name"))
        self.label_3.setText(_translate("product_window", "Seller"))
        self.label_4.setText(_translate("product_window", "Price"))
        
        
    def show_products(self):
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_select_query = """select * from products"""
        c.execute(sql_select_query)
        self.rows=c.fetchall()
        if(self.index<0):
            self.index=0
        elif(self.index>len(self.rows)-1):
            self.index=len(self.rows)-1
        self.label_show_id.setText(self.rows[self.index][0])
        self.label_show_name.setText(self.rows[self.index][1])
        self.label_show_seller.setText(self.rows[self.index][2])
        self.label_show_price.setText(str(self.rows[self.index][3]))
        
        sql_select_query2="SELECT * FROM pr_comments WHERE pr_id=?"
        c.execute(sql_select_query2,(self.rows[self.index][0],))
        self.comments=c.fetchall()
        if not self.comments:
            self.textedit_comments.clear()
            self.textedit_comments.setText("there is no comments yet")
        else:
            self.comments2=''
            for tp in self.comments:
                self.comments2=self.comments2 + f"\n{tp[1]} says: {tp[4]}"
            self.textedit_comments.clear()
            self.textedit_comments.setText(self.comments2)
        c.close()
        conn.close()
                
    def mines(self):
        self.index=self.index-1
        self.show_products()
    def plus(self):
        self.index=self.index+1
        self.show_products()
        
    def add_favorite(self):
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_select_query = """select * from products"""
        c.execute(sql_select_query)
        rows_products=c.fetchall()
        product_id=rows_products[self.index][0]
        product_name=rows_products[self.index][1]
        product_seller=rows_products[self.index][2]
        product_price=str(rows_products[self.index][3])
        sql_select_query2="""SELECT * FROM customers WHERE username=?"""
        c.execute(sql_select_query2,(self.username,))
        customer_id=c.fetchall()[0][0]
        sql_select_query2="""SELECT * FROM seller WHERE username=?"""
        c.execute(sql_select_query2,(product_seller,))
        seller_id=c.fetchall()[0][0]
        sql_select_query3="""SELECT * FROM favorite_list WHERE cu_name=?"""
        c.execute(sql_select_query3,(self.username,))
        favorite_list_user=c.fetchall()
        for i in favorite_list_user:
            if(i[2]==product_id):
                c.close()
                conn.close()
                return
        sql_update_query4="INSERT INTO favorite_list VALUES (?,?,?,?,?,?,?);"
        data=(customer_id,self.username,product_id,product_name,product_price,seller_id,product_seller)
        c.execute(sql_update_query4,data)
        conn.commit()
        c.close()
        conn.close()
        self.super_window.show_favorite(self.username) #finish
        
        
    def add_shoplist(self):
        conn = sqlite3.connect('online_shop.db')
        c = conn.cursor()
        sql_create_query = """CREATE TABLE IF NOT EXISTS shop_list(pr_id text, name text, price integer,seller text,cu_name text)"""
        c.execute(sql_create_query)
        sql_select_query = """select * from products"""
        c.execute(sql_select_query)
        rows_product=c.fetchall()
        
        sql_select_query3="""SELECT * FROM shop_list WHERE cu_name=?"""
        c.execute(sql_select_query3,(self.username,))
        shop_list_user=c.fetchall()
        for i in shop_list_user:
            if(i[0]==rows_product[self.index][0]):
                c.close()
                conn.close()
                self.super_window.show_shoplist(self.username)
                return
        
        
        sql_update_query="""INSERT INTO shop_list VALUES (?,?,?,?,?);"""
        data=(rows_product[self.index][0],rows_product[self.index][1],rows_product[self.index][3],str(rows_product[self.index][2]),self.username)
        c.execute(sql_update_query,data)
        conn.commit()
        c.close()
        conn.close()
        self.super_window.show_shoplist(self.username)

