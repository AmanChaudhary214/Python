# Implement the selection sort algorithm in Python.

"""
Input: [64, 25, 12, 22, 11]
Output: "[11, 12, 22, 25, 64]
"""

arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
  min_index = i
  for j in range(i + 1, len(arr)):
    if arr[j] < arr[min_index]:
      min_index = j

  temp = arr[i]
  arr[i] = arr[min_index]
  arr[min_index] = temp

print(arr)
