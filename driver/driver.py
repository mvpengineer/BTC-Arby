import sys, os, datetime

# add the current file to the system path so we can import everything
sys.path.append(os.getcwd())

from exchange_api.historical import Historical
from exchange_api.mtgoxrealtime import MtGoxRealTime
from exchange_api.true_forex_realtime import ForexRealTime
from exchange_api.record_forward import RecordForward
from helpers.trade import Trade
from helpers.currencypairstate import CurrencyPairState
from strategy.singleexchangestrategy import SingleExchangeStrategy
from helpers.email_protocol import Email
from threading import Thread
import pymongo
from pymongo import Connection

realtime = True
strategy = 'strategy_name'

portfolio_USD = 100.00    #how many BTC of USD I have
portfolio_EUR = 100.00
portfolio_BTC = 100.00

#e = Email()
#e.email("subject","body")


#def myfunc(num):
#    for i in range(10):
#        print num

#for i in range(5):
#    t = Thread(target=myfunc, args=(i,))
#    t.start()

#exit()



if realtime:
    auth_file = open("../../Barbie_auth.txt",'r')
    key = auth_file.readline().strip()
    secret = auth_file.readline().strip()
    api_mtgox = MtGoxRealTime(key,secret)
    api_forex = ForexRealTime()
    
    recorder = RecordForward(api_mtgox,api_forex)
    six_hours = 6*60*60
    three_hours = 3*60*60
    recording_thread_mtgox = Thread(target = recorder.start_mtgox, args = (three_hours,) )
    recording_thread_forex = Thread(target = recorder.start_forex, args = (three_hours,) )
    
    recording_thread_mtgox.start()
    recording_thread_forex.start()
    
    #print api.get_data_from_exchange()
    
else:
    api = Historical()
    #print api.get_data_from_exchange(datetime.datetime.now())
    #api.execute_trade([Trade(**trade_options)])

    s = SingleExchangeStrategy()
    print s.limit_order()
    #print s.gain(buy_trade, sell_trade, buy_currency_pair_state, sell_currency_pair_state)
    #print s.limit_order()

