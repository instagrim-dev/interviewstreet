#q1
from sys import stdin
from collections import deque

class BOX:
	cache = deque()
	bound = 0

def BOUND(box,n):
	box.bound = n
	if len(box.cache) > n:
		for x in range(len(box.cache) - n):
			box.cache.popleft()

def SET(box,d):
	if d in box.cache:
		box.cache.remove(d)
	box.cache.append(d)
	if len(box.cache) > box.bound:
		box.cache.popleft()

def GET(box,d):
	for x in box.cache:
		for y, z in dict.items(x):
			if y == d:
				print z
				box.cache.remove({d:z})
				box.cache.append({d:z})
				return
	print "NULL"

def PEEK(box,d):
	for x in box.cache:
		for y, z in dict.items(x):
			if y == d:
				print z
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
	line  = stdin.readline().strip('\r\n').split(' ')
	if 'BOUND' in line:
		BOUND(box, int(line[1]))
	if 'SET' in line:
		SET(box, {line[1]:line[2]} )
	if 'GET' in line:
		GET(box, line[1])
	if 'PEEK' in line:
		PEEK(box, line[1])
	if 'DUMP' in line:
		DUMP(box)