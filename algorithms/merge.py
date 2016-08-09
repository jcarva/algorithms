def MergeSort(sample):
	print("\t### Merge Sort ###")

	"Show received input, without algorithm changes"
	print(sample)

	"Check the sample size and verify if we are in a leaf"
	if (len(sample) > 1):

		"Auxiliary index to divide the problem into 2"
		middle = len(sample) / 2

		"Split the 'problem' into 2"
		left_side = sample[:middle]
		right_side = sample[middle:]

		"Call the recursion to both sides"
		MergeSort(left_side)
		MergeSort(right_side)

		"Merge both sides"
		Merge(sample, left_side, right_side)

	print(sample)


	print("\n")

def Merge(sample, left_side, right_side):

	"Auxiliary index to iterate the left side"
	i = 0

	"Auxiliary index to iterate the right side"
	j = 0

	"Auxiliary index to iterate the entire sample"
	k = 0

	"Compare and merge the both sides into the entire sample"
	while i < len(left_side) and j < len(right_side):
		if (left_side[i] < right_side[j]):
			sample[k]=left_side[i]
			i=i+1
		else:
			sample[k]=right_side[j]
			j=j+1
		k=k+1

	"Store remaining values in left side into the entire sample"
	while i < len(left_side):
		sample[k]=left_side[i]
		i=i+1
		k=k+1

	"Store remaining values in right side into the entire sample"
	while j < len(right_side):
		sample[k]=right_side[j]
		j=j+1
		k=k+1
