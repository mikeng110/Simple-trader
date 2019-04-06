from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

from Exchange.binance import BinanceClient
from Bots.ticker_fetcher import TickerFetcher
from Controller.transaction_controller import TransactionController

import uuid


class MainController(QtCore.QObject):
    transaction_signal = pyqtSignal(object)
    ticker_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)
        self.client = None
        self.crawler = None

        self.init_exchange_client()
        self.init_price_crawler()

        self.tc = TransactionController(self.client, self.crawler)

        self.conect_signals()

    def init_exchange_client(self):
        self.client = BinanceClient("", "")

    def init_price_crawler(self):
        self.crawler = TickerFetcher(self.client)
        self.crawler.start()
        self.crawler.sig.connect(self.update_display)

    def conect_signals(self):
        self.tc.sig.connect(self.update_list_views)
        self.crawler.sig.connect(self.update_display)

    def execute_trade(self, buy_in, take_profit, stop_loss):

        id = self.gen_id()
        transaction = {"id": id, "status": "pending", "symbol": "BTCUSDT", "buy_in": buy_in, "take_profit": take_profit,
                       "stop_loss": stop_loss}

        self.tc.create_transaction(transaction)

    def to_str(self, transaction):
        symbol = transaction["symbol"]
        buy_in = str(transaction["buy_in"])
        take_profit = str(transaction["take_profit"])
        stop_loss =  str(transaction["stop_loss"])

        return symbol + " ->\tEntry: " + buy_in + "\n\tGoal: " + take_profit + "\n\tStop Loss: " + stop_loss + "\n"

    def update_list_views(self, data): #change name
        pending_data = data["pending"]
        active_data = data["active"]
        closed_data = data["closed"]

        result = {"pending": [], "active": [], "closed": []} #change to the python way using generator expressions.

        for k, v in pending_data.items():
            result["pending"].append(self.to_str(v))

        for k, v in active_data.items():
            result["active"].append(self.to_str(v))

        for k, v in closed_data.items():
            result["closed"].append(self.to_str(v))

        self.transaction_signal.emit(result)

    def update_display(self, data): #change name
        price = float(data["price"])
        price = str('{0:g}'.format(price))
        self.ticker_signal.emit(price)

    def gen_id(self):
        return uuid.uuid4()