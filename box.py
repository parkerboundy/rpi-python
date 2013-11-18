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
import argparse
import Queue
import logging

from box.database import Database
from box.datapoint import DataPoint
from box.udpsocket import UDPSocket

def main():
	logging.basicConfig(filename='logs/box.log')
	logging.error("about to start")
def main(args):
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
	parser = argparse.ArgumentParser(description='Sailing Data Collection Server')
	parser.add_argument('-p','--port_number', type=int, metavar='Port', help='UDP port number', default=5050)
	parser.add_argument('-l', '--log_level', type=str, choices=['debug', 'info', 'warning', 'error', 'critical'], help='Log level to use', default='debug')
	main(vars(parser.parse_args()))