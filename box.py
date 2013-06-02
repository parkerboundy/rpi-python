from imu import IMU
import time

newimu = IMU()

while 1: 
	print newimu.heading()
	time.sleep(1)

