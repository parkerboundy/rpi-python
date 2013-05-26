import smbus

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
		data = self.readMagReg(self.LSM303_OUT_X_H_M, 6)
		return [self.__convert_mag(data, 0), self.__convert_mag(data, 2), self.__convert_mag(data, 4)]

	def read(self):
		self.readAcc()
		self.readMag()

	def heading(self):
		return 0

	def vector_cross(self):
		return 0

	def vector_dot(self):
		return 0

	def vector_normalize(self):
		return 0
	
	def __convert_accel(self, list, index):
		n = list[index] | (list[index+1] << 8)
		if n > 32767: n -= 65536
		return n >> 4
	
	def __convert_mag(self, list, index):
		n = (list[index] << 8) | list[index+1]
		return n if n < 32768 else n - 65536
