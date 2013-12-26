# q2
# Frequency Counting of Words / Top N words in a document
# Given N terms, your task is to find the k most frequent terms from
# given N terms.

import sys
import collections

N = int(sys.stdin.readline()) # First line of input, 'N' terms
#print 'Number of terms: %d' % N
if (0 < N) != True or (N < 300000) != True:	# CONSTRAINT 1
	exit(1)
input = {}
coconut = int(0)
k = 0

for line in sys.stdin:
	if line.rstrip('\r\n').isdigit():
		k += int(line)
		continue
	arg = line.rstrip('\r\n')
	if (0 < len(arg)) != True or (len(arg) < 25) != True:
		exit(2)
	if input.has_key(arg) != True:
		input[arg] = coconut
	else:
		for x,y in input.items():
			if arg == x:
				input[arg] += 1

#print 'Dictionay %r' % input
#print 'k terms %d' % k
kiwi = collections.OrderedDict(sorted(input.items(), key=lambda t: t[1]))
terms = kiwi.items()
terms.reverse()
for x in range(k):
	print '%s' % collections.OrderedDict(terms).keys()[x]