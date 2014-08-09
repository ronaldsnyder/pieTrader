__author__ = 'rsnyder'

import sqlite3
#purpose of this class is to get data and store it


class DataHandler:

    def __init__(self):
        pass

    def delete_stock_table(self):
        conn = sqlite3.connect('data/pietrader.db')
        c = self.conn.cursor()
        c.execute('''CREATE TABLE stock
                    (date, open, high, low, close, volume, ex_divident, split_ration,
                    adj_open, adj_high, adj_low, adj_close, adj_volume)''')
        conn.close()


