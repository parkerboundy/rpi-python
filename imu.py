import smbus

class IMU: 

	MAG_ADDRESS = (0x3C >> 1)
	ACC_ADDRESS = (0x32 >> 1)
	ACC_ADDRESS_SA0_A_LOW = (0x30 >> 1)
	ACC_ADDRESS_SA0_A_HIGH = (0x32 >> 1)
	LSM303_CTRL_REG1_A = 0x20
	LSM303_CTRL_REG4_A = 0x23
	LSM303_MR_REG_M = 0x02
	LSM303_OUT_X_L_A = 0x28

	def __init__(self):
		self.bus = smbus.SMBus(1)
		# note: don't need to pass self directly since it is implicitly passed by python
		self.writeAccReg(self.LSM303_CTRL_REG1_A, 0x27)
		self.writeMagReg(self.LSM303_MR_REG_M, 0x00)
		print self.readAccReg(self.LSM303_OUT_X_L_A | 0x80, 6) 

	def writeAccReg(self, register, value):
		self.bus.write_byte_data(self.ACC_ADDRESS, register, value)

	def readAccReg(self, register, length):
		return self.bus.read_i2c_block_data(self.ACC_ADDRESS, register, length)

	def writeMagReg(self, register, value):
		self.bus.write_byte_data(self.MAG_ADDRESS, register, value)

	def readMagReg(self, register):
		return 0

	def readAcc(self):
		return 0

	def readMag(self):
		return 0

	def read(self):
		return 0

	def heading(self):
		return 0

	def vector_cross(self):
		return 0

	def vector_dot(self):
		return 0

	def vector_normalize(self):
		return 0
