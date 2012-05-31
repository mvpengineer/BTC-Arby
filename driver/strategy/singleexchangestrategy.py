import datetime
from helpers.trade import Trade
from strategy import Strategy

class SingleExchangeStrategy(Strategy):
    def limit_order(self):
        trade_options = dict(
            currency_pair = 'EUR',
            buyBTC = True,
            price = 13.00,
            volume = 300.00,
            time_expiry = datetime.datetime.now()
        )
        return Trade(**trade_options)
