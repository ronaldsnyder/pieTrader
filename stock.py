__author__ = 'rsnyder'
import dataHandler


class Stock:
    dh = ''
    symbol = ''

    open = ''
    high = ''
    low = ''
    close = ''
    volume = ''
    dividend = ''
    split_ration = ''
    adj_open = ''
    adj_low = ''
    adj_close = ''
    adj_volume = ''

    def __init__(self, symbol):
        dh = dataHandler.DataHandler()
        #check last update, if today do nothing else update stock table to most recent
        last_update = dh.get_last_update_date(symbol)
        today = dh.get_today()
        if last_update != today:
            dh.load_updates(symbol)
        else:
            print "Stock data up to date"

        data = dh.get_data(symbol)
        print data

        #set instance variables

    def get_52_low(self):
        pass

    def get_52_high(self):
        pass

    def get_last_update(self):
        pass
