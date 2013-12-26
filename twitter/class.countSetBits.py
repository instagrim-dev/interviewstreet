def count_set_bits(n):
	count = 0 # count accumulates the total bits set 
	while(n != 0):
		n &= (n-1) # clear the least significant bit set
		count += 1
	return count