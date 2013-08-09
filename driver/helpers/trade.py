import datetime

class Trade(object):
    currency_pair = 'BTCUSD'
    price = 0
    volume = 0
    buy_BTC = False
    time_expiry = datetime.datetime.now()

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
        
    def get_price(self):
        return self.price
        
    def get_volume(self):
        return self.volume
        
    def get_buy_BTC(self):
        return self.buy_BTC
        
    def get_time_expiry(self):
        return self.time_expiry
        
    def set_volume(self,vol):
        self.volume = vol