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
        mystock = stock.Stock(favorite)
        lows.append(mystock.get_52_low())
    return lows

def print_all_52_high():
    highs = []
    for symbol in symbols:
        mystock = stock.Stock(symbol[0])
        highs.append(mystock.get_52_high())
    return highs

def favorites_52_high():
    highs = []
    for favorite in favorites:
        mystock = stock.Stock(favorite)
        highs.append(mystock.get_52_high())
    return highs

def favorites_52_average():
    average = []
    for favorite in favorites:
        temp_stock = {}
        mystock = stock.Stock(favorite)
        temp_stock['symbol'] = mystock.symbol
        temp_stock['average'] = mystock.get_52_average()
        average.append(temp_stock)
    return average



def pretty_print(mystock):
    print "\n"
    print mystock["symbol"] + "\t" + str(mystock["Open"]) + " \t" + str(mystock["Date"])
    print "\n"

def pretty_print_averages(mystock):
    print stock["symbol"] + "\t" + str(stock["average"])

def pretty_print_list(mystock):
    print "\n"
    for stock in mystock:
        print stock["symbol"] + "\t" + str(stock["Open"]) + " \t" + str(stock["Date"])
    print "\n"

def pretty_print_averages_list(mystock):
    print "\n"
    for stock in mystock:
        print stock["symbol"] + "\t" + str(stock["average"])
    print "\n"







