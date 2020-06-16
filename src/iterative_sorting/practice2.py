num_array = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

def divisible_three(arr):

    for each in arr:
        if each % 3 == 0:
            print(each)

divisible_three(num_array)
