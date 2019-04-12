# -*- coding: utf-8 -*-

import pymysql

HOST="127.0.0.1"
PORT=3306
USER="root"
PASSWORD="123456"
DB="qbaobei"


def connect(HOST,PORT,USER,PASSWORD,DB):
    conn=pymysql.connect(host=HOST,port=PORT,user=USER,password=PASSWORD,db=DB)
    return conn

def get(conn):
    cursor=conn.cursor()
    result=cursor.execute('select * from jiajia_spider_article where id=22')
    all=cursor.fetchall()
    return result,all

def close(conn):
    conn.close()


if __name__=="__main__":
    CONN = connect(HOST,PORT,USER,PASSWORD,DB)
    id,data = get(CONN)
    print id,data[0][1]
    close(CONN)

#
#
