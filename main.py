import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import pyqtSignal


from View.gen.mainView import Ui_MainWindow
from price_crawler import PriceCrawler
from Exchange.binance import BinanceClient
from transaction_handler import TransactionHandler


import uuid

class MainWindow(QMainWindow):
    trans_sig = pyqtSignal(object)
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #

        img_lay = QtWidgets.QVBoxLayout(self.ui.img_widget)
        label = QLabel(self)
        pixmap = QtGui.QPixmap('resources/img/rocket.png')
        label.setPixmap(pixmap)
        img_lay.addWidget(label)

        #

        self.ui.Execute_trade_btn.clicked.connect(self.execute_trade_clicked)
        self.client = BinanceClient("", "") #encapsulate with try catch

        self.crawler = PriceCrawler(self.client)
        self.crawler.start()
        self.crawler.sig.connect(self.update_display)

        self.th = TransactionHandler(self.client, self.crawler)
        self.th.sig.connect(self.update_list_views)

        self.ui.tabWidget.autoFillBackground()

    def update_display(self, data):
        price = float(data["price"])
        price = str('{0:g}'.format(price))
        self.ui.price_out.setText(price)

    def execute_trade_clicked(self):
        buy_in = self.ui.Entry_input.text()
        take_profit =  self.ui.Take_profit_input.text()
        stop_loss = self.ui.Stopp_loss_input.text()

        id = self.gen_id()
        transaction = {"id": id, "status": "pending", "symbol": "BTCUSDT", "buy_in": buy_in, "take_profit": take_profit,
                       "stop_loss": stop_loss}
        self.th.create_transaction(transaction)

    def to_str(self, transaction):
        symbol = transaction["symbol"]
        buy_in = str(transaction["buy_in"])
        take_profit = str(transaction["take_profit"])
        stop_loss =  str(transaction["stop_loss"])

        return symbol + " ->\tEntry: " + buy_in + "\n\tGoal: " + take_profit + "\n\tStop Loss: " + stop_loss + "\n"

    def update_list_views(self, data):
        pending_data = data["pending"]
        active_data = data["active"]
        closed_data = data["closed"]

        self.ui.Pending_list.clear()
        for k, v in pending_data.items():
            self.ui.Pending_list.addItem(self.to_str(v))

        self.ui.Active_list.clear()
        for k, v in active_data.items():
            self.ui.Active_list.addItem(self.to_str(v))

        self.ui.Closed_list.clear()
        for k, v in closed_data.items():
            self.ui.Closed_list.addItem(self.to_str(v))

    def gen_id(self):
        return uuid.uuid4()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()
    ret = app.exec_()
    mainWin.crawler.stop()
    mainWin.th.kill_all()
   # mainWin.trans.stop()
    sys.exit(ret)

