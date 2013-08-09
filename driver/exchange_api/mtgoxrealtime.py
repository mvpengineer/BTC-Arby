import datetime
from urllib import urlencode
import urllib2
import time
from hashlib import sha512
from hmac import HMAC
import base64
import json
from exchange_api import ExchangeAPI
from helpers.currencypairstate import CurrencyPairState

volume_multiplier = 100000000.00  #1.0e8
price_multiplier = 100000.00      #1.0e5
how_many_trades = 10

def get_nonce():
    return int(time.time()*100000)

def sign_data(secret, data):
    return base64.b64encode(str(HMAC(secret, data, sha512).digest()))
      
class MtGoxRealTime(ExchangeAPI):
    def __init__(self, auth_key, auth_secret):
        self.auth_key = auth_key
        self.auth_secret = base64.b64decode(auth_secret)

        
    def build_query(self, req={}):
        req["nonce"] = get_nonce()
        post_data = urlencode(req)
        headers = {}
        headers["User-Agent"] = "GoxApi"
        headers["Rest-Key"] = self.auth_key
        headers["Rest-Sign"] = sign_data(self.auth_secret, post_data)
        return (post_data, headers)
        
    def perform(self, path, args):
        data, headers = self.build_query(args)
        req = urllib2.Request("https://mtgox.com/api/1/"+path, data, headers)
        res = urllib2.urlopen(req, data)
        return json.load(res)
        
    def execute_trade(self, trade):
        
        path = trade.get_currency_pair()+"/private/order/add"
        args = {}
        if trade.get_buy_BTC():
            args['type'] = 'bid'
        else:
            args['type'] = 'ask'
        args['amount_int'] = trade.get_volume() * volume_multiplier
        args['price_int'] = trade.get_price() * price_multiplier
        
        self.perform(path,args)
    
    def get_currency_trade_pair_from_JSON(self,json,currency):
        if json['result'] == 'error':
            return None
        asks = json['return']['asks']    
        bids = json['return']['bids']
        asks_length = len(asks)
        bids_length = len(bids)
        
        bid_array = []
        ask_array = []
        for i in range(asks_length):
            ask_array.append((asks[i]['price'],asks[i]['amount'],asks[i]['stamp']))
            
        for i in range(bids_length):                        #reverse order for bids, and also extra one for 0-indexed
            bid_array.append((bids[bids_length - i - 1]['price'],bids[bids_length - i - 1]['amount'],bids[bids_length - i -1]['stamp']))    

        ask_array = sorted(ask_array)
        bid_array = sorted(bid_array)[::-1]                   #reverse sorted order

        ask_array_shortened = ask_array[0:how_many_trades]
        bid_array_shortened = bid_array[0:how_many_trades]
        
        json['return']['asks'] = ask_array_shortened
        json['return']['bids'] = bid_array_shortened
        return json
        
    def get_data_from_exchange(self):
        
        args = {}
        ret = {}
        currency = "BTCUSD"
        path = currency+"/fulldepth"
        ctp = self.get_currency_trade_pair_from_JSON(self.perform(path,args),currency)
        ret[currency] = ctp
        
        currency = "BTCEUR"
        path = currency+"/fulldepth"
        ctp = self.get_currency_trade_pair_from_JSON(self.perform(path,args),currency)
        ret[currency] = ctp
        currency = "BTCGBP"
        path = currency+"/fulldepth"
        ctp = self.get_currency_trade_pair_from_JSON(self.perform(path,args),currency)
        ret[currency] = ctp
        
        ret['active'] = 2
        time = datetime.datetime.now()
        ret['queried_at'] = time
        
        return ret
        
