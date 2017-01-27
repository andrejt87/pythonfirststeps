import time, threading, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mt
import json
import os
from googlefinance import getQuotes
from datetime import datetime
from time import gmtime, strftime

 
def fetch_data(symbol):
    global Matrix
    # get stock data
    stock = getQuotes(symbol)
    price = []
    for x in range(0, len(stock)):
        price.append(float(stock[x]['LastTradePrice']))
    
    if (Matrix == []):
        Matrix = np.atleast_2d(price).T
    else:
        Matrix = np.hstack((Matrix, np.atleast_2d(price).T))
        
    print Matrix
    #Matrix = np.append([float(stock[x-1]['LastTradePrice'])],[float(stock[x]['LastTradePrice'])])
    # increase indices
    clock.insert(0,time.ctime())
    
    dates.append(datetime.strptime(time.ctime() , "%a %b %d %H:%M:%S %Y"))
    mt.dates.date2num(dates)
    
    # write to csv
    if not os.path.exists("/Users/andrejtupikin/pythonfirststeps/Data/" + strftime("%d %b %Y", gmtime()) + "/"):
        os.makedirs("/Users/andrejtupikin/pythonfirststeps/Data/" + strftime("%d %b %Y", gmtime()) + "/")
    
    for x in range(0, len(sys.argv)-1):
        csv_df = pd.DataFrame({'Price': Matrix[x], 'Time': dates})
        csv_df.to_csv("/Users/andrejtupikin/pythonfirststeps/Data/" + strftime("%d %b %Y", gmtime()) + "/" + str(sys.argv[x+1]) + '.csv', index=False)
    
def plotting():

    # plot data
    plt.cla()
    for x in range(0, len(sys.argv)-1):
        
        plt.plot(dates,Matrix[x]) # plotting t,b separately 
    
    print(time.ctime())
    plt.pause(2)
    
    
def processing():
       fetch_data(sys.argv[1:]) 
      

def init():
    global figure_1, axes_1, price, clock, dates, x, Matrix
    
    clock = []
    dates = []
    Matrix = []

if __name__ == "__main__":
    init()
    while True:
        processing()
        plotting()