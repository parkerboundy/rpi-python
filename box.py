'''
from imu import IMU
from udpsocket import UDPSocket
import time

sock = UDPSocket()
newimu = IMU()

while 1: 
	sock.send(str(newimu.heading()))
	time.sleep(1)
'''

from box.database import Database
from box.datapoint import DataPoint

point = DataPoint()
d = Database()

point.speed = 1
d.insert(point)