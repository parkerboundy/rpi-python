
import Queue
import logging

#from box.arduino import Arduino
from box.database import Database
from box.datapoint import DataPoint
#from box.imu import IMU
from box.udpsocket import SocketClient
from box.udpsocket import SocketServer
from box.util import settings
from box.util import parser

def main(args):

	logging.basicConfig(filename='logs/box.log', level=args['log_level'].upper(), format='%(asctime)s:%(levelname)s:%(module)s:%(message)s')

	dbQueue = Queue.Queue()
	sockQueue = Queue.Queue()

	point = DataPoint()
	client = SocketClient(sockQueue)
	server = SocketServer()
	client.start()
	server.start()
	#d = Database(dbQueue)
	#d.start()

	while True:
		s = raw_input()
		if s == "close":
			break;
		else:
			#dbQueue.put(int(s))
			sockQueue.put(s)

if __name__ == "__main__":
	main(vars(parser.parse_args()))