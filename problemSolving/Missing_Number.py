# Given an array containing n distinct numbers taken from 0, 1, 2, ...n, find the one that is missing from the array.
# Example 1
# input: [3, 0, 1]
# output: [2]

def missing_number(nums):
    length = len(nums)
    return (length * (length + 1) / 2 ) - sum(nums)


print(int(missing_number([3, 0, 1])))
