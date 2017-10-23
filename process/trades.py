import json
import pandas as pd

from collections import OrderedDict
from matplotlib import pyplot as plt
from matplotlib import animation
from requests import get
from datetime import date, datetime


TRADES_URI = r'https://api.gemini.com/v1/trades/ethusd?'
API_KEY = r'1234'

# Gemini public API entry points: requests limited to 120 requests per minute
# Recommend not to exceed 1 request per second
#
# Gemini private API entry points: requests limited to 600 requests per minute
# Recommend not to exceed 5 requests per second

def get_trades():
    response = get(TRADES_URI).json()

    return response

def create_trades_df():
    response = get_trades()
    trades_df = pd.DataFrame(response)\
        .drop('exchange', axis = 1)\
        .sort_values(by = 'timestampms', ascending = True)
    trades_df['timestamp'] = pd.to_datetime(trades_df['timestamp'], unit = 's')
    trades_df['timestampms'] = pd.to_datetime(trades_df['timestamp'], unit = 'ms')

    return trades_df
