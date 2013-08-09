import pymongo
from pymongo import Connection
import datetime
import json
import time

class RecordForward(object):
    
    
    def __init__(self,api_mtgox,api_forex):
        connection = Connection() 
        self.forward_trades_db = connection.forward_trades_db
        self.api_mtgox = api_mtgox
        self.api_forex = api_forex
        self.wipe_db = False
        
    def put_new_record(self,trades,cps_dict):
        trades.insert(cps_dict)
        
    def start_mtgox(self, length_of_thread):
        now = datetime.datetime.now()
        done = now + datetime.timedelta(seconds = length_of_thread)
        trades = self.forward_trades_db.mtgox_forward_trades
        if self.wipe_db:
            trades.remove({})
        while 1:
            now = datetime.datetime.now()
            if now > done:
                break           # move to 1 and then to 0 so that there is always an active trade in the DB 
            active_trades = trades.update({'active':2},{ '$set' : {'active':1} })    
            self.put_new_record(trades,self.api_mtgox.get_data_from_exchange())  
            active_trades = trades.update({'active':1},{ '$set' : {'active':0} })
            
            now = datetime.datetime.now()
            if now > done:
                break
            time.sleep(2)
            now = datetime.datetime.now()
            if now > done:
                break
            
            
    def start_forex(self, length_of_thread):
        now = datetime.datetime.now()
        done = now + datetime.timedelta(seconds = length_of_thread)
        trades = self.forward_trades_db.forex_forward_trades
        if self.wipe_db:
            trades.remove({})
        while 1:
            now = datetime.datetime.now()
            if now > done:
                break
            active_trades = trades.update({'active':2},{ '$set' : {'active':1} })    
            self.put_new_record(trades,self.api_forex.get_data_from_exchange())  
            active_trades = trades.update({'active':1},{ '$set' : {'active':0} })
            
            now = datetime.datetime.now()
            if now > done:
                break
            time.sleep(5)
            now = datetime.datetime.now()
            if now > done:
                break
            
        #json = posts.find()
        #for post in json:
        #   print post