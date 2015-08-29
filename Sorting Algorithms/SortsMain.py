import os
import BubbleSort
import SelectionSort
import InsertionSort
import QuickSort
import MergeSort

LI = []
terminate = False

os.system('cls')

print "****************************************************************************************"
print "* Sorting Algorithms                                                                   *"
print "****************************************************************************************"

print "\nList Creation"

while not terminate:
	num = raw_input("Enter "+str(len(LI)+1)+"th number for the List (Enter X to stop]): ")
	if num != "X":
		LI.append(int(num))
	else:
		terminate = True
		
print "\nThe Entered List is: ", LI

print "\nPlease Choose any one of the following Sorting Algorithms: \n1.Bubble Sort \n2.Selection Sort \n3.Insertion Sort \n4.Quick Sort \n5.Merge Sort"
choice = int(raw_input(">>"))

if   choice == 1:
	print "\nSorting the List using Bubble Sort..."
	BubbleSort.BubbleSort(LI)
elif choice == 2:
	print "\nSorting the List using Selection Sort..."
	SelectionSort.SelectionSort(LI)
elif choice == 3:
	print "\nSorting the List using Insertion Sort..."
	InsertionSort.InsertionSort(LI)
elif choice == 4:
	print "\nSorting the List using Quick Sort..."
	QuickSort.QuickSort(LI)
elif choice == 5:
	print "\nSorting the List using Merge Sort..."
	MergeSort.MergeSort(LI)
else:
	print "\nSorry Wrong Selection!!!"
	print "BYE!!!"
	exit()
	
print "\nThe Sorted List is : ",LI, "\n"