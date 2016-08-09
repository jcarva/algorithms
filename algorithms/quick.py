def QuickSort(sample):
	"This QuickSort function just is a interface to maintain the pattern to pass only a sample as argument."

	print("\t### Quick Sort ###")

	"Call the quicksort logic"
	Quick(sample,0,len(sample)-1)

def Quick(sample, init, final):

	"Show received input, without algorithm changes in the first execution and after display each change"
	print(sample)

	"Set left index"
	i = init

	"Set right index"
	j = final

	"Select pivot value"
	pivot = sample[(final + init)/2]

	while (i < j):
		"Search a higher value than the pivot in left side"
		while (sample[i] < pivot):
			i += 1

		"Search a lower value than the pivot in left side"
		while (sample[j] > pivot):
			j -= 1

		"Switch a lower value to a higher value, when we have the as reference"
		if (i <= j):
			aux = sample[i]
			sample[i] = sample[j]
			sample[j] = aux
			i += 1
			j -= 1

	"Call the recursion to left side"
	if (j > init):
		Quick(sample, init, j)

	"Call the recursion to right side"
	if (i < final):
		Quick(sample, i, final)		