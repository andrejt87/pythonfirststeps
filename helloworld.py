import time, threading
i = 0
def test_run(i):
    i = i + 1
    print(time.ctime())
    from googlefinance import getQuotes
    import json
    stock = getQuotes('AAPL')
    print float(stock[0]['LastTradePrice'])
    threading.Timer(3, test_run(i)).start()


if __name__ == "__main__":
    
    test_run(i)

