#q2.py
from sys import stdin
from collections import deque

tower = deque()

N = int(stdin.readline())
rotations_needed = 3 ** N - 1

if N == 0:
	theight = 0
elif N == 1:
	line  = stdin.readline().strip('\r\n').split(' ')
	theight = max(int(line.pop(0)), int(line.pop(0)), int(line.pop(0)))
else:
	for x in range(N):
		tower.append(deque(stdin.readline().strip('\r\n').split(' ')))
		print "the tower now contains:", tower[x]
	hlist = []
	for x in xrange(N):
		print "	box %d on bottom" % int(x+1)
		i=0
		j=1
		for y in xrange(N):	
			for z in xrange(6):
				heighttemp = int(tower[0][2])
				widthtemp = int(tower[0][1])
				lengthtemp = int(tower[0][0])
				hlist.append(heighttemp)
				print "lengthtemp: %d, tower[j].l: %d, widthtemp: %d, tower[j].w: %d" % (lengthtemp, int(tower[j][0]), widthtemp, int(tower[j][1]))
				while lengthtemp <= int(tower[j][0]) and widthtemp <= int(tower[j][1]):
					lengthtemp = int(tower[j][0])
					widthtemp = int(tower[j][1])
					heighttemp += int(tower[j][2])
					print "	height increased to", heighttemp
					hlist.append(heighttemp)
					if j+1 > N-1:
						j = 1
						break
					else:
						j+=1
				tower[j].rotate()
			tower[y].rotate()
		tower.rotate()
	theight = max(hlist)	# finally get greatest computed height for N >= 2 boxea
print theight