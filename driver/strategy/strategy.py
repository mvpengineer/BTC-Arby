

class Strategy(object):
    rowML_model = 0

    def incorporate_new_data(self, currency_pair_states):
        for currency_pair_state in currency_pair_states:
            pass

    def limit_order(self):
        pass

    def commision_gain(self,trade):
        fixed_cost = -.000001    #BTC    
        #MT
        #add to DB schema
        #fixed_cost = DB.fixed_cost[trade.get_currency_pair()]
        variable_cost = -.00001  #percent
        #variable_cost = DB.variable_cost[trade.get_currency_pair()]

        return fixed_cost + variable_cost * trade.get_price() * trade.get_volume()
            
    def gain(self, buy_trade, sell_trade, buy_currency_pair_state, sell_currency_pair_state):
        commision_gain_total = self.commision_gain(buy_trade) + self.commision_gain(sell_trade)
        slippage_gain_total = self.predicted_slippage_gain(buy_trade, buy_currency_pair_state) + self.predicted_slippage_gain(sell_trade, sell_currency_pair_state)
        spread_gain_total = self.spread_gain(buy_trade, sell_trade, buy_currency_pair_state, sell_currency_pair_state)
        print commision_gain_total
        print spread_gain_total
        return commision_gain_total + slippage_gain_total + spread_gain_total

