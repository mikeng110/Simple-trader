from binance.client import Client

class BinanceClient(Client):
    def __init__(self, api_key, api_sig, parent=None):
        Client.__init__(self, api_key=api_key, api_secret=api_sig)