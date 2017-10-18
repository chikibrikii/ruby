
# coding: utf-8

# In[3]:

import threading
from threading import Thread
from book import api_book, calc_spread
from trades import api_trades


# In[ ]:

if __name__ == '__main__':
    Thread(target = api_book).start()
    Thread(target = api_trades).start()

