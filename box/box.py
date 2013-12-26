# create a dictionary for the Boxes
#Boxes = {}

#j = 1
#for i in dimensions:
#	str = "Box" + `j`
#	Boxes[str] = i
#	j+=1
#print "DEBUG The Box dictionary: %r" % Boxes
#del j

# print permutaitaions set of the dictionary keys
#print "Present order of Boxes: %r" % Boxes
#print "permutations of `Boxes`:"
#print set(itertools.permutations(Boxes))

# then print a permutation of the 
# permutations list (the outer list; box arrangements)
	

#Box_permutations_listlist = 

# display the permutations for each box
#for i in range(N):
#	print "DEBUG print permutations of Box %d:" % (int(i)+1)
#	for x in permute(dimensions[i]):
#	    print x

# create box dictionaries, append permutations
#for i in range(N):
#	exec 'Box%s = {}' % str(i+1)
#	statement = 'Box%s' % str(i+1)
#	print "the Box name is: %r " % statement

#ABANDONED
#from numpy import *
#	print "DEBUG print the permutation set: %r" % set(itertools.permutations(j))		# set is a class, an unordered collection with no duplicate elements.  
# numpy probably wont work on interviewstreet
#dimensions = numpy.zeros(N2).reshape((1,3))

# permutation function
def permute(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for n in range(0,length):
             for end in permute( LIST[:n] + LIST[n+1:] ):
                 yield [ LIST[n] ] + end