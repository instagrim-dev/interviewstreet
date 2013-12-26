# box2.py

import sys

class Box(object):
	def __init__(self, LIST):
		self.sortedDimensions = LIST
		self.sortedDimensions = sorted(self.sortedDimensions)
		self.w = int(self.sortedDimensions[0])
		self.l = int(self.sortedDimensions[1])
		self.h = int(self.sortedDimensions[2])
		self.weight = self.l * self.w

# tmp argument list from STDIN; Number of boxes and their dimensions
arg1 = []

for line in sys.stdin:
	arg1.append(line)
#print "DEBUG print `arg1`: %r" % arg1

arg1 = map(lambda each:each.strip('\n'), arg1)

#print "DEBUG print `arg1`: %r" % arg1

# number of boxes parsed from arg1
N = arg1.pop(0)

if N.isdigit() != True:
	#print "The first argument is not an integer, no further processing can be done; exiting"
	exit(1)
else:	# its safe to convert to assume N is a number and conv to an int
	N = int(N)

if (N<=20) != True:
	#print "\"N\" \(%d\) is too larg (>20); exiting" % N
	exit(2)

if len(arg1) != (N):
	#print "DEBUG \"number of lines of arguments: \" %d" % len(arg1)
	#print "First #_of_arguments_check: Not enough arguments given; exiting"
	exit(3)

# tmp argument list from arg1; box dimeninsions
arg2 = []

for arg in arg1:
	arg = arg.split(' ')
	#print "DEBUG list \"arg\" is: %r" % arg
	for iarg in arg:
		#print "DEBUG value of \"iarg\" is: %r" % iarg
		if iarg.isdigit():
			dimension = int(iarg)
			if (1<=dimension and dimension<=100) != True:
				#print "Constraint: For any box, 1<=length,width,height<=100; exiting"
				exit(4)
			else:
				arg2.append(dimension)
		else:
			#print "ERROR incompatible dimension value; exiting"
			exit(4)

if len(arg2) != N*3:
	#print "ERROR Too few box dimensions captured; exiting"
	exit(5)
else:
	N2 = int(N*3)	# the number of dimensions
del arg1

# box dimensions matrix: [[0, 0, 0]]
dimensions = [[0 for x in range(3)] for x in range(N)]

for j in range(N):
	for k in range(3):
		dimensions[j][k] = arg2.pop(0)
del arg2
#DEBUG dimensions input list: [[5, 2, 4], [1, 4, 2], [4, 4, 2]]

# dynamic box creation from dimensions list
for i in dimensions:
	exec 'box%s = Box(%s)' % (dimensions.index(i)+1, i)	# works

# proper sorted list
goodsort = []
for i in range(N):
	exec 'goodsort.append(box%s)' % int(i+1) 
# bubble sort the list of Box objects based on l & w
issorted = False
while not issorted:
	issorted = True
	for i in range(N-1):
		print "Comparing length %r to length %r and width %r to width %r" % (goodsort[i].l, goodsort[i+1].l, goodsort[i].w, goodsort[i+1].w)
		if goodsort[i].l > goodsort[i+1].l and goodsort[i].w > goodsort[i+1].w:
			issorted = False
			goodsort[i+1], goodsort[i] = goodsort[i], goodsort[i+1]
print "box order from goodsort, top to bottom (smallest to largest):"
for i in range(N):
	exec 'print \"box%s \"' % (i+1)

# compute max height
mheight = 0

for box in goodsort:
	#exec 'mheight+= %s.h' % (box)
	mheight += box.h
	#exec 'print \"\tIts Dimensions are: l:%%r w:%%r h:%%r\" %% (%s.l, %s.w, %s.h)' % (box,box,box)
	print "The dimensions are: %r %r %r" % (box.l, box.w, box.h)
print "%d" % mheight

# sort weights of boxes into a list
#tower = {}
#
#for i in range(N):
#	exec 'tower[\'box%s\'] = box%s.weight' % (str(i+1),str(i+1))
#
#print "DEBUG The order is (bottom to top):"
#for x in tower:
#	print "The tower is: %r" % x

# compute max height
#mheight = 0;
#
#for box, weight in tower.items():
#	exec 'mheight+= %s.h' % (box)
#	print "The box is %r the weight is %r." % (box, weight)
#	exec 'print \"\tIts Dimensions are: l:%%r w:%%r h:%%r\" %% (%s.l, %s.w, %s.h)' % (box,box,box)
#print "%d" % mheight
