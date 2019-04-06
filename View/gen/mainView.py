# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 692)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"    background-color: rgb(20,20,20);\n"
"}\n"
"#centralwidget {\n"
"    background-color:  rgb(20,20,20);\n"
"}\n"
"\n"
"QTabWidget\n"
"{\n"
"      background-color: rgb(60, 62, 63);\n"
"}\n"
"\n"
"QTabWidget::pane\n"
" {\n"
"     border-top: 1px solid gray;\n"
"     border-left: 1px solid gray;\n"
"     border-right: 1px solid gray;\n"
"     border-bottom: 1px solid gray;\n"
"    background-color: rgb(60, 62, 63);\n"
" }\n"
"\n"
"QListWidget\n"
"{\n"
"    background: #3C3F41;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QListWidget::item\n"
"{\n"
"    color: rgb(253, 165, 15);\n"
"    font-family: \"MV Boli\";\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(30,30, 30);\n"
"    color: rgb(253, 165, 15);\n"
"    font-family: \"MV Boli\";\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color:rgb(253, 165, 15);\n"
"    font-family: \"MV Boli\";\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    color:rgb(253, 165, 15);\n"
"    font-family: \"MV Boli\";\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background-color: rgb(60, 62, 63);\n"
"    color: rgb(253, 165, 15);\n"
"    font-family: \"MV Boli\";    \n"
"}\n"
"\n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"    background-color: rgb(40, 40, 40);\n"
"    \n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background: #3C3F41;\n"
"    color: rgb(253, 165, 15);\n"
"    font-family: \"MV Boli\";\n"
"    font-size: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 331, 641))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Entry_input = QtWidgets.QLineEdit(self.groupBox)
        self.Entry_input.setGeometry(QtCore.QRect(20, 290, 291, 31))
        self.Entry_input.setObjectName("Entry_input")
        self.amount_slider = QtWidgets.QSlider(self.groupBox)
        self.amount_slider.setGeometry(QtCore.QRect(20, 470, 261, 22))
        self.amount_slider.setOrientation(QtCore.Qt.Horizontal)
        self.amount_slider.setObjectName("amount_slider")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 270, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 330, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 81, 16))
        self.label_4.setObjectName("label_4")
        self.amount_75 = QtWidgets.QRadioButton(self.groupBox)
        self.amount_75.setGeometry(QtCore.QRect(170, 510, 51, 17))
        self.amount_75.setObjectName("amount_75")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 390, 81, 16))
        self.label_3.setObjectName("label_3")
        self.Stopp_loss_input = QtWidgets.QLineEdit(self.groupBox)
        self.Stopp_loss_input.setGeometry(QtCore.QRect(20, 410, 291, 31))
        self.Stopp_loss_input.setObjectName("Stopp_loss_input")
        self.portfolio_procentage_display = QtWidgets.QLabel(self.groupBox)
        self.portfolio_procentage_display.setGeometry(QtCore.QRect(290, 470, 31, 20))
        self.portfolio_procentage_display.setObjectName("portfolio_procentage_display")
        self.Take_profit_input = QtWidgets.QLineEdit(self.groupBox)
        self.Take_profit_input.setGeometry(QtCore.QRect(20, 350, 291, 31))
        self.Take_profit_input.setObjectName("Take_profit_input")
        self.price_out = QtWidgets.QLabel(self.groupBox)
        self.price_out.setGeometry(QtCore.QRect(110, 240, 201, 16))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(-1)
        self.price_out.setFont(font)
        self.price_out.setObjectName("price_out")
        self.img_widget = QtWidgets.QWidget(self.groupBox)
        self.img_widget.setGeometry(QtCore.QRect(20, 10, 242, 215))
        self.img_widget.setObjectName("img_widget")
        self.amount_25 = QtWidgets.QRadioButton(self.groupBox)
        self.amount_25.setGeometry(QtCore.QRect(20, 510, 61, 17))
        self.amount_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.amount_25.setObjectName("amount_25")
        self.amount_100 = QtWidgets.QRadioButton(self.groupBox)
        self.amount_100.setGeometry(QtCore.QRect(250, 510, 61, 17))
        self.amount_100.setObjectName("amount_100")
        self.Execute_trade_btn = QtWidgets.QPushButton(self.groupBox)
        self.Execute_trade_btn.setGeometry(QtCore.QRect(14, 560, 301, 61))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(-1)
        self.Execute_trade_btn.setFont(font)
        self.Execute_trade_btn.setObjectName("Execute_trade_btn")
        self.amount_50 = QtWidgets.QRadioButton(self.groupBox)
        self.amount_50.setGeometry(QtCore.QRect(90, 510, 51, 17))
        self.amount_50.setObjectName("amount_50")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 450, 61, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 10, 421, 641))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 401, 611))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Pending_list = QtWidgets.QListWidget(self.tab)
        self.Pending_list.setGeometry(QtCore.QRect(0, 0, 391, 471))
        self.Pending_list.setStyleSheet("")
        self.Pending_list.setObjectName("Pending_list")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 520, 391, 61))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(-1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Active_list = QtWidgets.QListWidget(self.tab_2)
        self.Active_list.setGeometry(QtCore.QRect(0, 0, 391, 471))
        self.Active_list.setObjectName("Active_list")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Closed_list = QtWidgets.QListWidget(self.tab_3)
        self.Closed_list.setGeometry(QtCore.QRect(0, 0, 391, 471))
        self.Closed_list.setObjectName("Closed_list")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trader"))
        self.label.setText(_translate("MainWindow", "Entry"))
        self.label_2.setText(_translate("MainWindow", "Take Profit"))
        self.label_4.setText(_translate("MainWindow", "BTCUSD: "))
        self.amount_75.setText(_translate("MainWindow", "75%"))
        self.label_3.setText(_translate("MainWindow", "Stop Loss"))
        self.portfolio_procentage_display.setText(_translate("MainWindow", "0%"))
        self.price_out.setText(_translate("MainWindow", "0"))
        self.amount_25.setText(_translate("MainWindow", "25%"))
        self.amount_100.setText(_translate("MainWindow", "100%"))
        self.Execute_trade_btn.setText(_translate("MainWindow", "Execute Trade"))
        self.amount_50.setText(_translate("MainWindow", "50%"))
        self.label_5.setText(_translate("MainWindow", "Amount"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel All Pending"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Pending"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Active"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Closed"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
