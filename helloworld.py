import time, threading
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mt
import json
from googlefinance import getQuotes
from datetime import datetime

i = 1
price = []
clock = []
dates = []

 
def test_run(i):
    
    # print time
    print(time.ctime())
    
    # get stock data
    stock = getQuotes('AAPL')
    price.append(float(stock[0]['LastTradePrice']))
    
    # increase indices
    clock.append(time.ctime())
    i = i + 1
    
    dates.append(datetime.strptime(time.ctime() , "%a %b %d %H:%M:%S %Y"))
    mt.dates.date2num(dates)
    
    # write to csv
    csv_df = pd.DataFrame({'Price': price, 'Time': clock})
    csv_df.to_csv('AAPL.csv', index=False)
    
    # plot data
    plt.ion()
    plt.plot(dates,price)
    plt.pause(1)
    print price
    
    #reset timer
    i = 0
    
    # cyclic function call
    threading.Timer(1, test_run(i)).start()
    

if __name__ == "__main__":
    test_run(i)

