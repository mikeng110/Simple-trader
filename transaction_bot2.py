from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import time


class TransactionBot(QtCore.QThread):
    sig = pyqtSignal(object)

    def __init__(self, client, price_crawler, transaction, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = True
        self.delta = 0.5
        self.client = client
        self.price_crawler = price_crawler
        self.symbol = "BTCUSDT"
        self.transaction = transaction
        self.price_crawler.sig.connect(self.update_ticker)
        self.ticker = {}

    def run(self):
        while self.running:
            self.process(self.transaction)

            time.sleep(self.delta)

    def stop(self):
        print("Stop")
        self.running = False

    def process(self, transaction):
        if not self.ticker:
            return

        current_price = self.ticker[self.symbol]
        buy_in = float(transaction["buy_in"])
        take_profit = float(transaction["take_profit"])
        stop_loss = float(transaction["stop_loss"])

        if transaction["status"] == "pending":
            if current_price <= buy_in:
                self.buy()
                self.transaction["status"] = "active"
                self.sig.emit(self.transaction)

        elif transaction["status"] == "active":
            if current_price <= stop_loss or current_price >= take_profit: #implement trailing stop loss.
                self.sell()
                self.transaction["status"] = "closed"
                self.sig.emit(self.transaction)


    def update_ticker(self, price ):
        self.ticker[price["symbol"]] = float(price["price"])


    def exist(self, transaction):
        try:
            next(item for item in self.transactions if item["id"] == transaction["id"])
            return True

        except StopIteration:
            pass



    def buy(self):
        print("Buy at price: " + str(self.ticker[self.symbol]))

    def sell(self):
        print("sell at price: " + str(self.ticker[self.symbol]))