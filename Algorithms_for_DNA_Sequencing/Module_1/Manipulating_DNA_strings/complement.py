
def reverseComplement(s):
	complement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
	t = ''
	for base in s:
		t = complement[base] + t #add up the reverse complement string and print out from the buttom of the string
	return t
