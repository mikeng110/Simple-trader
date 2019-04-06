from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import time


class PriceCrawler(QtCore.QThread):
    sig = pyqtSignal(object)

    def __init__(self, client, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = True
        self.delta = 1
        self.client = client
        self.symbol = "BTCUSDT"


    def run(self):
        while self.running:
            ticker = self.client.get_all_tickers()
            f = filter(lambda price_ticker: price_ticker['symbol'] == self.symbol, ticker)
            ticker = f.__next__()
            self.sig.emit(ticker)
            time.sleep(self.delta)

    def stop(self):
        self.running = False