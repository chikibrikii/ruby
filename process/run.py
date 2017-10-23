import threading
import pandas as pd
import multiprocessing as mp 

from threading import Thread
from book import get_book, create_book_df
from trades import get_trades, create_trades_df


# create a self-contained multiprocessing pool and distribute async processes
# within this run script.

def apply_async():
    pass
    
def main():
    Thread(target = create_book_df).start()
    Thread(target = create_trades_df).start()
    apply_async()

if __name__ == '__main__':
    main()