from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import time


class TransactionBot(QtCore.QThread):
    sig = pyqtSignal(object)

    def __init__(self, client, price_crawler, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = True
        self.delta = 0.5
        self.client = client
        self.price_crawler = price_crawler
        self.symbol = "BTCUSDT"
        self.transactions = [] #status Pending, active, closed
        self.price_crawler.sig.connect(self.update_ticker)
        self.ticker = {}

    def run(self):
        while self.running:
            for transaction in self.transactions:
                self.process(transaction)

            time.sleep(self.delta)

    def stop(self):
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
                self.set_active(transaction)
        elif transaction["status"] == "active":
            if current_price <= stop_loss or current_price >= take_profit: #implement trailing stop loss.
                self.sell()
                self.set_closed(transaction)

    def set_active(self, transaction):
        for d in self.transactions:
            if d["id"] == transaction["id"]:
                d.update((k, "active") for k, v in d.items() if v == "pending")

    def set_closed(self, transaction):
        for d in self.transactions:
            if d["id"] == transaction["id"]:
                d.update((k, "closed") for k, v in d.items() if v == "active")



    def update_ticker(self, price ):
        self.ticker[price["symbol"]] = float(price["price"])


    def update(self, transaction):
        if not self.exist(transaction):
            self.transactions.append(transaction)
            print("Transaction added")
        else:
            print("Transaction already exist")

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