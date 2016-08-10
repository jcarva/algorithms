def InsertionSort(sample):

	for j in xrange(1, len(sample)):

		"Select current key to compare and sort"
		picked = sample[j]

		"Index to help us to search the correct position to select key"
		i = j-1

		"Move positions of values higher than selected key"
		while (i >= 0 and picked < sample[i]):
			sample[i+1] = sample[i]
			i -= 1

		"Put the current key in its correct position"
		sample[i+1] = picked
