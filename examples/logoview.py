import sys
import time


empty = 0
with open( 'logos.txt' ) as file:
	s = file.readline()
	while s.find(':EOF:') < 0:
		s = s.replace('\r','').replace('\n','')
		if (s == None) or (len(s)==0):
			empty += 1
			if empty >= 3:
				print( "Pause" )
				print( 'Press a key to continue:' )
				char = sys.stdin.read(1)

				empty = 0
			else:
				print( " ")
		else:
			empty = 0
			print( s )
		s = file.readline()
