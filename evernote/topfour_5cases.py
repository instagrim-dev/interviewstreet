# Evernote Programming Challenge
# Challenges / Frequent Terms
from sys import stdin

N = int(stdin.readline())
lista = [None] * N
for x in xrange(N):
	arg = int(stdin.readline())
	if arg in lista == False:
		break
	lista[x] = arg

for x in xrange(4):
	print max(lista)
	i = lista.index(max(lista))
	lista.pop(i)