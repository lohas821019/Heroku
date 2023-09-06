# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:55:19 2022
"""

from flask import Flask
from line_notify import LineNotify
from twse import get_twse_trade

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = BackgroundScheduler()

# 定义一个触发器，每隔10秒执行一次
trigger = IntervalTrigger(seconds=10)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

f = open('token.txt', 'r')
token = f.readline().strip()
notify = LineNotify(token)

@app.route("/hello")
def hello():
    print("Hello")
    notify.send("hello test")
    return "hello test"

@app.route("/")
def trade_transaction():
    result = get_twse_trade()

    if result[0] == 404:
        notify.send(result[1])
        pass
    elif result[0] == 200:
        notify.send(result[1] + "三大法人買賣金額統計表", image_path='./resources/'+result[1]+'.png')
        return result[0]
    else:
        pass

# 添加定时任务
scheduler.add_job(trade_transaction, trigger=trigger)

if __name__ == '__main__':
    try:
        scheduler.start()
        app.run(debug=False, use_reloader=False)
    finally:
        scheduler.shutdown()
