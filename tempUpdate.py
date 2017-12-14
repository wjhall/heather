#!/usr/bin/python

import requests
import sqlite3
from sensor import *

def get_urldata(urlString):
    try:
        r=requests.get(urlString)
        if r.status_code==200:
            return float(r.text)
        return None
    except:
        return None

urlList = {"conservatory":"http://192.168.0.102:8080/conservatory",
           "exterior":"http://192.168.0.102:8080/exterior",
           "bedroom":"http://192.168.0.101:8080/bedroom"
           }

tempList={"conservatory":None,
          "exterior":None,
          "bedroom":None,
          "lounge":get_temp(probeMap["lounge"]),
          "spence":get_temp(probeMap["spence"]),
          "boiler":None
    }

for item, value in urlList.iteritems():
    tempList[item]=get_urldata(value)

tempList = {k: v for k, v in tempList.items() if v is not None}

sqlstr_1 = "INSERT into temp_log ("
sqlstr_2 = ") values ("

for k,v in tempList.items():
    sqlstr_1 = sqlstr_1 + k + ", "
    sqlstr_2 = sqlstr_2 + str(v) + ", "

sqlstr_1 = sqlstr_1[:-2]
sqlstr_2 = sqlstr_2[:-2]
sqlstr = sqlstr_1 + sqlstr_2 + ");"

conn = sqlite3.connect('heather.db')
c=conn.cursor()
c.execute(sqlstr)
conn.commit()
conn.close()
