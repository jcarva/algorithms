import sys
from random import randint
from algorithms.insertion import InsertionSort
from algorithms.selection import SelectionSort
from algorithms.merge import MergeSort
from algorithms.quick import QuickSort

"Default input size to the sorting algorithms"
sample_size = 10

"Initialize vector input"
sample = []

"Check optional argument to update the input size"
if len(sys.argv) > 1:
    sample_size = int(sys.argv[1]);

"Set input with random numbers"
for i in xrange(sample_size):
	sample.append(randint(0,1000))

"Call Algorithms"
MergeSort(list(sample))
InsertionSort(list(sample))
SelectionSort(list(sample))
QuickSort(list(sample))
