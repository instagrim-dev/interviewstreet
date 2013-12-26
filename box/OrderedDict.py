#OrderedDict.py

import collections

print 'Regular dictionary:'
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

print '\nOrderedDict:'
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v
########################
In an OrderedDict you use the setkeys, setvalues, and setitems methods to change the keys, values, and items. You do this by passing in an iterable to the method.

As an example:

>>> d = OrderedDict([(1, 3), (2, 1), (3, 2)])
>>> d.keys()
[1, 2, 3]
>>> newkeys = [3, 2, 1]
>>> d.setkeys(newkeys)
>>> d
OrderedDict([(3, 2), (2, 1), (1, 3)])

########################
>>> d.popitem(i=-1)
Unlike a normal dictionary, the popitem method takes an index as the argument. It pops the item at that position in the dictionary.

The index defaults to -1, the last item in the dictionary.
########################


"del" faster than "pop()" - http://stackoverflow.com/questions/3077145/fastest-way-of-deleting-certain-keys-from-dict-in-python
########################
dict.popitem() is not the same thing as dict.iteritems(); it removes one pair from the dictionary as a tuple, and you are looping over that pair.

The most efficient method is to use a while loop instead; no need to call len(), just test against the dictionary itself, an empty dictionary is considered false:

#########################
how fast is getting the length of a dict. in pythong:
http://www.quora.com/Python-programming-language-1/How-fast-is-getting-the-length-of-a-dictionary-in-Python

#########################
http://copernicus-computing.org/api/html/classcpc_1_1util_1_1ordered__dict_1_1OrderedDict.html#ac02551a2fe853c9c49883aeb54492338