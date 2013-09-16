import socket

class UDPSocket:

	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

	def send(self, data):
		self.s.sendto(data, ('<broadcast>', 5050))

