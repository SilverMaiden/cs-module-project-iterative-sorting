def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    high = len(arr) - 1
    low = 0
    mid = high - int(high / 2)
    arr.sort()
    print(arr[mid])


    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        low = mid
    elif target < arr[mid]:
        high = mid

    return -1  # not found

