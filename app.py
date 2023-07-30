# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:55:19 2022
"""

from flask import Flask
import schedule
import time
import threading
from line_notify import LineNotify
from twse import get_twse_trade
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

f = open('token.txt', 'r')
token = f.readline().strip()
notify = LineNotify(token)

@app.route("/")
def hello():
    print("Hello")
    notify.send("hello test")
    return "hello test"

@app.route("/v1")
def trade_transaction():
    result = get_twse_trade()
    if result[0] == 200:
        notify.send(result[1] + "三大法人買賣金額統計表", image_path='./resources/'+result[1]+'.png')
        return result[0]
    else:
        pass

def run_scheduler():
    # Schedule the job to run on weekdays (Monday to Friday) at 15:00 (3:00 PM)
    schedule.every().monday.at("15:00").do(hello)
    schedule.every().tuesday.at("15:00").do(hello)
    schedule.every().wednesday.at("15:00").do(hello)
    schedule.every().thursday.at("15:00").do(hello)
    schedule.every().friday.at("15:00").do(hello)
    # schedule.every(10).seconds.do(trade_transaction)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
    
    app.run(debug=False, use_reloader=False)
