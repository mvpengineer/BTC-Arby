import sys, os, datetime

# add the current file to the system path so we can import everything
sys.path.append(os.getcwd())

from exchange_api.historical import Historical
from helpers.trade import Trade
from helpers.currencypairstate import CurrencyPairState
from strategy.singleexchangestrategy import SingleExchangeStrategy

# settings
realtime = False
strategy = 'strategy_name'

portfolio_USD = 500.00
portfolio_EUR = 500.00
portfolio_BTC = 100.00

# run the program
if realtime:
    # TODO : create realtime run environment
    pass
else:
    # run the driver over historical data
    api = Historical()
    #print api.get_data_from_exchange(datetime.datetime.now())
    #api.execute_trade([Trade(**trade_options)])

    s = SingleExchangeStrategy()
    print s.limit_order()
    #print s.gain(buy_trade, sell_trade, buy_currency_pair_state, sell_currency_pair_state)
    #print s.limit_order()

