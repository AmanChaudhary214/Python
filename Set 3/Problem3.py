# Given an array of integers and a target integer, find the two integers in the array that sum to the target.
"""
Input: [2, 7, 11, 15], target = 9
Output: "[0, 1]"
"""

list = [2, 7, 11, 15]
target = 9

output = []

for i in range(0, len(list)) :
  for j in range(i+1, len(list)) :
    if list[i]+ list[j] == target :
      output.append(i)
      output.append(j)

print(output)
