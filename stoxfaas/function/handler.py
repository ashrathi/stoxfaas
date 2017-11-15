import pandas as pd
import pandas_datareader.data as web
from datetime import datetime as dt, timedelta

def handle(st):
    end = dt.now()
    start = end - timedelta(days=7)
    try:
        df = web.DataReader(st, "yahoo", start, end)
        print(df.to_string())
    except:
        print('No such symbol or unknown error')
        return 1
    return 0
