# q2
# priority is to sort

from sys import stdin
from collections import Counter
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')	# sterms.sort(cmp=locale.strcoll)

def lexprint(kcounter, k):
	listg = []
	print "Terms we are working with: ", kcounter.most_common(k)
	#i = 0
	for word, count in kcounter.most_common(k):
		try:
			exec 'words%s' % str(count)
		except NameError:
			exec 'words%s = []' % str(count)
			listg.append(count)
		else:
			continue
	#print "listg sizes: ", listg
		#didnt work#exec 'if words%s in locals() == False: words%s = []' % (str(count), str(count))
		#exec 'words%s = []' % str(count)
	for word, count in kcounter.most_common(k): #create 'k' number of lists that we'll lexi-sort
		#print "The word: %s, the count: %d" % (word, count)
		exec 'words%s.append("%s")' % (count, word)
		#i+=1
	#exec 'print \"printing...:\", words%s' % count
	for x in listg:	# sort here
		#exec 'sorted(words%s, lambda x,y: cmp(x.lower(), y.lower()) or cmp(x,y))' % str(x)
		exec 'words%s.sort(cmp=locale.strcoll)' % str(x)
		# can't sort these things 
	sorted(listg, reverse=True)
	for x in listg:
		exec 'for y in words%s: print y' % str(x)
		#exec 'if x == len(words%s): for y in words%s: print y' % (str(x),str(x))
		#exec 'print words%s' % str(x)


terms = Counter()
N = int(stdin.readline())	# get N
for x in range(N):	# faster
	arg = stdin.readline().rstrip('\r\n')
	terms[arg] += 1
k = int(stdin.readline().rstrip('\r\n')) # get k
print "All the terms: ", terms.items()
lexprint(terms, k)