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
# import dataframe_image as dfi
import os
import matplotlib.pyplot as plt
import warnings

import matplotlib
matplotlib.use('Agg')
warnings.filterwarnings('ignore', category=UserWarning)

# plt.rc("font",family='YouYuan')
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
#plt.rcParams['font.family'] = ['Microsoft JhengHei']
# plt.rcParams['font.family'] = 'Arial' 
# plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei',]


#pandas 結果對齊
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

def get_twse_trade():
    
    today = time.gmtime()
    year = str(today.tm_year)
    month = str(today.tm_mon)
    date = str(today.tm_mday)

    zero = '0'
    if len(month) == 1:
        month = zero + month

    if len(date) == 1:
        date = zero + date

    todaydate = year+month+date
    print(todaydate)
    print(type(todaydate))
    # todaydate = '20230720'
    headers = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    url = 'https://www.twse.com.tw/fund/BFI82U?response=json&dayDate='+ todaydate
    data = requests.get(url).text

    print(data)
    
    if data == '{"stat":"很抱歉，沒有符合條件的資料!","hints":"單位：元"}':
        return (404,data)
    else:
        json_data = json.loads(data)
        Stock_data = json_data['data']
        StockPrice = pd.DataFrame(Stock_data, columns = ['單位名稱', '買進金額', '賣出金額', '買賣差額'])
        StockPrice['買進金額'] = round(StockPrice['買進金額'].str.replace(',','').astype(float)/100000000,2)
        StockPrice['賣出金額'] = round(StockPrice['賣出金額'].str.replace(',','').astype(float)/100000000,2)
        StockPrice['買賣差額'] = round(StockPrice['買賣差額'].str.replace(',','').astype(float)/100000000,2)
        StockPrice['單位名稱'] = StockPrice['單位名稱'].replace('外資及陸資(不含外資自營商)', '外資及陸資')
        print(type(StockPrice))

        # Create a table-like chart
        fig, ax = plt.subplots()

        # Convert DataFrame to list of lists
        table_data = StockPrice.values.tolist()

        # Create the table with cell colors (optional)
        table = ax.table(cellText=table_data, colLabels=StockPrice.columns, cellLoc='center', loc='center', cellColours=None)

        # Table style customization (optional)
        table.auto_set_font_size(False)
        table.set_fontsize(12)

        # Remove axis ticks and labels
        ax.axis('off')

        # Save the table chart as an image
        plt.savefig("./resources/"+todaydate +".png")
    
        return (200,todaydate,StockPrice)
    

        # result = StockPrice.to_numpy()
        
        # fig,ax = render_mpl_table(StockPrice, header_columns=0, col_width=2.0)
        # fig.savefig('./resources/'+todaydate +".png")
        
        # if not os.path.exists(todaydate+'.jpg'):
        #     dfi.export(StockPrice, './resources/'+todaydate+'.jpg')
        # return (200,todaydate,result)


def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
    mpl_table.auto_set_font_size(True)
    mpl_table.set_fontsize(font_size)

    for k, cell in mpl_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax.get_figure(), ax

#%%

# from bs4 import BeautifulSoup
# from lxml import etree

# def get_histock_option():
    
#     url = 'https://histock.tw/stock/three.aspx'
#     data = requests.get(url).text
    
#     soup = BeautifulSoup(data, "html.parser")
#     # print(soup.prettify())  #輸出排版後的HTML內容
    
#     dom = etree.HTML(str(soup))