__author__ = 'rsnyder'
import analyze
import stock

def main():
    main_menu()

def main_menu():
    print "1. Print Favorite 52 Week Lows"
    print "2. Print Favorite 52 Week High"
    print "3. Print Favorite 52 Week Average"
    print "4. Print Favorites at 52 Week Low"
    print "5. Print Favorites at 52 Week High"
    print "6. Analyze a specific stock"
    print "0. Quit Application"


def stock_menu():
    print "1.  Get Current Price"
    print "2.  Get 52 High Price"
    print "3.  Get 52 Low Prince"
    print "4.  Get Average Price"
    print "5.  Back to Main Menu"



if __name__ == "__main__":
    exit = False
    while not exit:
        main_menu()
        choice = raw_input("Enter a menu choice: ")
        if choice == '1':
            analyze.pretty_print_list(analyze.favorites_52_low())
            raw_input("Press any key to continue")
        elif choice == '2':
            analyze.pretty_print_list(analyze.favorites_52_high())
            raw_input("Press any key to continue")
        elif choice == '3':
            analyze.pretty_print_averages_list(analyze.favorites_52_average())
            raw_input("Press any key to continue")
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            main_menu = False
            mysymbol = raw_input("Enter a symbol: ")

            try:
                mystock = stock.Stock(mysymbol)
            except:
                print "Invalid Symbol, try again"

            while not main_menu:
                stock_menu()
                stock_choice = raw_input("Enter a menu choice: ")
                if stock_choice == '1':
                    print mystock.Open
                elif stock_choice == "2":
                    analyze.pretty_print(mystock.get_52_high())
                elif stock_choice == "3":
                    analyze.pretty_print(mystock.get_52_low())
                elif stock_choice == "4":
                    print mystock.symbol + "\t average: " + str(mystock.get_52_average())
                elif stock_choice == "5":
                    main_menu = True
                else:
                    print "Invalid Choice"
        elif choice == '0':
            exit = True
        else:
            print "Invalid choice"
