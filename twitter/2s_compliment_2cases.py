# twitter.interviewstreet
# 2's compliment, 32 bits
# binary: http://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
# 2's: http://stackoverflow.com/questions/1049722/what-is-2s-complement/3701121#3701121
from sys import stdin

def hammingweight(a,b):
	count = 0
	for z in xrange(a,b+1):
		if z == -1:
			count += 32
		elif z < 0:
			z += 1
			count += 32 - bin(z).count('1')
		elif z > 0:
			count += bin(z).count('1')
	return count

N = int(stdin.readline())

for x in xrange(N):
	line = stdin.readline().split()
	print hammingweight(int(line[0]),int(line[1]))