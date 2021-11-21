# -*- codeing = utf-8 -*-
# @Time : 2021/11/19 10:14
# @Author : CHY
# @File : Test.py
# @Software : PyCharm

import sqlite3
import requests
import os

if not os.path.exists('image'):
    os.makedirs('image')
datalist = []
pic=[]
conn = sqlite3.connect("movies.db")
cur = conn.cursor()
sql = "select * from movie250"
data = cur.execute(sql)
for item in data:
    datalist.append(item)
for url in datalist:
    pic.append(url[2])
# m=1
# for i in pic:
#     img=requests.get(i,timeout=5)
#     filename = "image/" + str(m) + ".jpg"
#     fp = open(filename, 'wb')
#     fp.write(img.content)
#     fp.close()
#     m+1
for i in pic:
    print(i)

cur.close()
conn.close()
