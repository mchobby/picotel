#
# Display the Charset on terminal
#
import sys

print( 'Display Charset')
for i in range( 128 ): # 0..127
	if i<=32:
		continue
	s = chr(i)
	print( '%3i : %s' % (i,s))
	if i%20==0:
		print( 'press key:')
		c = sys.stdin.read(1)
