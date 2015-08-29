import Swap

def BubbleSort(LI):
	swapped = True

	while swapped:	
		for loop1 in range(len(LI)):
			swapped = False
			for loop2 in range(len(LI)-1-loop1):
				if LI[loop2] > LI[loop2+1]:
					Swap.swap(LI,loop2,loop2+1)
					swapped = True
			