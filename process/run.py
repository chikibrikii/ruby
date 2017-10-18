import threading
from threading import Thread
from book import api_book, calc_spread
from trades import api_trades


def main():
    Thread(target = calc_spread).start()
    Thread(target = api_trades).start()
    return

if __name__ == '__main__':
    main()