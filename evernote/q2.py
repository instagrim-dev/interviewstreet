# q2

from sys import stdin
from collections import Counter

class q:
	term = None
	count = None

	def __init__(self, t, c):
		self.term = t
		self.count = c

def quickSorta(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i.count > pivot.count:
                less.append(i)
            elif i.count < pivot.count:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSorta(less)
        more = quickSorta(more)
        return less + pivotList + more

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

# descending quicksort
lista = quickSorta(lista)

# lexicographical ascending insertionsort
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