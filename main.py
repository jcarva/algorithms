import sys
from random import randint
from algorithms.insertion import InsertionSort
from algorithms.selection import SelectionSort
from algorithms.merge import MergeSort
from algorithms.quick import QuickSort
from algorithms.heap import HeapSort

"Sorting Algorithms ID to call by args on the execution"
sorters={1: SelectionSort, 2: InsertionSort, 3: MergeSort, 4: QuickSort, 5: HeapSort}

"Initialize vector input, array to store the input values"
sample = []

def Input():
	"Sample size"
	size = int(input())

	"Loop to get the input values"
	for i in range(size):
		sample.append(int(input()))

"Check argument to choose a sorting algorithm"
if (len(sys.argv) == 2) and (sorters.has_key(int(sys.argv[1]))):
	"Read input"
	Input()

	"Call Algorithm"
	sorters[int(sys.argv[1])](sample)

	"Output"
	for element in sample:
		print(element)
else:
	print("Please, select a valid sorting algorith!!!")
