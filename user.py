__author__ = 'rsnyder'

from ConfigParser import SafeConfigParser

class User():
    def _init__(self):
        pass

    def get_favorites(self):
        favorites = []
        parser = SafeConfigParser()
        parser.read('pieTrader.config')
        if parser.has_section('stocks') & parser.has_option('stocks', 'favorites'):
            favorites = parser.get('stocks', 'favorites')
        favorites = favorites.replace(" ", "")
        favorites = favorites.split(",")
        return favorites
