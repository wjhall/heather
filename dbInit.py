#!/usr/bin/python

import sqlite3

days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def zero_pad(n):
    if n<10:
        return "0"+str(n)
    return str(n)

conn = sqlite3.connect('heather.db')
c=conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS temp_log
( timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
lounge REAL,
spence REAL,
exterior REAL,
conservatory REAL,
bedroom REAL,
boilder INTEGER
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS bed_sched
( DOW TEXT,
Timestamp TEXT,
temperature REAL
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS lou_sched
( DOW Text,
Timestamp TEXT,
temperature REAL
);
''')

conn.commit()

sql_string="Insert into bed_sched (DOW,Timestamp,temperature) VALUES ('{}','{}',{})"
for day in days:
    for i in range(24):
        for j in range(60):
            c.execute(sql_string.format(day,zero_pad(i)+zero_pad(j),15.0))

sql_string="Insert into lou_sched (DOW,Timestamp,temperature) VALUES ('{}','{}',{})"
for day in days:
    for i in range(24):
        for j in range(60):
            c.execute(sql_string.format(day,zero_pad(i)+zero_pad(j),15.0))


conn.commit()
conn.close()
