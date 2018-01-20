import smbus

class I2C:
    """ simulate """
    class Port:
        kOnboard = 0
        kMXP = 1

    def __init__(self, port, address):
        self.port = port
        self.address = address
        self.node = smbus.SMBus(port)

    def readOnly(self, count):
        bytes = self.node.read_i2c_block_data(self.address, 0, count)
        return bytes

    def writeBulk(self, values):
        for b in values:
            self.node.write_byte(self.address, b)