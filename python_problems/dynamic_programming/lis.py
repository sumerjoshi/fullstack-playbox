

"""
Pseudocode for LIS
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Pseudocode:
1. Create a temporary array that is size of the input
2. Have two pointers start j at 0, i at 1.
3. i from 1 to n
4. j from 1 to i
    5. if arr[j] < arr[i] and lis[i] < lis[j]+1
    6. lis[i] = lis[j]+1
"""

def lis(nums):
    n = len(nums)
    temp_array = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and temp_array[i] < temp_array[j]+1:
                temp_array[i] = temp_array[j]+1

    maximum = 0
    for i in range(n):
        maximum = max(maximum, temp_array[i])

    return maximum

x = lis([10,9,2,5,3,7,101,18])
print(x)


def faster_lis(nums):
    pass



