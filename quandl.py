__author__ = 'rsnyder'

import urllib
import json
from ConfigParser import SafeConfigParser
import datetime
import os


class Quandl(object):

    def __init__(self):
        self.today = self.get_today()
        self.last_year = self.get_one_year_ago()
        config_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + "pieTrader.config"
        parser = SafeConfigParser()
        parser.read(config_path)
        parser = SafeConfigParser()
        parser.read('pieTrader.config')
        if parser.has_section('quandl') & parser.has_option('quandl', 'token'):
            self.token = "&auth_token=" + parser.get('quandl', 'token')
        else:
            print "You do not have a Quandl Token which limits the amount of API calls and the use of this program.  \
                  Get an API key at http://www.quandl.com/users/sign_up"
            self.token = ''

    #returns a dictionary of the most recent stock data
    def get_most_recent(self, symbol):
        stock_url = "http://www.quandl.com/api/v1/datasets/WIKI/%s.json?sort_order=desc%s" \
                    % (symbol, self.token)
        stock_json = urllib.urlopen(stock_url)
        stock_data = json.loads(stock_json.read())
        keys = []
        for key in stock_data['column_names']:
            key = key.replace(" ", "")
            key = key.replace(".", "")
            keys.append(key)
        values = stock_data["data"][0]
        stock_dict = dict(zip(keys, values))
        stock_dict['symbol'] = symbol
        return stock_dict

    #function returns a list of dictionaries of stock data
    def get_stock_by_date(self, symbol, start_date, end_date):
        stock_url = "http://www.quandl.com/api/v1/datasets/WIKI/%s.json?trim_start=%s&trim_end=%s?sort_order=desc%s" \
                    % (symbol, start_date, end_date, self.token)
        stock_json = urllib.urlopen(stock_url)
        stock_data = json.loads(stock_json.read())
        if 'column_names' in stock_data:
            keys = []
            for key in stock_data['column_names']:
                key = key.replace(" ", "")
                key = key.replace(".", "")
                keys.append(key)
            values = stock_data["data"]
            stock_history = []
            for value in values:
                temp = dict(zip(keys, value))
                temp['symbol'] = symbol
                stock_history.append(temp)
        else:
            stock_history = []
        return stock_history

    def get_symbols(self):
        all_symbols = []
        for page in range(1, 12):
            symbols_url = "http://www.quandl.com/api/v2/datasets.json?query=*&source_code=WIKI&per_page=300&page=%s%s" \
                          % (page, self.token)
            symbol_lookup = urllib.urlopen(symbols_url)
            symbols = json.loads(symbol_lookup.read())
            symbols = symbols["docs"]
            for symbol in symbols:
                all_symbols.append(symbol["code"])
        return all_symbols

    @staticmethod
    def get_one_year_ago():
        date = datetime.date.today()
        date += datetime.timedelta(days=-365)
        return date

    @staticmethod
    def get_today():
        now = datetime.date.today()
        return now.strftime("%Y-%m-%d")


