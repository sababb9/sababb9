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
        self.login_tab.setTabText(self.login_tab.indexOf(self.Management), _translate("login_page", "Operator")) #commited
    
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
        conn.close()  #commit
    




class sign_up(object):
    def  close_signup(self):
        MainWindow.show()
        ui.signupwindow.hide()#commit
        
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
        QtCore.QMetaObject.connectSlotsByName(sign_up)#commited

    def retranslateUi(self, signup):
        _translate = QtCore.QCoreApplication.translate
        signup.setWindowTitle(_translate("signup", "MainWindow"))
        self.label_username.setText(_translate("signup", "User Name"))
        self.label_password.setText(_translate("signup", "Password"))
        self.signup_btn.setText(_translate("signup", "sign up"))
        self.back_btn.setText(_translate("signup", "Back"))
        self.login_tab.setTabText(self.login_tab.indexOf(self.customers), _translate("signup", "customers"))#commit
    
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
            return #commit
        
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
            c.execute(sqlite_insert_with_param,(ID,self.username,self.password,first,email,email)) #commit
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
