#!/usr/bin/python

import requests
from sensor import *

def get_urldata(urlString):
    r=requests.get(urlString)
    if r.status_code==200:
        return float(r.text)
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

print tempList

