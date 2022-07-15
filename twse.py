# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:01:38 2022

@author: Jason
"""

import pandas as pd
import numpy as np
import json
import requests
import time
import dataframe_image as dfi
import os

def get_twse_trade():
    today = time.gmtime()

    year = str(today.tm_year)
    month = str(today.tm_mon)
    date = str(today.tm_mday)

    zero = '0'
    if len(month) == 1:
        month = zero + month
    elif len(date) == 1:
        date = zero + date

    todaydate = year+month+date

    headers = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    url = 'https://www.twse.com.tw/fund/BFI82U?response=json&dayDate='+ todaydate
    data = requests.get(url).text

    if data == '{"stat":"很抱歉，沒有符合條件的資料!"}':
        return 404
    else:
        json_data = json.loads(data)
        Stock_data = json_data['data']
        StockPrice = pd.DataFrame(Stock_data, columns = ['單位名稱', '買進金額', '賣出金額', '買賣差額'])

        if not os.path.exists(todaydate+'.png'):
            dfi.export(StockPrice, todaydate+'.png')
        
        return (200,todaydate)



