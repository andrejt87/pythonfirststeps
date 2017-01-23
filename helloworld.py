import time, threading, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mt
import json
from googlefinance import getQuotes
from datetime import datetime

price = []
clock = []
dates = []

 
def fetch_data(symbol):
    
    # get stock data
    stock = getQuotes(symbol)
    price.append(float(stock[0]['LastTradePrice']))
    
    # increase indices
    clock.insert(0,time.ctime())
    
    dates.append(datetime.strptime(time.ctime() , "%a %b %d %H:%M:%S %Y"))
    mt.dates.date2num(dates)
    
    # write to csv
    csv_df = pd.DataFrame({'Price': price, 'Time': dates})
    csv_df.to_csv("/Users/andrejtupikin/pythonfirststeps/" + str(symbol) + '.csv', index=False)
    
    
def plotting():

    # plot data
    #plt.ion()
    axes_1.clear()
    axes_1.ticklabel_format(useOffset=False)
    #axes_1.set_title(str(y_val[-1]))
    axes_1.set_title(symbol)
    axes_1.plot(dates, price)
    #plt.annotate(str(symbol) + ":" + str(price[-1]), xy=(0.05, 0.95), xycoords='axes fraction')
    print(time.ctime())
    print price
    plt.pause(2)
    
    
def processing():
       fetch_data(sys.argv[1:]) 
       
def create_figure():
    global figure_1
    global axes_1
    
    figure_1 = plt.figure()
    axes_1 = figure_1.add_subplot(111)

def init():
    global figure_1, axes_1, price, clock, dates, symbol
    price = []
    clock = []
    dates = []
    symbol = sys.argv[1:]

if __name__ == "__main__":
    init()
    create_figure()
    while True:
        processing()
        plotting()

