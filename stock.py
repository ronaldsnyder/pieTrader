__author__ = 'rsnyder'
import quandl


class Stock:

    def __init__(self, symbol):
        self.qdl = quandl.Quandl()
        data = self.qdl.get_most_recent(symbol)
        if data:
            for key in data:
                setattr(self, key, data[key])
                print key
        else:
            print "No Data Found"

    def get_52_low(self):
        pass

    def get_52_high(self):
        pass

    def get_last_update(self):
        pass
