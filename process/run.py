import threading
from threading import Thread
from book import api_book, calc_spread
from trades import api_trades

def main():
    Thread(target = api_book).start()
    Thread(target = api_trades).start()

if __name__ == '__main__':
    main()