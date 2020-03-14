#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-. iso-8859-1

###### Import ########

import json
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from enum import Enum
from pprint import pprint
from time import mktime

###### Variable ######


###### Function ######


###### Program #######

class YahooFinance:
    SCRAPE_URL = "https://finance.yahoo.com/quote/"
    BASE_URL = "https://query1.finance.yahoo.com/v7/finance"
    USER_AGENT = "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"

    def __init__(self, stock):
        self.stock = stock
        self.header, self.crumb, self.cookies = self._get_cookie_crumb(self.stock)

    def _get_cookie_crumb(self, stock):
    
        url = f"{self.SCRAPE_URL}{stock}/history"
        with requests.session():
            header = {
                'Connection': 'keep-alive',
                'Expires': '-1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': self.USER_AGENT
            }
            
            website = requests.get(url, headers=header)
            soup = BeautifulSoup(website.text, 'lxml')
            crumb = re.findall('"CrumbStore":{"crumb":"(.+?)"}', str(soup))

            return (header, crumb[0], website.cookies)

    def convert_to_unix(self, date):

        datum = datetime.strptime(date, '%d-%m-%Y')
        return int(mktime(datum.timetuple()))

    def load_csv_data(self, interval='1d', day_begin='01-02-2010', day_end='28-03-2020'):

        day_begin_unix = self.convert_to_unix(day_begin)
        day_end_unix = self.convert_to_unix(day_end)

        url = f"{self.BASE_URL}/download/{self.stock}"
        params = {
            "period1": day_begin_unix,
            "period2": day_end_unix,
            "interval": interval,
            "events": "history",
            "crumb": self.crumb
        }
        website = requests.get(url, headers=self.header, cookies=self.cookies, params=params)
           
        return website.text.split('\n')[:-1]

    def quoteResponse(self):

        url = f"{self.BASE_URL}/quote"
        params = {
            "symbols" : self.stock
        }
        website = requests.get(url, headers=self.header, cookies=self.cookies, params=params)
        return website.json()

    def optionChain(self):

        url = f"{self.BASE_URL}/options/{self.stock}"
        website = requests.get(url, headers=self.header, cookies=self.cookies)
        return website.json()

    def chart(self, params):
        url = f"{self.BASE_URL}/chart/{self.stock}"
        website = requests.get(url, headers=self.header, cookies=self.cookies, params=params.value)
        return website.json()

    def setStock(stock):
        self.stock = stock
        self.header, self.crumb, self.cookies = self._get_cookie_crumb(self.stock)

class ChartYahooFinance(Enum):
    HistoricalPricesDaily = {
           "range": "2y",
           "interval": "1d",
           "indicators": "quote",
           "includeTimestamps": "true",
    }
    HistoricalPricesWeekly = {
           "range": "5y",
           "interval": "1wk",
           "indicators": "quote",
           "includeTimestamps": "true"
    }
    HistoricalPricesMonthly = {
           "range": "max",
           "interval": "1mo",
           "indicators": "quote",
           "includeTimestamps": "true"
    }
    IntradayPrices1m = {
           "range": "1d",
           "interval": "1m",
           "indicators": "quote",
           "includeTimestamps": "true"
    }
    IntradayPrices5m = {
           "range": "5d",
           "interval": "5m",
           "indicators": "quote",
           "includeTimestamps": "true"
    }
    IntradayPrices15m = {
           "range": "5d",
           "interval": "15m",
           "indicators": "quote",
           "includeTimestamps": "true"
    }
    IntradayPrices60m = {
           "range": "1mo",
           "interval": "60m",
           "indicators": "quote",
           "includeTimestamps": "true"
    }

if __name__ == "__main__":
    yt = YahooFinance("FB")
    pprint(yt.chart(ChartYahooFinance.IntradayPrices1m))
    print(ChartYahooFinance.IntradayPrices1m)