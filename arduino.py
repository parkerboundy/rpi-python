import smbus
import struct

bus = smbus.SMBus(1)

data = bus.read_i2c_block_data(0x04, 0x01, 32)
#print data
for i in range(0, 7):
	bytes = data[4*i:4*i+4]
	#print bytes
	if i < 6:
		print struct.unpack('<L', "".join(map(chr, bytes)))[0]
	else:
		print struct.unpack('<l', "".join(map(chr, bytes)))[0]
		
class ARDUINO: 

	# register addresses
	ARDUINO_ADDRESS = 0x04
	ARDUINO_GPS_REG = 0x01
	ARDUINO_WIND_REG = 0x02

	def __init__(self):
		self.bus = smbus.SMBus(1)

	def write_register(self, register):
		self.bus.write_byte(self.ARDUINO_ADDRESS, register)

	def read_gps(self):
		# data is recieved in the following format:
		# fix age
		# date
		# time
		# speed
		# course
		# latitude
		# longitude

	def read_wind(self):

	def cra
