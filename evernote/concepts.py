# q2
# Frequency Counting of Words / Top N words in a document
# Given N terms, your task is to find the k most frequent terms from
# given N terms.
# Python	Python 2.7.3	16 (secs)	256(MB)	.py

from sys import stdin, stdout
from collections import Counter
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')	# sterms.sort(cmp=locale.strcoll)

class q2:

	term=""
	count=0

	def __init__(self, t, k):
		self.term = t
		self.count = k

def lexprint(kcounter, k):
	i = 0
	for word, count in kcounter.most_common(k): #create 'k' number of lists that we'll lexi-sort
		exec 'words%s = []' % i
		exec 'words%s.append("%s")' % (i, word)
		i+=1
	for x in range(k):
		#exec 'print \"words list %%s contents: %%r\" %% (%s,"words"+str(%s))' % (x, x) # this doesn't perform as expected
		exec 'print \"words list %%s contents: %%r\" %% (%s,%s)' % (x, "words"+str(x))	# this performs as expected
		#exec 'print %s' % "words"+str(x)
	# sort
	#for index in 

terms = Counter()
N = int(stdin.readline())	# get N
for x in range(N):	# faster
	arg = stdin.readline().rstrip('\r\n')
	terms[arg] += 1
k = int(stdin.readline().rstrip('\r\n')) # get k
lexprint(terms, k)