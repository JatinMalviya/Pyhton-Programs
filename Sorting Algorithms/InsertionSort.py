import Swap

def InsertionSort(LI):
	
	for loop1 in range(len(LI)):
		i = loop1
		print
		while i > 0 and LI[i] < LI[i-1]:
			Swap.swap(LI,i,i-1)
			i -= 1
			print LI
			
		