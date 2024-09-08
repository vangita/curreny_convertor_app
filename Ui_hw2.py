import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 20, 791, 571))
        self.stackedWidget.setObjectName("stackedWidget")

        self.registartion = QtWidgets.QWidget()
        self.registartion.setObjectName("registartion")
        self.label = QtWidgets.QLabel(self.registartion)
        self.label.setGeometry(QtCore.QRect(350, 120, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.registartion)
        self.label_2.setGeometry(QtCore.QRect(350, 200, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.registartion)
        self.lineEdit.setGeometry(QtCore.QRect(320, 160, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.registartion)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 230, 113, 22))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.registartion)
        self.pushButton.setGeometry(QtCore.QRect(330, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.registartion)

        self.currency_exchange = QtWidgets.QWidget()
        self.currency_exchange.setObjectName("currency_exchange")
        self.pushButton_2 = QtWidgets.QPushButton(self.currency_exchange)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 130, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.currency_exchange)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 130, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_3 = QtWidgets.QLabel(self.currency_exchange)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 10, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLabel(self.currency_exchange)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 40, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLabel(self.currency_exchange)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 100, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox = QtWidgets.QComboBox(self.currency_exchange)
        self.comboBox.setGeometry(QtCore.QRect(130, 10, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["USD", "GEL", "RUPEE"])
        self.comboBox_2 = QtWidgets.QComboBox(self.currency_exchange)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 40, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["USD", "GEL", "RUPEE"])
        self.pushButton_4 = QtWidgets.QPushButton(self.currency_exchange)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 530, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_7 = QtWidgets.QLabel(self.currency_exchange)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 70, 113, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.currency_exchange)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 70, 113, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.currency_exchange)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 100, 113, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.stackedWidget.addWidget(self.currency_exchange)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.convert)
        self.pushButton_3.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.exit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
        self.pushButton_2.setText(_translate("MainWindow", "Convert"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.lineEdit_3.setText(_translate("MainWindow", "From"))
        self.lineEdit_4.setText(_translate("MainWindow", "To"))
        self.lineEdit_5.setText(_translate("MainWindow", "Converted Amount"))
        self.lineEdit_7.setText(_translate("MainWindow", "Amount"))
        self.pushButton_4.setText(_translate("MainWindow", "Exit"))

    # Login function
    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == "admin" and password == "admin":
            self.stackedWidget.setCurrentIndex(1)
        else:
            QtWidgets.QMessageBox.warning(None, "Login Failed", "Incorrect Username or Password")

    def convert(self):
        self.lineEdit_6.clear()
        from_currency = self.comboBox.currentText()
        to_currency = self.comboBox_2.currentText()
        dct = {
            "USD/GEL": 2.69,
            "GEL/USD": 0.37,
            "GEL/RUPEE": 31.21,
            "RUPEE/GEL": 0.032,
            "USD/RUPEE": 83.96,
            "RUPEE/USD": 0.012
        }
        key = f"{from_currency}/{to_currency}"
        if key not in dct:
            QtWidgets.QMessageBox.warning(None, "Conversion Error",
                                          "Conversion rate not available for selected currencies")
            return

        try:
            amount = float(self.lineEdit_8.text())
            converted_amount = dct[key] * amount
            self.lineEdit_6.setText(f"{converted_amount:.2f}")
        except ValueError:
            QtWidgets.QMessageBox.warning(None, "Input Error", "Please enter a valid number")
    # Clear function
    def clear(self):
        self.lineEdit_8.clear()
        self.lineEdit_6.clear()
        self.comboBox.setCurrentIndex(-1)
        self.comboBox_2.setCurrentIndex(-1)

    # Exit function
    def exit(self):
        self.stackedWidget.setCurrentIndex(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

