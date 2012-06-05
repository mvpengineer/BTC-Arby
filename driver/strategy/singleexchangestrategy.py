import datetime
from datetime import timedelta
from helpers.trade import Trade
from helpers.currencypairstate import CurrencyPairState
from strategy import Strategy
from gen_helpers import *


#6-1-12
#USD 5.27
#EUR 4.24897
#USD / EUR = 1.241927

usd_eur = 1.241927

#ask is "asking $ 5 for one BTC" or "me buying BTC"
#ask > bid 

class SingleExchangeStrategy(Strategy):
    
    def produce_trade_pair_forward(self,currency_pair_state_one, currency_pair_state_two):
        """
        create a pair of trades based on the currency pair state.  Basically, just make a naive trade in the forward direction between the two currencies.
        """
        c_p_bid = collapse_volumes_bid(currency_pair_state_one.get_bid())
        c_p_bid_price = c_p_bid[0][0]               #price is the second in the tuple (0), of the best bid (0)
        c_p_bid_volume = c_p_bid[0][1]              #volume is the first in the tuple (1), of the best bid (0)
        c_p_ask = collapse_volumes_ask(currency_pair_state_two.get_ask())
        c_p_ask_price = c_p_ask[0][0]
        c_p_ask_volume = c_p_ask[0][1]
        
        c_p_volume = min(c_p_bid_volume,c_p_ask_volume)
             
        time_expire = datetime.datetime.now()
        time_expire = time_expire + timedelta(minutes = 2)
        
        trade_options = dict(
                currency_pair = currency_pair_state_one.get_currency_pair(),
                buy_BTC = False,
                price = c_p_bid_price,
                volume = c_p_volume,
                time_expiry = time_expire
        )
        buy_trade = Trade(**trade_options)
        
        
        trade_options = dict(
                currency_pair = currency_pair_state_two.get_currency_pair(),
                buy_BTC = True,
                price = c_p_ask_price,
                volume = c_p_volume,
                time_expiry = time_expire
        )
        sell_trade = Trade(**trade_options)
        
        return (buy_trade,sell_trade)
    
    def limit_order(self):
        """
        Create a limit order if we're making money on a naive trade.
        """
        
        portfolio_USD_current = 2000.00      #replace with model
        portfolio_USD_start = 2000.00
        portfolio_EUR_current = 1600.00
        portfolio_EUR_start = 1600.00
        
        
        currency_options = dict(        #replace with model
                currency_pair='USD',
                bid={5.26 : {'guy_1' : 100.00}},
                ask={5.27 : {'guy_2' : 200.00}},
                time=datetime.datetime.now()
        )
        currency_pair_state_USD = CurrencyPairState(**currency_options)
        currency_options = dict(
                currency_pair='EUR',
                bid={4.24 : {'guy_3' : 100.00}},
                ask={4.25 : {'guy_4' : 100.00, 'guy_5' : 100.00}, 4.26 : {'guy_6' : 50.00}},
                time=datetime.datetime.now()
        )
        currency_pair_state_EUR = CurrencyPairState(**currency_options)
        
        (buy_trade,sell_trade) = self.produce_trade_pair_forward(currency_pair_state_USD, currency_pair_state_EUR)  #produce naive pair
        
        gain_total = self.gain(buy_trade,sell_trade,currency_pair_state_USD,currency_pair_state_EUR)  #solve for gain
        
        if(gain_total <= 0):   #attempt in other direction if the trade doesnt make money
            (buy_trade,sell_trade) = self.produce_trade_pair_forward(currency_pair_state_EUR, currency_pair_state_USD)
            
            gain_total = self.gain(buy_trade,sell_trade,currency_pair_state_EUR,currency_pair_state_USD)
            if(gain_total <= 0):   #trade doesnt make money, don't return a trade pair at this time.
                return None
                
            new_trade_volume = portfolio_manager(portfolio_EUR_start,portfolio_EUR_current,sell_trade.get_volume(),sell_trade.get_price(),gain_total)
                            #check portfolio manager for the amount we're willing to trade
            buy_trade.set_volume(new_trade_volume)
            sell_trade.set_volume(new_trade_volume)
            return [buy_trade,sell_trade]
            
        new_trade_volume = portfolio_manager(portfolio_USD_start,portfolio_USD_current,sell_trade.get_volume(),sell_trade.get_price(),gain_total)
        
        buy_trade.set_volume(new_trade_volume)
        sell_trade.set_volume(new_trade_volume)
        return [buy_trade,sell_trade]
        
        
            
        #trade_options = dict(
        #    currency_pair = 'EUR',
        #    buy_BTC = True,
        #    price = 13.00,
        #    volume = 300.00,
        #    time_expiry = datetime.datetime.now()
        #)
        #return Trade(**trade_options)
        
        
    def spread_gain(self, buy_trade, sell_trade, buy_currency_pair_state, sell_currency_pair_state):
        """
        Determine the gain based on the ask / bid for each exchange.
        """
        buy_asks_collapsed = collapse_volumes_ask(buy_currency_pair_state.get_ask())

        sell_bids_collapsed = collapse_volumes_bid(sell_currency_pair_state.get_bid())

        buying_volume = buy_trade.get_volume()
        selling_volume = sell_trade.get_volume()
        
        buying_offer_volume = buy_asks_collapsed[0][1]     #volume is the second in the tuple (1), of the best ask (0)
        selling_offer_volume = sell_bids_collapsed[0][1]
        
        if(buying_volume == selling_volume):     #make sure the pair of trades are equivalent
            if(buying_volume <= buying_offer_volume and selling_volume <= selling_offer_volume):
                buy_price = buying_volume * buy_asks_collapsed[0][0]   #price is the first in the tuple (0), of the best ask (0)
                sell_price = selling_volume * sell_bids_collapsed[0][0]
                return buying_volume * ((buy_price / sell_price) - usd_eur)
                        
        return -99
        

    def predicted_slippage_gain(self,trade,currency_pair_state):
        """
        Return the gain based on possible slippage, predicted based on the current strategy.
        """
        return 0.00
        
        