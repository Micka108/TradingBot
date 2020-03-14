#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-. iso-8859-1

###### Import ########

import os
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

###### Variable ######


###### Function ######


###### Program #######

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', '^GSPC']

    # We would like all available data from 01/01/2000 until 12/31/2016.
    start_date = '2010-01-01'
    end_date = '2016-12-31'

    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    f = web.DataReader("AAPL", "av-daily", start=datetime(2017, 2, 9),
        end=datetime(2017, 5, 24),
        api_key='JMGU7Q6I9YYYH8O1')
    print(f.loc["2017-02-09"])