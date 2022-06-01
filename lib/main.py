run_app = Pin( 16, Pin.IN, Pin.PULL_UP )
if run_app.value()==0: # Running PicoTel
	import mshell
