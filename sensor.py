#!/usr/bin/python

probeMap={
	'spence':'/sys/bus/w1/devices/28-031644f127ff/w1_slave',
	'lounge':'/sys/bus/w1/devices/28-031644d50dff/w1_slave',
	'conservatory':'/sys/bus/w1/devices/28-0316473cfdff/w1_slave',
	'bedroom':'/sys/bus/w1/devices/28-03164778ccff/w1_slave',
	'exterior':'/sys/bus/w1/devices/28-0316453747ff/w1_slave'
}

def get_temp(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        if line.split(" ")[-1]!="YES\n":
            return None
        line = f.readline()
        return float(line.split("t=")[1])/1000
