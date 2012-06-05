import sys, os, datetime

# add the current file to the system path so we can import everything
sys.path.append(os.getcwd())

from exchange_api.historical import Historical
from helpers.trade import Trade
from strategy.singleexchangestrategy import SingleExchangeStrategy

# settings
realtime = False
strategy = 'strategy_name'

# run the program
if realtime:
    # TODO : create realtime run environment
    pass
else:
    # run the driver over historical data
    api = Historical()
    print api.get_data_from_exchange(datetime.datetime.now())
    trade_options = dict(
            currency_pair = 'USD',
            buyBTC = True,
            price = 13.00,
            volume = 300.00,
            time_expiry = datetime.datetime.now()
    )
    api.execute_trade([Trade(**trade_options)])

    s = SingleExchangeStrategy()
    print s.limit_order()
