#q1
from sys import stdin
from collections import deque

class BOX:
	cache = deque()
	bound = 2

def BOUND(box,n):
	box.bound = n
	if len(box.cache) > n:
		for x in range(len(box.cache) - n):
			box.cache.popleft()

def SET(box,d):
	if d in box.cache:
		box.cache.remove(d)
	if len(box.cache) == box.bound:
		box.cache.popleft()
	box.cache.append(d)

def GET(box,k):
	for x in box.cache:
		if k in x.keys():
			box.cache.remove({k:x.values()[0]})
			box.cache.append({k:x.values()[0]})
			print x.values()[0]
			return
	print "NULL"

def PEEK(box,d):
	for x in box.cache:
		if d in x.keys():
				print x.values()[0]
				return
	print "NULL"

def DUMP(box):	# try .cache.iterkeys() to iterate over the 'keys'
	listt = sorted(list(box.cache))
	for x in range(len(listt)):
		for y,z in dict.items(listt[x]):
			print y, z

N = int(stdin.readline())
box = BOX()

for x in range(N):
	line  = stdin.readline().strip().split(' ', 2) # 1 change
	if 'BOUND' == line[0]:
		BOUND(box, int(line[1]))
	if 'SET' == line[0]:
		SET(box, {str(line[1]):str(line[2])} )
	if 'GET' == line[0]:
		GET(box, str(line[1]))
	if 'PEEK' == line[0]:
		PEEK(box, str(line[1]))
	if 'DUMP' == line[0]:
		DUMP(box)