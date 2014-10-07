__author__ = 'rsnyder'

from ConfigParser import SafeConfigParser
from stock import Stock

#user is for getting favorites
#should we include favorite functions in user class instead of in analyze.py?
class User(object):
    def _init__(self):
        pass

    #returns a list of favorites in pieTrader.config
    def get_favorites(self):
        favorites = []
        parser = SafeConfigParser()
        parser.read('pieTrader.config')
        if parser.has_section('stocks') & parser.has_option('stocks', 'favorites'):
            favorites = parser.get('stocks', 'favorites')
        favorites = favorites.replace(" ", "")
        favorites = favorites.split(",")
        return favorites
