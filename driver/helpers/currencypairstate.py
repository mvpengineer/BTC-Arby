import datetime

class CurrencyPairState(object):
    currency_pair = 'BTC'
    bid = dict()
    ask = dict()
    time = datetime.datetime.now()

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
       return str(dict(self.__dict__))
       
   #MT
   #is this the standard practice for getters?    
    def get_currency_pair(self):
        return self.currency_pair
       
    def get_bid(self):
        return self.bid
       
    def get_ask(self):
        return self.ask
       
    def get_time(self):
        return self.time