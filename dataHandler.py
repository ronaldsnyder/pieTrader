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
                    (symbol, date, open, high, low, close, volume, ex_dividend, split_ration,
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

    @staticmethod
    def update_stock_table(**kwargs):
        conn = sqlite3.connect('data/pietrader.db')
        c = conn.cursor()
        c.execute('''INSERT INTO stock
                    (symbol, date, open, high, low, close, volume, ex_dividend, split_ration,
                    adj_open, adj_high, adj_low, adj_close, adj_volume) VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (kwargs["symbol"], kwargs["Date"], kwargs["Open"], kwargs["High"], kwargs["Low"], kwargs["Close"],
                     kwargs["Volume"], kwargs["Ex-Dividend"], kwargs["Split Ratio"], kwargs["Adj. Open"],
                     kwargs["Adj. High"], kwargs["Adj. Low"], kwargs["Adj. Close"], kwargs["Adj. Volume"]))
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









