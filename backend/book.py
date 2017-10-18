import json
import pandas as pd

from collections import OrderedDict
from matplotlib import pyplot as plt
from matplotlib import animation
from requests import get
from datetime import date, datetime
get_ipython().magic(u'matplotlib inline')


BASE_URI = r'https://api.gemini.com/v1/book/ethusd?'
API_KEY = r'1234'

def api(asks, bids, **kwargs):
    kwargs.update({'limit_asks': asks,
                   'limit_bids': bids
                  })
    response = get(BASE_URI, kwargs).json()
    bid_price, bid_amount, spread = [], [], []
    for result in response:
        df = pd.DataFrame(response['asks'])
#         for row in df:
#             df['timestamp'] = datetime.fromtimestamp(df['timestamp'].astype(str)).\
#                                                     strftime('%Y-%m-%d %H:%M:%S')

    for i in response['bids']:
        bid_price.append(i['price'])
        bid_amount.append(i['amount'])
    df['bid_price'] = bid_price
    df['bid_amount'] = bid_amount
#     df['timestamp'] = map(lambda x: pd.to_datetime(x, unit='ms'), df['timestamp'])
    
    return df

def calc_spread():
    book = api(5, 5)
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
    book = calc_spread()

if __name__ == '__main__':
    main()