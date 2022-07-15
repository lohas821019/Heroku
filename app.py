# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:55:19 2022

@author: Jason
"""

from flask import Flask
from twse import *
from line_notify import LineNotify
from flask_apscheduler import APScheduler

app = Flask(__name__)  # 实例化，可视为固定格式
app.debug = True  # Flask内置了调试模式，可以自动重载代码并显示调试信息
app.config['JSON_AS_ASCII'] = False  # 解决flask接口中文数据编码问题

f = open('token.txt', 'r')
token = f.readlines()
token = token[0][:-1]
notify = LineNotify(token)

@app.route("/")
class Config(object):
    JOBS = [
        {
            'id': 'trade_transaction', # 一個標識
            'func': '__main__:trade_transaction',     # 指定執行的函式 
            # 'args': (1, 2),              # 傳入函式的引數
            'trigger': 'cron',                            # 指定任務觸發器 cron
            'day_of_week': 'mon-fri',              # 每週1至周5早上6點執行 
            'hour': 15,
            'minute': 00   
        }
    ]

    SCHEDULER_API_ENABLED = True
def trade_transaction():
    result = get_twse_trade()
    if result[0] == 200:
        notify.send(result[1] + "三大法人買賣金額統計表", image_path='./'+result[1]+'.png')
    return result[0]


# notify.send( "文字測試")
# notify.send("圖片測試", image_path='./test.jpg')
# notify.send("貼紙測試",sticker_id=283, package_id=4)
# notify.send("圖片&貼紙測試", image_path='./'+result[1]+'.png',sticker_id=283,package_id=4)

if __name__ == '__main__':
    app = Flask(__name__)                 # 例項化flask
    app.config.from_object(Config())      # 為例項化的 flask 引入配置 

    scheduler = APScheduler()                  # 例項化 APScheduler
    # it is also possible to enable the API directly
    # scheduler.api_enabled = True
    scheduler.init_app(app)                    # 把任務列表放入 flask
    scheduler.start()                          # 啟動任務列表
    app.run()                                  # 啟動 flask
    
