import sys
from random import randint
from algorithms.insertion import InsertionSort
from algorithms.selection import SelectionSort
from algorithms.merge import MergeSort
from algorithms.quick import QuickSort
from algorithms.heap import HeapSort

"Sorting Algorithms ID to call by args on the execution"
sorters={1: SelectionSort, 2: InsertionSort, 3: MergeSort, 4: QuickSort, 5: HeapSort}

"Default input size to the sorting algorithms"
sample_size = 10

"Initialize vector input"
sample = []

"Set input with random numbers"
for i in xrange(sample_size):
	sample.append(randint(0,1000))

"Check argument to choose a sorting algorithm"
if (len(sys.argv) == 2) and (sorters.has_key(int(sys.argv[1]))):
	"Call Algorithm"
	sorters[int(sys.argv[1])](sample)

	"Set input with random numbers"
	for index in sample:
		print(index)
else:
	print("Please, select a valid sorting algorith!!!")
