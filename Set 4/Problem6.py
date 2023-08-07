# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one that is missing from the array.
"""
Input: [3, 0, 1]
Output: "2"
"""

list =  [3, 0, 1]


def missing_number(list):
    n = len(list)
    total_sum = (n * (n + 1)) / 2
    array_sum = sum(list)
    return total_sum - array_sum


result = missing_number(list)
print(result) 
