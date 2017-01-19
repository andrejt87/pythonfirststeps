import time, threading
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

i = 1
price = []
clock = []

 
def test_run(i):
    i = i + 1
    print(time.ctime())
    from googlefinance import getQuotes
    stock = getQuotes('AAPL')
    price.append(float(stock[0]['LastTradePrice']))
    clock.append(time.ctime())
    submission = pd.DataFrame({'Price': price, 'Time': clock})
    submission.to_csv('AAPL.csv', index=False)
    plt.ion()
    plt.plot(price)
    plt.pause(1)
    print price
    threading.Timer(3, test_run(i)).start()
    

if __name__ == "__main__":
    test_run(i)

