from machine import UART
import io, time

class PicoTelUart(io.IOBase):
	def __init__(self, *args, **kwargs ):
		# open UART
		self.u = UART(*args, **kwargs)
		self.ms = 5 # default sleep in ms when printout buffer to terminal

	def read(self, sz=None):
		return self.u.read( sz )

	def readinto(self, buf):
		return self.u.readinto(buf)

	def ioctl(self, op, arg):
		return 0

	def write(self, buf):
		# write buf to terminal
		self.u.write( buf )
		time.sleep_ms( self.ms )
