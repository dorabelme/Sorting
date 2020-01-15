# STRETCH: implement Linear Search
def linear_search(arr, target):
    # loop through the array
    for i in range(len(arr)):
        # if the item equals the target, return the index
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    while low <= high:
        middle_point = low + (high - low) // 2
        midpoint_value = arr[middle_point]

        if midpoint_value == target:
            return middle_point
        elif target < midpoint_value:
            high = middle_point - 1
        else:
            low = middle_point + 1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if low > high:
        return - 1
    else:
        middle = (low + high) // 2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            return binary_search_recursive(arr, target, low, middle - 1)
        else:
            return binary_search_recursive(arr, target, middle + 1, high)


data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 25
print(linear_search(data, target))
print(binary_search(data, target))
print(binary_search_recursive(data, target, 0, len(data)))
