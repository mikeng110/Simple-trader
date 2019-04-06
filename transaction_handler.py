from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from transaction_bot2 import TransactionBot

class TransactionHandler(QtCore.QObject):
    sig = pyqtSignal(object) #used to send
    def __init__(self, client, crawler, parent=None):
        QtCore.QObject.__init__(self, parent)
        self.pending_data = {}
        self.active_data = {}
        self.closed_data = {}
        self.client = client
        self.crawler = crawler
        self.bots = []


    def create_transaction(self, transaction): #create proper class for data
        id = transaction["id"]

        bot = TransactionBot(self.client, self.crawler, transaction)
        self.bots.append({"id": id, "bot": bot})
        bot.start()
        bot.sig.connect(self.update_transaction)

        self.pending_data[id] = transaction
        self.update_transaction(transaction)



    def update_transaction(self, transaction):
        id = transaction["id"]
        if transaction["status"] == "active":
            print("set active")
            self.pending_data.pop(id)
            self.active_data[id] = transaction

        elif transaction["status"] == "closed":
            print("set closed")
            self.active_data.pop(id)
            self.closed_data[id] = transaction
            self.kill(id)

        self.sig.emit({"pending": self.pending_data, "active": self.active_data, "closed": self.closed_data})

    def kill_all(self):
        for bot in self.bots:
            bot["bot"].stop()

    def kill(self, id):
        for bot in self.bots:
            if bot["id"] == id:
                bot["bot"].stop()





