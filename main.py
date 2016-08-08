import sys
from random import randint

sample_size = 10
sample = []

if len(sys.argv) > 1:
    sample_size = int(sys.argv[1]);

for i in xrange(sample_size):
	sample.append(randint(0,1000))

for number in sample:
	print(number)