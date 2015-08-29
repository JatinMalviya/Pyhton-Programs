import Swap

def QuickSort(LI):
	quicksort(LI,0,len(LI)-1)
	
def quicksort(LI,lo,hi):
	if hi > lo :
		part = partition(LI,lo,hi)
		quicksort(LI,0,part-1)
		quicksort(LI,part+1,hi)
	
def partition(LI,lo,hi):
	j = lo
	for i in range(lo,hi):
		if LI[i] < LI[hi]:
			Swap.swap(LI,i,j)
			j += 1
	Swap.swap(LI,j,hi)
	print "\n",LI[lo:hi]
	return j
	