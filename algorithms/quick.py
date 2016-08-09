def QuickSort(sample):
	"This QuickSort function just is a interface to maintain the pattern to pass only a sample as argument."

	print("\t### Quick Sort ###")

	"Call the quicksort logic"
	Quick(sample,0,len(sample)-1)

def Quick(sample, init, final):

	"Show received input, without algorithm changes in the first execution and after display each change"
	print(sample)

	i = init
	j = final
	pivot = sample[(final + init)/2]

	while (i < j):
		while (sample[i] < pivot):
			i += 1

		while (sample[j] > pivot):
			j -= 1

		if (i <= j):
			aux = sample[i]
			sample[i] = sample[j]
			sample[j] = aux
			i += 1
			j -= 1

	if (j > init):
		Quick(sample, init, j)

	if (i < final):
		Quick(sample, i, final)		