__author__ = 'rsnyder'
import quandl

#class for handling stock data, takes a symbol to instantiate.
#sets all keys in QUANDL class as attributes.
class Stock:

    def __init__(self, symbol):
        self.qdl = quandl.Quandl()
        try:
            self.history = self.qdl.get_stock_by_date(symbol, self.qdl.last_year, self.qdl.today)
            data = self.history[0]
            #for each key in the json set it as an attribute of the object, this sets todays data as the attributes.
            for key in data:
                setattr(self, key, data[key])
        except:
            print "Symbol is incorrect or could not communicate with Quandl"

    #print the ticker symbol
    def __str__(self):
        print_string = "Ticker: " + self.symbol

    #get the 52 week low record, returns dictionary
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

    #get the 52 week high record, returns dictionary
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

    #get the 52 week low record, returns the average price of stock data
    def get_52_average(self):
        average = 0
        if self.history:
            for data in self.history:
                average = average + data["Open"]
            if len(self.history) > 0:
                average /= len(self.history)
        return average



