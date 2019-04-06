from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import pyqtSignal

from View.gen.mainView import Ui_MainWindow


class MainWindow(QMainWindow):
    trans_sig = pyqtSignal(object)

    def __init__(self, main_ctr):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.main_ctr = main_ctr

        self.build_ui()

    def build_ui(self):
        self.ui.setupUi(self)
        self.init_graphics()
        self.connect_signals()

    def connect_signals(self):
        self.ui.Execute_trade_btn.clicked.connect(self.execute_trade_clicked)
        self.main_ctr.transaction_signal.connect(self.update_list_views)
        self.main_ctr.ticker_signal.connect(self.update_display)

    def init_graphics(self):
        img_lay = QtWidgets.QVBoxLayout(self.ui.img_widget)
        label = QLabel(self)
        pixmap = QtGui.QPixmap('resources/img/rocket.png')
        label.setPixmap(pixmap)
        img_lay.addWidget(label)

        self.ui.tabWidget.autoFillBackground()

    def update_display(self, price):
        self.ui.price_out.setText(price)

    def execute_trade_clicked(self):
        buy_in = self.ui.Entry_input.text()
        take_profit = self.ui.Take_profit_input.text()
        stop_loss = self.ui.Stopp_loss_input.text()

        self.main_ctr.execute_trade(buy_in, take_profit, stop_loss)

    def update_list_views(self, data):
        pending_data = data["pending"]
        active_data = data["active"]
        closed_data = data["closed"]

        self.ui.Pending_list.clear()
        for p in pending_data:
            self.ui.Pending_list.addItem(p)

        self.ui.Active_list.clear()
        for a in active_data:
            self.ui.Active_list.addItem(a)

        self.ui.Closed_list.clear()
        for c in closed_data:
            self.ui.Closed_list.addItem(c)

