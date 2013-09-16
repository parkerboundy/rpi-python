from imu import IMU
from udpsocket import UDPSocket
import time

sock = UDPSocket()
newimu = IMU()

while 1: 
	sock.send(str(newimu.heading()))
	time.sleep(1)

