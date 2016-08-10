def HeapSort(sample):
    print("\t### Heap Sort ###")

    "Show received input, without algorithm changes"
    print(sample)

    final = len(sample)

    init = (final / 2) - 1

    for i in range(init, -1, -1):   
        Heapify(sample, final, i)

    for i in range(final-1, 0, -1): 
        Switch(sample, i, 0)   
        Heapify(sample, i, 0)


def Heapify(sample, final, i):

    left = 2 * i + 1

    right = 2 * (i + 1)

    max = i

    if left < final and sample[i] < sample[left]:   
        max = left

    if right < final and sample[max] < sample[right]:   
        max = right

    if max != i:   
        Switch(sample, i, max)   
        Heapify(sample, final, max)

    "Show each change"
    print(sample)

def Switch(sample, i, j):
    aux = sample[i]
    sample[i] = sample[j]
    sample[j] = aux