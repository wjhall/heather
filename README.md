# HEAting The Home Electronically and Remotely

## V2, with actualy backups of codebase

**below maps of DS18B20 serial#**

- 192.168.0.100 Master (lounge, spence) 28-031644d50dff, 28-031644f127ff
- 192.168.0.101 Slave (bedroom) 28-03164778ccff
- 192.168.0.102 Slave (exterior, Conservatory) 28-0316453747ff, 28-0316473cfdff

**git setup (replace [] with content, do not reatain []):**
```
cd Desktop
git config --global user.email [your email here]
git config --global user.name [your name here]
mkdir heather
git init
git remote add origin https://github.com/wjhall/heather.git
git pull||push origin master
```
**setup to run webserver at startup**
```
sudo apt-get install gnome-schedule
crontab -e
```
- add:
```
@reboot sudo python /home/pi/Desktop/heather/slave.py
```
- save/close/reboot/test

**SQL setup**
```
sudo apt-get install sqlite3
```
run dbInit.py to setup heather.db with temp_log, bed_sched and lou_sched tables with sched tables initialiesd with weekly values to 15.0



**Logging**

tempUpdate.py is to run on the master and will log temperatures to db.
to run per minuite, use following in crontab -e
```
* * * * * sudo python /home/pi/Desktop/heather/slave.py
```

**Todo list:**

- [ ] Clone relay/boiler slave
- [x] Create database
- [x] Create logging table in db
- [x] Create schedule table in db
- [x] Create routine for logging temps
- [ ] Create routine for effecting schedule based on logged temps
- [ ] Create webUI
