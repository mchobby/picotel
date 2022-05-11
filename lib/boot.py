from machine import Pin, UART
import os
run_app = Pin( 16, Pin.IN, Pin.PULL_UP )
p = Pin( 25, Pin.OUT )
if run_app.value()==0: # Running PicoTel
	print( "Running PicoTel")
	# 1200 bauds or 4800 bauds or 9600 bauds
	ser = UART( 0, 9600, bits=7, parity=2, stop=1 ) # Minital compatible UART
	os.dupterm( ser ) # Duplicate terminal over IART
	p.value(1)
	print(" ")
	print("   ")
else:
	print( "PicoTel disabled")
	p.value(0)
