__author__ = 'rsnyder'
import quandl


class Stock:

    def __init__(self, symbol):
        self.qdl = quandl.Quandl()
        self.history = self.qdl.get_stock_by_date(symbol, self.qdl.last_year, self.qdl.today)
        data = self.history[0]
        if data:
            for key in data:
                setattr(self, key, data[key])
        else:
            print "No Data Found"

    def get_52_low(self):
        low = self.Open
        low_record = []
        #get history if it isn't loaded
        if not self.history:
            self.get_history()
        for data in self.history:
            if data["Open"] < low:
                low = data["Open"]
                low_record = data
        return low_record

    def get_52_high(self):
        high = self.Open
        high_record = []
        #get history if it isn't loaded
        if not self.history:
            self.get_history()
        for data in self.history:
            if data["Open"] > high:
                high = data["Open"]
                high_record = data
        return high_record

    def get_history(self):
        self.history = self.qdl.get_stock_by_date(self.symbol, self.qdl.last_year, self.qdl.today)

