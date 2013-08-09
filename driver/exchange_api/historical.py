import datetime
from exchange_api import ExchangeAPI
from helpers.currencypairstate import CurrencyPairState

class Historical(ExchangeAPI):
    """
    Class that siulates past states of the market.
    """
    def get_data_from_exchange(self, now):
        """
        Retrieves data from the given exchange, and returns it as an array of CurrencyPairStates.
        """
        currency_options = dict(
                currency_pair='USD',
                bid={12.00 : {'guy_1' : 100.00}},
                ask={14.00 : {'guy_2' : 200.00}},
                time=datetime.datetime.now()
        )
        currency_pair_state = CurrencyPairState(**currency_options)
        return [currency_pair_state]

    def execute_trade(self, trade):
        """
        Given a single trade, executes it.
        """
        print trade
