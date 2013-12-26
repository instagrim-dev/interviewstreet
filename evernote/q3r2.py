#q3
from sys import stdin
from collections import deque
import operator

# get all terms into buffer()
N = int(stdin.readline())
arr = deque()
for x in range(N):
	arg = stdin.readline().rstrip('\r\n')
	arr.append(int(arg))

# do work
#n = None
total = reduce(operator.mul, list(arr), 1)
for x in range(N):
	print total/list(arr)[x]

# you just take the total from the whole list, the divide it 'n' times by i=nth elemnt of the list