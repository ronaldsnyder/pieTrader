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
                    (symbol, date, open, high, low, close, volume, ex_divident, split_ration,
                    adj_open, adj_high, adj_low, adj_close, adj_volume)''')
        conn.close()

    @staticmethod
    def drop_stock_table():
        conn = sqlite3.connect('data/pietrader.db')
        c = conn.cursor()
        c.execute('''DROP TABLE stock''')
        conn.commit()
        conn.close()

    def get_last_update_date(self):
        pass

    #method needs changed to use dictionary
    @staticmethod
    def update_stock_table(*stock):
        #debugging print statement below, needs removed
        #print (stock[0], stock[1], stock[2], stock[3], stock[4], stock[5], stock[6], stock[7], stock[8], stock[9],
              # stock[10], stock[11], stock[12])
        print stock
        conn = sqlite3.connect('data/pietrader.db')
        c = conn.cursor()
        c.execute('''INSERT INTO stock
                    (symbol, date, open, high, low, close, volume, ex_divident, split_ration,
                    adj_open, adj_high, adj_low, adj_close, adj_volume) VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (stock[0], stock[1], stock[2], stock[3], stock[4], stock[5], stock[6], stock[7], stock[8],
                     stock[9], stock[10], stock[11], stock[12]))
        conn.commit()
        conn.close()

    @staticmethod
    def get_data_test(code):
        conn = sqlite3.connect('data/pietrader.db')
        c = conn.cursor()
        results = c.execute('''SELECT * FROM stock where symbol = ?''', (code,))
        print results.fetchone()

    @staticmethod
    def init_load():
        #initial load of data to the table
        qdl = quandl.Quandl()
        symbols = qdl.get_symbols()
        for symbol in symbols:
            print "Adding data for: %s" % symbol
            #stock = qdl.get_stock(symbol)
            DataHandler.update_stock_table(symbol)

    @staticmethod
    def create_favorite_table():
        conn = sqlite3.connect('data/pietrader.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE favorites
                    (id integer primary key autoincrement, symbol, name)''')
        conn.close()

    def set_favorites(self):
        pass

    def get_favorites(self):
        pass









