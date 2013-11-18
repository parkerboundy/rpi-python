import threading
import Queue
import socket
import logging

class UDPSocket(threading.Thread):

	def __init__(self, queue):
		self.log = logging.getLogger(__name__)
		
		threading.Thread.__init__(self)
		self.queue = queue
		self.daemon = True

		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

	def send(self, data):
		self.log.info('Sending socket with message "%s"', data)
		self.s.sendto(data, ('<broadcast>', 5050))

	def run(self):
		while True:
			message = self.queue.get()
			self.log.info('Received message from queue "%s"', message)
			self.send(message)
			self.queue.task_done()