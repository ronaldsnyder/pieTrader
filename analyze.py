__author__ = 'rsnyder'
import quandl
import stock
import dataHandler

dh = dataHandler.DataHandler()
dh.init_load()
symbols = dh.get_symbols()

def print_all_52_low():
    lows = []
    i = 0
    for symbol in symbols:
        i += 1
        print symbol[0] + " " + str(i)
        mystock = stock.Stock(symbol[0])
        lows.append(mystock.get_52_low())
    return lows





