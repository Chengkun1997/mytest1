#!/usr/bin/python

import psycopg2

import os
import json
# from flask_cors import *
from flask_cors import CORS, cross_origin
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request
app = Flask(__name__)

cors = CORS(app)


@app.route('/getAll', methods=[ 'GET'])
# @app.route('/index1', methods=[ 'POST'])

def getcontent():
   conn = psycopg2.connect(database="postgis_picture", user="postgres", password="123456789", host="127.0.0.1", port="5432")
   print(conn)
   print ("Opened database successfully")

   cur = conn.cursor()

   #select 查询记录
   cur.execute("SELECT id, name,age, address, salary  from COMPANY")
   rows = cur.fetchall()
   # for row in rows:
   #    print( "ID = ", row[0])
   #    print ("NAME = ", row[1])
   #    print( "ADDRESS = ", row[2])
   #    print ("SALARY = ", row[3], "\n")

   # print ("Operation done successfully")

   # conn.commit()
   # conn.close()

   para = []
   for i in rows:
        text = {'name':i[1],'age':i[2],'address':i[3],'salary':i[4]}
        # print(text)
        para.append(text)
   return json.dumps(para, ensure_ascii=False, indent=4)

if __name__ == '__main__':
   #  app.run(host='0.0.0.0', port=5590)
   # app.run(host='127.0.0.1', port=5590)
   # app.run(host='127.0.0.1', port=8081)
   app.run(host='127.0.0.1',debug=True)

#如此，在postman中Add Request,用GET或POST， Send 这个  http://127.0.0.1:5000/getAll    就可以