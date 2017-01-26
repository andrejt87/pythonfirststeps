import time, threading, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mt
import json
from googlefinance import getQuotes
from datetime import datetime

clock = []
dates = []

 
def fetch_data(symbol):
    global Matrix
    # get stock data
    stock = getQuotes(symbol)
    price = []
    for x in range(0, len(stock)):
        price.append(float(stock[x]['LastTradePrice']))

    Matrix = np.hstack((Matrix, np.atleast_2d(price).T))    
    print Matrix
    #Matrix = np.append([float(stock[x-1]['LastTradePrice'])],[float(stock[x]['LastTradePrice'])])
    # increase indices
    clock.insert(0,time.ctime())
    
    dates.append(datetime.strptime(time.ctime() , "%a %b %d %H:%M:%S %Y"))
    mt.dates.date2num(dates)
    
    # write to csv
    #csv_df = pd.DataFrame({'Price': price, 'Time': dates})
    #csv_df.to_csv("/Users/andrejtupikin/pythonfirststeps/" + str(symbol) + '.csv', index=False)
    
    
def plotting():

    # plot data
    plt.ion()
    #plt.plot(dates,price,'r') # plotting t,a separately 
    #plt.plot(dates,Matrix[1],'b') # plotting t,b separately 
    print(time.ctime())
    plt.pause(2)
    
    
def processing():
       fetch_data(sys.argv[1:]) 
       
def create_figure():
    global figure_1
    global axes_1
    
    #figure_1 = plt.figure()
    #axes_1 = figure_1.add_subplot(111)

def init():
    global figure_1, axes_1, price, clock, dates, symbol, x, Matrix,Temp_array
    price = []
    clock = []
    dates = []
    
    Temp_array = np.zeros((len(sys.argv)-1, 1))
    Matrix = np.zeros((len(sys.argv)-1, 1))

if __name__ == "__main__":
    init()
    create_figure()
    while True:
        processing()
        plotting()