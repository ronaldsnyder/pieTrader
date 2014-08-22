__author__ = 'rsnyder'

import sqlite3
import quandl

class DataHandler:

    conn = None
    c = None
    qdl = None

    def __init__(self):
        self.conn = sqlite3.connect('data/pietrader.db')
        self.c = self.conn.cursor()
        self.qdl = quandl.Quandl()

    def __del__(self):
        self.conn.close()

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

    def symbols_exist(self):
        found = False
        symbols = self.c.execute("SELECT * from symbols where symbol = 'GOOG'")
        if self.c.fetchone():
            found = True
        return found

    def init_load(self):
        #initial load of data to the table

        print "Creating symbols table..."
        self.create_symbol_table()

        print "Checking to see if symbols exist"
        if not self.symbols_exist():
            print "Symbols need to be loaded.  This may take a while..."
            print "Fetching Stock Symbols from Quandl..."
            symbols = self.qdl.get_symbols()

            print "Adding the symbols to the database..."
            self.update_symbols_table(*symbols)

            print "Symbols have been added..."
        else:
            print "Symbols exist"








