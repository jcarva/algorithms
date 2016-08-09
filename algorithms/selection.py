def SelectionSort(sample):
	print("\t### Selection Sort ###")

	"Show received input, without algorithm changes"
	print(sample)

	for j in xrange(0, len(sample)):

		"Select current key to compare and sort"
		min = j

		"Search index of the lower value"
		for i in xrange(j+1, len(sample)):
			if (sample[min] > sample[i]):
				min = i


		"Put the lower value in its correct position"
		tmp = sample[min]
		sample[min] = sample[j]
		sample[j] = tmp

		"Show each change"
		print(sample)

	print("\n")