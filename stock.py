__author__ = 'rsnyder'
import quandl


class Stock:

    def __init__(self, symbol):
        self.qdl = quandl.Quandl()
        try:
            self.history = self.qdl.get_stock_by_date(symbol, self.qdl.last_year, self.qdl.today)
            data = self.history[0]
            #for each key in the json set it as an attribute of the object.
            for key in data:
                setattr(self, key, data[key])
        except:
            print "Symbol is incorrect or could not communicate with Quandl"

    def __str__(self):
        print_string = "Ticker: " + self.symbol


    def get_52_low(self):
        low = self.Open
        low_record = []
        low_record = self.history[0]
        if self.history:
            for data in self.history:
                if data["Open"] < low:
                    low = data["Open"]
                    low_record = data
        else:
            low_record = 0

        return low_record

    def get_52_high(self):
        high = self.Open
        high_record = []
        if self.history:
            high_record = self.history[0]
            for data in self.history:
                if data["Open"] > high:
                    high = data["Open"]
                    high_record = data
        else:
            high_record = self.history[0]

        return high_record

    def get_52_average(self):
        average = 0
        if self.history:
            for data in self.history:
                average = average + data["Open"]
            if len(self.history) > 0:
                average /= len(self.history)
        return average



