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


@app.route('/picApp', methods=[ 'POST'])

def indextest():
    paramsData = request.get_json('paramsData') # 接收外界参数
    print("Serv-inputData",paramsData)
    print("Serv-inputData.inputData",paramsData["inputData"])
    data1 = getcontent(str(paramsData["inputData"]))
    return data1

def getcontent(inputData):
   conn = psycopg2.connect(database="postgis_picture", user="postgres", password="123456789", host="127.0.0.1", port="5432")
   print(conn)
   print ("Opened database successfully")

   cur = conn.cursor()

#    inputData=33

   # INSERT 插入记录
   cur.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('33', 22, '%s', 8888 )"%inputData)

   print ("Records created successfully")
   conn.commit()
   
   
   #select 查询记录
   cur.execute("SELECT id, name, address, salary  from COMPANY")
   rows = cur.fetchall()

   conn.close()
#    para = []
#    for i in rows:
#         text = {'name':i[0],'class':i[1],'number':i[2],'score':i[3]}
#         para.append(text)
   i =rows[-1]
   para=[{'name':i[0],'class':i[1],'number':i[2],'score':i[3]}]
   return json.dumps(para, ensure_ascii=False, indent=4)
    

if __name__ == '__main__':
   app.run(host='127.0.0.1',port=5590)

#如此，在postman中Add Request,用GET或POST， Send 这个  http://127.0.0.1:5590/index1    就可以