#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-. iso-8859-1

###### Import ########

import requests

###### Variable ######


###### Function ######


###### Program #######

class AlphaVantage:
    API_URL = "https://www.alphavantage.co/query"
    USER_AGENT = "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"

    def __init__(self, api_key, stock="", api_url=API_URL):
        self.api_key = api_key
        self.api_url = api_url
        self.stock = stock




if __name__ == "__main__":
    pass