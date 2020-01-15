# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        if smallest_index != cur_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # define the length of array
    # cannot perform a comparison on the last item of the list because there is nothing after it
    indexing_length = len(arr) - 1
    # set sorted to False
    sorted = False

    # loop through while not sorted
    while not sorted:
        # will end the loop
        sorted = True

        # loop through the array and make the comparison
        for i in range(0, indexing_length):
            # if the item is bigger than the one to its right, set sorted to False and swap them
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    # return the array
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    counts = {}
    for n in arr:
        if n < maximum:
            return "Error, negative numbers not allowed in Count Sort"
        if n not in counts:
            counts[n] = 0
        counts[n] += 1

    sorted_ = []
    for n, count in sorted(counts.items()):
        for i in range(count):
            sorted_.append(n)
    return sorted_
