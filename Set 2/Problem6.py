# Concatenate two lists in the following order
"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

output = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list = []

for i in list1 :
  for j in list2 :
    temp = i + j
    list.append(temp)

print(list)
