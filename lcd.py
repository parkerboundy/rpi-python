import smbus

class LCD:
	
	def __init__(self, address):
		self.LCD_ADDRESS = address
		self.bus = smbus.SMBus(1)

	def write_data(self, data):
		self.bus.write_i2c_block_data(self.LCD_ADDRESS, 0, self.convert_to_bytes(data))

	def convert_to_bytes(self, data):
		bytes = []
		data = str(data)
		for item in data:
			bytes.append(ord(item))
		return bytes
