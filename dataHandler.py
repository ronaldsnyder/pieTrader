__author__ = 'rsnyder'

import sqlite3
import quandl
#purpose of this class is to get data and store it


class DataHandler:

    def __init__(self):
        self.last_update = ''

    @staticmethod
    def create_stock_table():
        conn = sqlite3.connect('data/pietrader.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE stock
                    (date, open, high, low, close, volume, ex_divident, split_ration,
                    adj_open, adj_high, adj_low, adj_close, adj_volume)''')
        conn.close()

    def get_last_update_date(self):
        pass

    @staticmethod
    def update_stock_table(stock):
        pass

    @staticmethod
    def init_load():
        #initial load of data to the table
        qdl = quandl.Quandl()
        symbols = qdl.get_symbols()
        for symbol in symbols:
            print "Adding data for: %s" % symbol
            stock = qdl.get_stock(symbol)
            DataHandler.update_stock_table(stock)







