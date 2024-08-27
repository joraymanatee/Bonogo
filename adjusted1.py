import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup
import requests


# URL of the Wikipedia page containing S&P 500 tickers
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Send a GET request to the URL
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})

rows = table.find_all('tr')[1:]

tickers = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 0:
        ticker = cells[0].text.strip()
        tickers.append(ticker)

stock_highs = pd.DataFrame()
stock_close = pd.DataFrame()
stock_lows = pd.DataFrame()
stock_volume = pd.DataFrame()
stock_open = pd.DataFrame()
stock_adjclose = pd.DataFrame()

for symbol in tickers[0:5]:

    stock = yf.download(symbol, period='1y')
    
    stock_lows[symbol] = stock['Low']
    stock_highs[symbol] = stock['High']
    stock_volume[symbol] = stock['Volume']
    stock_close[symbol] = stock['Close']
    stock_open[symbol] = stock['Open']
    stock_adjclose[symbol] = stock['Adj Close']

    
print(stock)

stock_highs.to_csv("stockHighs.csv")
stock_lows.to_csv("stockLows.csv")
stock_close.to_csv("stockClose.csv")
stock_volume.to_csv("slockVolume.csv")
stock_open.to_csv("stocksOpen.csv")
stock_adjclose.to_csv("stocksAdjclose.csv")

A = yf.Ticker("A")
print(A.info)