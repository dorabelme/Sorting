import random

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    a = 0
    b = 0

    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    middle = int(len(arr) / 2)
    if len(arr) > 1:
        left = merge_sort(arr[0:middle])
        right = merge_sort(arr[middle:])
        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    left = arr[start:mid]
    right = arr[mid:end]
    i = 0
    j = 0
    k = start

    for l in range(k, end):
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            arr[l] = left[i]
            i = i + 1
        else:
            arr[l] = right[j]
            j = j + 1

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if r - l > 1:
        mid = int((l + r) / 2)
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid, r)
        merge_in_place(arr, l, mid, r)

    return arr


arr1 = [0, 1, 2, 3, 4, 5, 6, 8, 9, 7]
print(merge_sort_in_place(arr1, 0, len(arr1)))


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt

def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]


def insertion_sort(arr):
    if len(arr) == 0:
        return -1

    for i in range(1, len(arr)):
        # print(arr[i])
        index = i
        while index > 0 and arr[index - 1] > arr[index]:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr


def timsort(arr, run=32):
    for x in range(0, len(arr), run):
        arr[x: x + run] = insertion_sort(arr[x: x + run])

    run_inc = run
    while run_inc < len(arr):
        for x in range(0, len(arr), 2 * run_inc):
            arr[x: x + 2 * run_inc] = merge(arr[x: x + run_inc],
                                            arr[x + run_inc: x + 2 * run_inc])
        run_inc = run_inc * 2
    return arr


tim_sort_arr = create_array(100, 99)
print(f'tim sort before: {tim_sort_arr}')
tim_sorted = timsort(tim_sort_arr)
print(f'tim sort after: {tim_sorted}')
