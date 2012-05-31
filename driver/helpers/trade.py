import datetime

class Trade(object):
    currency_pair = 'BTC:BTC'
    price = 0
    volume = 0
    buyBTC = False
    time_expiry = datetime.datetime.now()

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
        return str(dict(self.__dict__))
