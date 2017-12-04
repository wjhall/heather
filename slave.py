#!/usr/bin/python

import os
import web
import sys
from sensor import *

sys.stderr = open('/home/pi/Desktop/log.txt', 'ab')

app=web.auto_application()



class spence(app.page):
    def GET(self):
        return get_temp(probeMap.spence)
    
class lounge(app.page):
    def GET(self):
        return get_temp(probeMap.lounge)

class conservatory(app.page):
    def GET(self):
        return get_temp(probeMap.conservatory)

class bedroom(app.page):
    def GET(self):
        return get_temp(probeMap.bedroom)

class exterior(app.page):
    def GET(self):
        return get_temp(probeMap.exterior)		

app.run()
