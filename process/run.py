import threading
import multiprocessing
import pandas as pd 

from threading import Thread
from book import api_book, calc_spread
from trades import api_trades


# create a self-contained multiprocessing pool and distribute async processes
# within this run script.

def apply_async():
    pass
    
def main():
    Thread(target = calc_spread).start()
    Thread(target = api_trades).start()
    apply_async()

if __name__ == '__main__':
    main()