import json
import pandas as pd

from collections import OrderedDict
from matplotlib import pyplot as plt
from matplotlib import animation
from requests import get
from datetime import date, datetime
get_ipython().magic(u'matplotlib inline')

BOOK_URI = r'https://api.gemini.com/v1/book/ethusd?'
API_KEY = r'1234'


# Gemini public API entry points: requests limited to 120 requests per minute
# Recommend not to exceed 1 request per second
#
# Gemini private API entry points: requests limited to 600 requests per minute
# Recommend not to exceed 5 requests per second

def api_book(asks, bids, **kwargs):
    kwargs.update({'limit_asks': asks,
                   'limit_bids': bids
                  })
    response = get(BASE_URI, kwargs).json()
    bid_price, bid_amount = [], []
    for i in response['bids']:
        bid_price.append(i['price'])
        bid_amount.append(i['amount'])
    
    df = pd.DataFrame(response['asks']).sort_values(by = 'timestamp', ascending = True)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit = 's')
    df['bid_price'], df['bid_amount'] = bid_price, bid_amount
    
    return df

def calc_spread():
    book = api_book(100, 100)
    for row in book:
        book['price'] = book['price'].astype(float)
        book['bid_price'] = book['bid_price'].astype(float)
        book['spread'] = (book['price'] - book['bid_price']).astype(float)
    
    print book

def count_neg_spread(book):
    for i in book['spread']:
        if i < 0:
            pass
            
def main():
    calc_spread()

if __name__ == '__main__':
    main()