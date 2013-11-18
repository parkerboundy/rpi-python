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
import Queue
import logging

from box.database import Database
from box.datapoint import DataPoint
from box.udpsocket import UDPSocket

def main():
	logging.basicConfig(filename='box.log')
	logging.error("about to start")
	dbQueue = Queue.Queue()
	sockQueue = Queue.Queue()

	#sock = UDPSocket(sockQueue)
	#sock.start()
	d = Database(dbQueue)
	d.start()

	while True:
		s = raw_input()
		if s == "close":
			break;
		else:
			dbQueue.put(int(s))
#point = DataPoint()
#d = Database()

#point.speed = 1
#d.insert(point)

if __name__ == "__main__":
    main()