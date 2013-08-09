import datetime
#from urllib import urlencode
import urllib2
#import time
#from hashlib import sha512
#from hmac import HMAC
#import base64
#import json
from exchange_api import ExchangeAPI
#from helpers.currencypairstate import CurrencyPairState

class ForexRealTime(ExchangeAPI):
           
          
    def perform(self):
        req = urllib2.Request("http://webrates.truefx.com/rates/connect.html?f=html")
        res = urllib2.urlopen(req).read()
        return res
          
    def get_currency_trade_pair_from_table(self,table,currency):
        ret = {}
        ret['return'] = {}
        ret['result'] = 'success'
        
        currency = currency[0:3] + "/" + currency[3:6]
        
        index_start = table.find(currency)
        index_end = table.find("/tr",index_start)
        table = table[index_start:index_end]
        
        index_time_start = table.find("<td>")
        index_time_end = table.find("</td>",index_time_start)
                                #because "<td>" is 4 in length, and timestamps are not down to microsecond, but rather, millisecond
        time_s = str(int(table[index_time_start+4:index_time_end])*1000)
        
        table = table[index_time_end:]
        
        index_bid_start = table.find("<td>")
        index_bid_end = table.find("</td>",index_bid_start)
        bid = float(table[index_bid_start+4:index_bid_end])
        
        table = table[index_bid_end:]
        
        index_bid2_start = table.find("<td>")
        index_bid2_end = table.find("</td>",index_bid2_start)
        bid += .00001 * float(table[index_bid2_start+4:index_bid2_end])
        
        table = table[index_bid2_end:]
        
        index_ask_start = table.find("<td>")
        index_ask_end = table.find("</td>",index_ask_start)
        ask = float(table[index_ask_start+4:index_ask_end])
        
        table = table[index_ask_end:]
        
        index_ask2_start = table.find("<td>")
        index_ask2_end = table.find("</td>",index_ask2_start)
        ask += .00001 * float(table[index_ask2_start+4:index_ask2_end])

        asks = [ask,0,time_s]
        bids = [bid,0,time_s]
        
        ret['return']['asks'] = [asks]
        ret['return']['bids'] = [bids]
        
        return ret     
           
    def get_data_from_exchange(self):
        
        ret = {}
        table = self.perform()
        
        currency = "EURUSD"
        ctp = self.get_currency_trade_pair_from_table(table,currency)
        ret[currency] = ctp

        currency = "GBPUSD"
        ctp = self.get_currency_trade_pair_from_table(table,currency)
        ret[currency] = ctp

        currency = "EURGBP"
        ctp = self.get_currency_trade_pair_from_table(table,currency)
        ret[currency] = ctp
        
        ret['active'] = 2
        time = datetime.datetime.now()
        ret['queried_at'] = time
        
        return ret
        

"""
EUR/USD	1340649703081	1.24	981	1.24	985	1.24712	1.25599	1.25476
USD/JPY	1340649692299	79.	686	79.	692	79.438	80.625	80.417
GBP/USD	1340649703163	1.55	590	1.55	598	1.55386	1.55950	1.55676
EUR/GBP	1340649703150	0.80	320	0.80	326	0.80195	0.80738	0.80600
USD/CHF	1340649702821	0.96	074	0.96	085	0.95603	0.96298	0.95696
EUR/JPY	1340649702830	99.	594	99.	603	99.159	101.121	100.934
EUR/CHF	1340649702534	1.20	083	1.20	091	1.20066	1.20151	1.20114
USD/CAD	1340649694192	1.02	940	1.02	950	1.02486	1.03181	1.02720
AUD/USD	1340649703430	0.99	924	0.99	934	0.99685	1.00555	1.00460
GBP/JPY	1340649703123	123.	984	123.	999	123.596	125.680	125.187"""

"""
<table><tr><td>EUR/USD</td><td>1340651163036</td><td>1.24</td><td>953</td><td>1.24</td><td>959</td><td>1.24712</td><td>1.25599</td><td>1.25476</td></tr><tr><td>USD/JPY</td><td>1340651163087</td><td>79.</td><td>697</td><td>79.</td><td>702</td><td>79.438</td><td>80.625</td><td>80.417</td></tr><tr><td>GBP/USD</td><td>1340651162205</td><td>1.55</td><td>637</td><td>1.55</td><td>649</td><td>1.55386</td><td>1.55950</td><td>1.55676</td></tr><tr><td>EUR/GBP</td><td>1340651162830</td><td>0.80</td><td>279</td><td>0.80</td><td>289</td><td>0.80195</td><td>0.80738</td><td>0.80600</td></tr><tr><td>USD/CHF</td><td>1340651163087</td><td>0.96</td><td>096</td><td>0.96</td><td>105</td><td>0.95603</td><td>0.96298</td><td>0.95696</td></tr><tr><td>EUR/JPY</td><td>1340651163072</td><td>99.</td><td>587</td><td>99.</td><td>597</td><td>99.159</td><td>101.121</td><td>100.934</td></tr><tr><td>EUR/CHF</td><td>1340651161679</td><td>1.20</td><td>083</td><td>1.20</td><td>091</td><td>1.20066</td><td>1.20151</td><td>1.20114</td></tr><tr><td>USD/CAD</td><td>1340651162883</td><td>1.02</td><td>944</td><td>1.02</td><td>954</td><td>1.02486</td><td>1.03181</td><td>1.02720</td></tr><tr><td>AUD/USD</td><td>1340651161716</td><td>0.99</td><td>926</td><td>0.99</td><td>935</td><td>0.99685</td><td>1.00555</td><td>1.00460</td></tr><tr><td>GBP/JPY</td><td>1340651162802</td><td>124.</td><td>040</td><td>124.</td><td>056</td><td>123.596</td><td>125.680</td><td>125.187</td></tr></table>
"""