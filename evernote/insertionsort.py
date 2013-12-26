# insertion sort

def insertion_sort(list):	# pass a list
	for index in range(1,len(list)):	# step through each slot in list, but dont start at '0' item because this would be inefficient 
		value = list[index]				# current element we're working with
		i = index - 1					# index of element to the left of value
		while i >= 0:
			if value < list[i]:
				list[i+1] = list[i]		# put(i) in the slot to the right(i+1)
				list[i] = value			# shift value left into slot i
				i = i - 1
			else:
				break