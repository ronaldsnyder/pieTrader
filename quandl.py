__author__ = 'rsnyder'

import urllib
import json
from ConfigParser import SafeConfigParser


class Quandl:

    def __init__(self):
        #read config file to get token and remove from this class
        parser = SafeConfigParser()
        parser.read('pieTrader.config')
        if parser.has_section('quandl') & parser.has_option('token'):
            self.token = "&auth_token="parser.get('quandl', 'token')
        else:
            print "You do not have a Quandl Token which limits the amount of API calls and the use of this program.  \
                  Get an API key at http://www.quandl.com/users/sign_up"
            self.token = ''

    def get_stock(self, code):
        stock_url = "http://www.quandl.com/api/v1/datasets/WIKI/%s.json?sort_order=desc%s" \
                    % (code, self.my_token)

        stock_json = urllib.urlopen(stock_url)
        stock_data = json.loads(stock_json.read())
        stock_data = stock_data["data"]
        stock_data = stock_data[0]
        return stock_data

    def get_stock_by_date(self, stock, start_date, end_date):
        stock_url = "http://www.quandl.com/api/v1/datasets/WIKI/%s.json?trim_start=%s&trim_end=%s%s" \
                    % (stock, start_date, end_date, self.my_token)

        stock_json = urllib.urlopen(stock_url)
        stock_history = json.loads(stock_json.read())
        stock_history = stock_history["data"]
        return stock_history

    def get_symbols(self):
        all_symbols = []
        for page in range(1, 12):
            symbols_url = "http://www.quandl.com/api/v2/datasets.json?query=*&source_code=WIKI&per_page=300&page=%s%s" \
                          % (page, self.my_token)
            symbol_lookup = urllib.urlopen(symbols_url)
            symbols = json.loads(symbol_lookup.read())
            symbols = symbols["docs"]


            for symbol in symbols:
                all_symbols.append(symbol["code"])

        return all_symbols


