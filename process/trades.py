import json
import pandas as pd

from collections import OrderedDict
from matplotlib import pyplot as plt
from matplotlib import animation
from requests import get
from datetime import date, datetime
get_ipython().magic(u'matplotlib inline')

BASE_URI = r'https://api.gemini.com/v1/trades/ethusd?'
API_KEY = r'1234'


# Gemini public API entry points: requests limited to 120 requests per minute
# Recommend not to exceed 1 request per second
#
# Gemini private API entry points: requests limited to 600 requests per minute
# Recommend not to exceed 5 requests per second

def api_trades():
    response = get(BASE_URI).json()
    df = pd.DataFrame(response)        .drop('exchange', axis = 1)        .sort_values(by = 'timestampms', ascending = True)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit = 's')
    df['timestampms'] = pd.to_datetime(df['timestamp'], unit = 'ms')
        
    print df
            
def main():
    api_trades()

if __name__ == '__main__':
    main()


