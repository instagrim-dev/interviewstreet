# q2
# priority is to sort
from sys import stdin
from collections import Counter

class q:
	term = None
	count = None

	def __init__(self, t, c):
		self.term = t
		self.count = c

# get all terms into Counter()
terms = Counter()
N = int(stdin.readline())
for x in range(N):
	arg = stdin.readline().rstrip('\r\n')
	terms[arg] += 1
k = int(stdin.readline().rstrip('\r\n'))

# put terms in list, as objects
lista = []
for x, y in terms.items():
	lista.append(q(x, y))

# descending insertion sort		#problem
for index in range(1, len(lista)):
	value = lista[index]
	i = index - 1
	while i >= 0:
		if value.count > lista[i].count:
			lista[i+1] = lista[i]
			lista[i] = value
			i = i - 1
		else:
			break

# debug print
#for x in range(k):
#	print "Term: %s, Count: %d" % (lista[x].term, lista[x].count)

# lexicographical insertion sort on lista
for index in range(1, len(lista)):
	value = lista[index]
	i = index - 1
	while i >= 0 and value.count == lista[i].count:
		if cmp(value.term,lista[i].term) == -1:
			lista[i+1] = lista[i]
			lista[i] = value
			i = i - 1
		else:
			break

# output
for x in range(k):
	print lista[x].term