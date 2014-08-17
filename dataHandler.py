__author__ = 'rsnyder'

import sqlite3
import quandl
#purpose of this class is to get data and store it


class DataHandler:

    conn = None
    c = None
    qdl = None

    def __init__(self):
        self.last_update = ''
        self.conn = sqlite3.connect('data/pietrader.db')
        self.c = self.conn.cursor()
        self.qdl = quandl.Quandl()

    def __del__(self):
        self.conn.close()

    def create_stock_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS stock
                    (symbol, date, open, high, low, close, volume, ex_dividend, split_ration,
                    adj_open, adj_high, adj_low, adj_close, adj_volume)''')
        self.conn.commit()

    def drop_stock_table(self):
        self.c.execute('''DROP TABLE iF EXISTS stock''')
        self.conn.commit()

    def get_last_update_date(self):
        results = self.c.execute('''SELECT MAX(date) from stock''')
        date = results.fetchone()
        return date[0]

    def update_stock_table(self, **kwargs):
        print "Adding stock data for: %s %s" % (kwargs["symbol"], kwargs["Date"])
        self.c.execute('''INSERT INTO stock
                    (symbol, date, open, high, low, close, volume, ex_dividend, split_ration,
                    adj_open, adj_high, adj_low, adj_close, adj_volume) VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (kwargs["symbol"], kwargs["Date"], kwargs["Open"], kwargs["High"], kwargs["Low"], kwargs["Close"],
                     kwargs["Volume"], kwargs["Ex-Dividend"], kwargs["Split Ratio"], kwargs["Adj. Open"],
                     kwargs["Adj. High"], kwargs["Adj. Low"], kwargs["Adj. Close"], kwargs["Adj. Volume"]))
        self.conn.commit()

    def create_symbol_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS symbols(symbol_id integer primary key autoincrement, symbol)''')
        self.conn.commit()

    def drop_symbol_table(self):
        self.c.execute('''DROP TABLE IF EXISTS symbols''')
        self.conn.commit()

    def update_symbols_table(self, *symbols):
        for symbol in symbols:
            print "Adding symbol: %s" % symbol
            self.c.execute('INSERT INTO symbols (symbol) VALUES (?)', (symbol,))
        self.conn.commit()

    def get_data_test(self, symbol):
        results = self.c.execute('''SELECT * FROM symbols where symbol = ?''', (symbol,))
        print results.fetchone()

    def init_load(self):
        #initial load of data to the table
        self.drop_symbol_table()
        print "This may take a while..."
        print "Creating symbols table..."
        self.create_symbol_table()

        print "Fetching Stock Symbols from Quandl..."
        symbols = self.qdl.get_symbols()

        print "Adding the symbols to the database..."
        self.update_symbols_table(*symbols)

        print "Symbols have been added..."
        print "Creating stock table..."
        self.drop_stock_table()
        self.create_stock_table()

        print "Retrieving stock info..."
        print "This may be a good time to read the documentation..."
        for symbol in symbols:
            stock_data = self.qdl.get_stock_by_date(symbol, '2012-01-01', '2014-08-15')
            for data in stock_data:
                self.update_stock_table(**data)

        print "Initial Load Complete"



    def create_favorite_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS favorites
                    (favorite_id integer primary key autoincrement, symbol, name)''')
        self.conn.commit()









