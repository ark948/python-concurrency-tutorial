# a multithreaded program that scraps stock prices from the yahoo finance website
# pip install requests lxml

import threading
import requests
from lxml import html

class Stock(threading.Thread):
    def __init__(self, symbol: str) -> None:
        super().__init__()

        self.symbol = symbol
        self.url = f'https://finance.yahoo.com/quote/{symbol}'
        self.price = None

    def run(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        # note: without valid headers, yahoo will return 404
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            # parse the HTML
            tree = html.fromstring(response.text)
            # get the price in text
            # every element on webpage, can be selected using its XPath
            price_text = tree.xpath(
                '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()')
            # note: if yahoo changes the page structure, XPath must be updated
            if price_text:
                try:
                    self.price = float(price_text[0].replace(',', ''))
                except ValueError:
                    self.price = None

    def __str__(self):
        return f'{self.symbol}\t{self.price}'

# main.py 

symbols = ['MSFT', 'GOOGL', 'AAPL', 'META']
threads = []

for symbol in symbols:
    t = Stock(symbol)
    threads.append(t)    
    t.start()
    

for t in threads:
    t.join()
    print(t)
