import time, threading
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mt
import json
from googlefinance import getQuotes
from datetime import datetime
from matplotlib.ticker import ScalarFormatter

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
    #clock.append(time.ctime())
    clock.insert(0,time.ctime())
    i = i + 1
    
    dates.append(datetime.strptime(time.ctime() , "%a %b %d %H:%M:%S %Y"))
    mt.dates.date2num(dates)
    
    # write to csv
    csv_df = pd.DataFrame({'Price': price, 'Time': dates})
    csv_df.to_csv('AAPL.csv', index=False)
    
    # plot data
    plotting(dates,price)
    
    # print price
    print price
    
    #reset timer
    i = 0
    
    # cyclic function call
    threading.Timer(1, test_run(i)).start()
    
def plotting(x_val,y_val):

    # plot data
    #plt.ion()
    axes_1.clear()
    axes_1.ticklabel_format(useOffset=False)
    axes_1.set_title(str(y_val[-1]))
    axes_1.plot(x_val, y_val)
    plt.pause(2)
    

if __name__ == "__main__":
    figure_1 = plt.figure()
    axes_1 = figure_1.add_subplot(111)
    test_run(i)

