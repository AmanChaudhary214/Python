# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

10 400
20 300
30 200
40 100
"""

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

n = len(list1)

for i in range(len(list1)) :
  print(list1[i], list2[n-1])
  n -= 1