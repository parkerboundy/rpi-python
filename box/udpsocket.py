import threading
import Queue
import socket

class UDPSocket(threading.Thread):

	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.daemon = True
		
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

	def _send(self, data):
		self.s.sendto(data, ('<broadcast>', 5050))

	def run(self):
		while True:
			message = self.queue.get()
			self._send(message)
			self.queue.task_done()