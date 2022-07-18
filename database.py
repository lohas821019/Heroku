# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:06:20 2022

@author: Jason
"""



import psycopg2
import os

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a twsestock').read()[:-1]
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

conn = psycopg2.connect(database="testdb", user = "postgres", password = "pass123", host = "192.168.1.75", port = "80")

