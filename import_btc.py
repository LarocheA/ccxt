import ccxt

exchange = ccxt.bitcoin()

data = excahnge.fetch_ticker('BTC/USD')

print(data)
