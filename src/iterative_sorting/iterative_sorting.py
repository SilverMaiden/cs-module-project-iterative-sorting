from binary_search_tree import BSTNode
# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        while cur_index <= len(arr) - 1:
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index
            cur_index += 1
        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index]= arr[smallest_index], arr[i]
    return arr

num_array = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
print(selection_sort(num_array))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    for i in range(0, len(arr) - 2):
        cur_index = i
        next_index = i+1
        while cur_index < len(arr) - 1:
            if arr[cur_index] > arr[next_index]:
                arr[next_index], arr[cur_index] = arr[cur_index], arr[next_index]
            cur_index += 1

    print(arr)
    return arr

bubble_sort(num_array)

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
