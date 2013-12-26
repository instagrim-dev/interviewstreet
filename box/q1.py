#q1 Python	Python 2.7.3	16s	256MB
from sys import stdin
from collections import OrderedDict

class BOX:
	cache = OrderedDict()
	bound = 0

def BOUND(box,n):
	#print "	BOUND",n,box.cache
	box.bound = n
	if len(box.cache) > n:
		for x in range(len(box.cache) - n):
			box.cache.popitem(False)   # (ALT) del box.cache[box.cache.keys()[0]]

def SET(box,k,v):
	#print "	SET",k,v,box.cache
	if k in box.cache:
		del box.cache[k]	# del is faster than pop
	box.cache[k] = v
	if len(box.cache) > box.bound:
		box.cache.popitem(False)

def GET(box,k):
	#print "	GET",k,box.cache
	if k in box.cache:
		v = box.cache[k]
		del box.cache[k]
		box.cache[k] = v
		print box.cache[k]
	else:
		print "NULL"
	
def PEEK(box,k):
	#print "	PEEK",k,box.cache
	if k in box.cache:
		print box.cache[k]
	else:
		print "NULL"

def DUMP(box):	# try .cache.iterkeys() to iterate over the 'keys'
	for k,v in sorted(box.cache.items()):
		print k, v

N = int(stdin.readline())
box = BOX()

for x in range(N):
	line  = stdin.readline().strip('\r\n').split(' ')
	if 'BOUND' in line[0]:
		BOUND(box, int(line[1]))
	if 'SET' in line[0]:
		SET(box, str(line[1]), str(line[2]) )
	if 'GET' in line[0]:
		GET(box, line[1])
	if 'PEEK' in line[0]:
		PEEK(box, line[1])
	if 'DUMP' in line[0]:
		DUMP(box)