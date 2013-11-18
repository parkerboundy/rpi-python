import smbus
import struct
from datetime import datetime
import logging

bus = smbus.SMBus(1)

class ARDUINO: 

	# register addresses
	ARDUINO_ADDRESS = 0x04
	ARDUINO_GPS_REG = 0x01
	ARDUINO_WIND_REG = 0x02

	def __init__(self):
		self.log = logging.getLogger(__name__)
		self.bus = smbus.SMBus(1)

	def write_register(self, register):
		self.bus.write_byte(self.ARDUINO_ADDRESS, register)

	def read_gps(self):
		# data is recieved in the following format as 4 bytes:
		# [fix age, date, time, speed, course, latitude, longitude]
		data = self.bus.read_i2c_block_data(self.ARDUINO_ADDRESS, self.ARDUINO_GPS_REG, 28)
		temp = []
		for i in range(0,7):
			bytes = data[4*i:4*i+4]

			if i < 6:
				# first six values we recieve are unsigned long
				temp.append(struct.unpack('<L', "".join(map(chr, bytes)))[0])
			else:
				# last two values (latitude and longitude) are long
				temp.append(struct.unpack('<l', "".join(map(chr, bytes)))[0])
		
		# create datetime object, and divide the other numbers to create proper floats
		return [temp[0], self.crack_date(temp[1], temp[2]), temp[3]/100.0, temp[4]/100.0, temp[5]/100000.0, temp[6]/100000.0]

	def read_wind(self):
		print "to-do"

	def crack_date(self, date, time):
		return datetime.strptime("".join([str(date), str(time)]),'%d%m%y%H%M%S%f')
