import datetime
from helpers.currencypairstate import CurrencyPairState
from helpers.trade import Trade

class ExchangeAPI(object):
    """
    Abstract base class for exchange APIs
    """
    def get_data_from_exchange(self, now):
        """
        Retrieves data from the given exchange, and returns it as an array of CurrencyPairStates.
        """
        return [CurrencyPairState()]

    def schedule_trades(self, trades):
        """
        Given a list of trades, schedules each to be executed in its own thread / process / magical subverse
        """
        for trade in trades:
            # create a thread / process that executes the trade
            pass

    def execute_trade(self, trade):
        """
        Given a single trade, executes it.
        """
        pass
