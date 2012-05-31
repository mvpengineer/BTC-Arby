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
