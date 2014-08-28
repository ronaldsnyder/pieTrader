__author__ = 'rsnyder'
import stock
import dataHandler
import user

dh = dataHandler.DataHandler()
user = user.User()
dh.init_load()
symbols = dh.get_symbols()
favorites = user.get_favorites()

def print_all_52_low():
    lows = []
    for symbol in symbols:
        mystock = stock.Stock(symbol[0])
        lows.append(mystock.get_52_low())
    return lows

def favorites_52_low():
    lows = []
    for favorite in favorites:
        print favorite
        mystock = stock.Stock(favorite)
        lows.append(mystock.get_52_low())
    return lows






