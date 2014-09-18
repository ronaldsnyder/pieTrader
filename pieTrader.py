__author__ = 'rsnyder'
import analyze

def main():
    main_menu()

def main_menu():
    print "1. Print Favorite 52 Week Lows"
    print "2. Print Favorite 52 Week High"
    print "3. Print Favorites at 52 Week Low"
    print "4. Print Favorites at 52 Week High"
    print "5. Analyze a specific stock"
    print "0. Quit Application"


def stock_menu():
    print "1.  Get Current Price"
    print "2.  Get 52 High Price"
    print "3.  Get 52 Low Prince"
    print "4.  Get Average Price"
    print "5.  Back to Main Menu"
    print "0.  Quit Application"



if __name__ == "__main__":
    exit = False
    while not exit:
        main_menu()
        choice = raw_input("Enter a menu choice: ")
        if choice == '1':
            print analyze.favorites_52_low()
        elif choice == '2':
            print analyze.favorites_52_high()
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            stock_menu()
        elif choice == '0':
            exit = True
        else:
            print "Invalid choice"
