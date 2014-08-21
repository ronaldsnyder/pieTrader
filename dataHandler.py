__author__ = 'rsnyder'

import sqlite3
import quandl
import datetime
#purpose of this class is to get data and store it


class DataHandler:

    conn = None
    c = None
    qdl = None
    today = None
    last_update = None

    def __init__(self):
        self.conn = sqlite3.connect('data/pietrader.db')
        self.c = self.conn.cursor()
        self.qdl = quandl.Quandl()
        self.today = self.get_today()

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

    def get_last_update_date(self, symbol):
        results = self.c.execute('''SELECT MAX(date) from stock WHERE symbol = ?''', (symbol,))
        date = results.fetchone()
        date = datetime.datetime.strptime(date[0], "%Y-%m-%d").date()
        date += datetime.timedelta(days=1)
        return date

    def get_one_year_ago(self):
        date = datetime.date.today()
        date += datetime.timedelta(days=-365)
        return date

    def get_today(self):
        now = datetime.date.today()
        return now.strftime("%Y-%m-%d")

    def update_stock_table(self, **kwargs):
        print "Adding stock data for: %s %s" % (kwargs["symbol"], kwargs["Date"])
        self.c.execute('''INSERT OR REPLACE INTO stock
                    (symbol, date, open, high, low, close, volume, ex_dividend, split_ration,
                    adj_open, adj_high, adj_low, adj_close, adj_volume) VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (kwargs["symbol"], kwargs["Date"], kwargs["Open"], kwargs["High"], kwargs["Low"], kwargs["Close"],
                     kwargs["Volume"], kwargs["Ex-Dividend"], kwargs["SplitRatio"], kwargs["AdjOpen"],
                     kwargs["AdjHigh"], kwargs["AdjLow"], kwargs["AdjClose"], kwargs["AdjVolume"]))
        self.conn.commit()

    #Methods for symbols
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

    def get_symbols(self):
        symbols = self.c.execute('''SELECT symbol from symbols order by symbol DESC''')
        return symbols.fetchall()

    def get_stored_data(self, symbol):
        results = self.c.execute('''SELECT * FROM stock where symbol = ? ORDER by date ASC''',
                                 (symbol,))
        return results.fetchone()

    def init_load(self):
        #initial load of data to the table
        self.drop_symbol_table()
        self.drop_stock_table()
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

    def load_updates(self, symbol):
        stock_data = self.qdl.get_stock_by_date(symbol, self.today, last_update,)
        if stock_data:
            for data in stock_data:
                self.update_stock_table(**data)
                print data
        else:
            print "No update for " + symbol

    def create_favorite_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS favorites
                    (favorite_id integer primary key autoincrement, symbol, name)''')
        self.conn.commit()









