#q1
from sys import stdin
from collections import deque

def stdToDeque():
	return deque(stdin.readline().rstrip('\r\n'))

class EVERNOTE:
	buffer = deque()
	size = None
	N = 0

	def __init__(self, N):
		self.size = N

	def A(self):
		# normalize integer from deque(): dequeu->list->str->int
		for x in range(int("".join(str(x) for x in list(arg)))):
			if self.N < self.size:
				self.buffer.append(stdin.readline().rstrip('\r\n'))
				self.N += 1
			else:
				self.buffer.popleft()
				self.buffer.append(stdin.readline().rstrip('\r\n'))
		return stdToDeque()

	def R(self):
		for x in range(int("".join(str(x) for x in list(arg)))):
			self.buffer.popleft()
			self.N -= 1
		return stdToDeque()

	def L(self):
		for x in list(self.buffer):
			print x
		return stdToDeque()

q = EVERNOTE(int(stdin.readline()))
arg = stdToDeque()

while 'Q' not in arg:
	exec 'arg = q.%s()' % arg.popleft()