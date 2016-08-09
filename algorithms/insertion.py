def Insertion(input_vector):
	print("\t### Insertion Sort ###")

	"Copy the input because everything is a reference in Python"
	sample = list(input_vector);

	"Show received input, without algorithm changes"
	print(sample)

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

		"Show each change"
		print(sample)

	print("\n")
