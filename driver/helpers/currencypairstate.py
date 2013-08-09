import datetime

class CurrencyPairState(object):
    currency_pair = 'BTC'
    bid = []             #ordered array of tuples
    ask = []
    poll_time = datetime.datetime.now()                 #what time did we receive the data
    place_time = datetime.datetime.now()                #what time was the trade order placed by the other party

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
       return str(dict(self.__dict__))

    def get_currency_pair(self):
        return self.currency_pair
       
    def get_bid(self):
        return self.bid
       
    def get_ask(self):
        return self.ask
       
    def get_poll_time(self):
        return self.time

    def get_place_time(self):
        return self.time