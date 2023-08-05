# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. Any leftover items will get added at the end of the new list.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list = []

len1 = len(list1)
len2 = len(list2)

count1 = count2 = 0

if len1 > len2 :
  for i in range(len2) :
    temp = list1[i] + list2[i]
    list.append(temp)
    count1 += 1
  for i in range(count1, len1) :
    list.append(list1[i])

else :
  for i in range(len1) :
    temp = list1[i] + list2[i]
    list.append(temp)
    count2 += 1
  for i in range(count2, len2) :
    list.append(list2[i])

print(list)