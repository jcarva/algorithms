import sys
from random import randint
from algorithms.insertion import Insertion

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
Insertion(sample)