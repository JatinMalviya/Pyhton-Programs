import Swap

def SelectionSort(LI):
	for loop1 in range(len(LI)):
		min = loop1
		for loop2 in range(loop1,len(LI)-1):
			if LI[loop2] < LI[min]:
				min = loop2
		if min <> loop1:
			Swap.swap(LI,min,loop1)
			