# Implement the bubble sort algorithm in Python.
"""
Input: [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
"""

list = [64, 34, 25, 12, 22, 11, 90]

n = len(list)
isSwapped = 0

for i in range(n-1) :
    for j in range(n-i-1) :
        if list[j] > list[j+1] :
            isSwapped = 1
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

    if isSwapped == 0 :
        break

print(list)
