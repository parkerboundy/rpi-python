import smbus
import math
from operator import mul
from itertools import starmap, izip

class IMU: 
	
	# register addresses
	MAG_ADDRESS = (0x3C >> 1)
	ACC_ADDRESS = (0x32 >> 1)
	ACC_ADDRESS_SA0_A_LOW = (0x30 >> 1)
	ACC_ADDRESS_SA0_A_HIGH = (0x32 >> 1)
	LSM303_CTRL_REG1_A = 0x20
	LSM303_CTRL_REG4_A = 0x23
	LSM303_MR_REG_M = 0x02
	LSM303_OUT_X_L_A = 0x28
	LSM303_OUT_X_H_M = 0x03

	# mag calibration
	# note: need to be floats so our mag scaling in heading() works correctly
	MAG_X_MIN = -573.0
	MAG_X_MAX = 573.0
	MAG_Y_MIN = -661.0
 	MAG_Y_MAX = 644.0
	MAG_Z_MIN = -543.0
	MAG_Z_MAX = 581.0

	def __init__(self):
		self.bus = smbus.SMBus(1)
		# note: don't need to pass self directly since it is implicitly passed by python
		self.writeAccReg(self.LSM303_CTRL_REG1_A, 0x27)
		self.writeMagReg(self.LSM303_MR_REG_M, 0x00)

	def writeAccReg(self, register, value):
		self.bus.write_byte_data(self.ACC_ADDRESS, register, value)

	def readAccReg(self, register, length):
		return self.bus.read_i2c_block_data(self.ACC_ADDRESS, register, length)

	def writeMagReg(self, register, value):
		self.bus.write_byte_data(self.MAG_ADDRESS, register, value)

	def readMagReg(self, register, length):
		return self.bus.read_i2c_block_data(self.MAG_ADDRESS, register, length)

	def readAcc(self):
		data = self.readAccReg(self.LSM303_OUT_X_L_A | 0x80, 6)
		return [self.__convert_accel(data, 0), self.__convert_accel(data, 2), self.__convert_accel(data, 4)]

	def readMag(self):
		# note: mag returns values in the wrong order (x, z, y) 
		data = self.readMagReg(self.LSM303_OUT_X_H_M, 6)
		return [self.__convert_mag(data, 0), self.__convert_mag(data, 4), self.__convert_mag(data, 2)]

	def read(self):
		self.readAcc()
		self.readMag()

	def heading(self):
		mag = self.readMag()
		mag[0] = (mag[0] - self.MAG_X_MIN) / (self.MAG_X_MAX - self.MAG_X_MIN) * 2 - 1
		mag[1] = (mag[1] - self.MAG_Y_MIN) / (self.MAG_Y_MAX - self.MAG_Y_MIN) * 2 - 1
		mag[2] = (mag[2] - self.MAG_Z_MIN) / (self.MAG_Z_MAX - self.MAG_Z_MIN) * 2 - 1
		
		a = self.readAcc()
		a = self.__vector_normalize(a)
		f = [0, -1, 0]
		
		e = self.__vector_cross(mag, a)
		e = self.__vector_normalize(e)
		n = self.__vector_cross(a, e)
	
		heading = round(math.atan2(self.__vector_dot(e, f), self.__vector_dot(n, f)) * 180 / math.pi)
		
		if heading < 0:
			 heading += 360
		
		return heading

	def __vector_cross(self, listA, listB):
		data = []
		data.append(listA[1]*listB[2] - listA[2]*listB[1])
		data.append(listA[2]*listB[0] - listA[0]*listB[2])
		data.append(listA[0]*listB[1] - listA[1]*listB[0])
		return data

	def __vector_dot(self, listA, listB):
		return sum(starmap(mul, izip(listA, listB)))

	def __vector_normalize(self, list):
		mag = math.sqrt(self.__vector_dot(list, list))
		data = []
		data.append(list[0] / mag)
		data.append(list[1] / mag)
		data.append(list[2] / mag)
		return data
	
	def __convert_accel(self, list, index):
		n = list[index] | (list[index+1] << 8)
		if n > 32767: n -= 65536
		return n >> 4
	
	def __convert_mag(self, list, index):
		n = (list[index] << 8) | list[index+1]
		return n if n < 32768 else n - 65536
