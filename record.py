
import Queue

#from box.arduino import Arduino
from box.common.database import Database
from box.record.datapoint import DataPoint
#from box.imu import IMU
from box.record.udpsocket import SocketClient
from box.record.udpsocket import SocketServer
from box.common.util import settings
from box.common.util import ArgumentParser
from box.common.util import logging

def main(args):
	
	logging.info('Starting Main')

	dbQueue = Queue.Queue()
	sockQueue = Queue.Queue()

	point = DataPoint()
	client = SocketClient(sockQueue)
	server = SocketServer()
	d = Database(dbQueue)

	client.start()
	server.start()
	d.start()

	while True:
		s = raw_input()
		if s == "close":
			break;
		else:
			dbQueue.put(int(s))
			#sockQueue.put(s)

if __name__ == "__main__":
	parser = ArgumentParser()

	main(vars(parser.parse_args()))