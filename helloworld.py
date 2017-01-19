import time, threading
import numpy as np 
import matplotlib.pyplot as plt
import json

i = 1
tm = []
 
def test_run(i):
    global tm
    i = i + 1
    print(time.ctime())
    from googlefinance import getQuotes
    stock = getQuotes('AAPL')
    tm.append(float(stock[0]['LastTradePrice']))
    print tm
    threading.Timer(3, test_run(i)).start()


if __name__ == "__main__":
    
    test_run(i)

