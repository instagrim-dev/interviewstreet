#py
from collections import OrderedDict
od = OrderedDict()
od["drink"] = "water"
od["fruit"] = "orange"
od["sport"] = "football"
dd = ("fruit","orange")
#print od
#print od.keys()
#print "length:", len(od)
#print "Length:", od.__len__()
#print od
#print "pop'd",od.pop("drink","water")
#del od[:1]
if "drink" in od:
	print 'drink is here'
if "DRINK" in od:
	print "DRINK is here"
#od.pop("drink")
print od
#if ("drink","water") in od.items():
#	print "hi"
#del od[od.keys()[0]]	# works
#od.popitem()
#od.popitem(1)
#print od
#print "length again:", len(od)