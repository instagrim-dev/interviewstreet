from sys import stdin
from collections import deque
import operator	# reduce(operator.mul, list(arr), 1)

N = int(stdin.readline())

arr = deque( int(stdin.readline().rstrip('\r\n')) for x in range(N) )

for x in range(N):
	arr.rotate(-1)
	print reduce(operator.mul, list(arr)[:len(list(arr))-1], 1)