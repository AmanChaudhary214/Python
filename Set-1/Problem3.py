# Operations in list in python

# Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.

list = [1,2,3,4,5,6,7,8,9,10]

#append() - add single element
list.append(11)
list.append(12)
print(list)

#extend() - add multiple elements
list.extend([13,14,15])
print(list)

#insert() - add element at specific position (index, element)
list.insert(0,0)
print(list)

#remove() - removes an element from the list. 
#first occurrence of the element is removed in the case of multiple occurrences.
list.remove(0)
print(list)

#pop() - remove an element from any position (index)
list.pop(14)
print(list)

#slice() - prints a portion of list
print(list[:5])  # prints from beginning to end index
print(list[2:])  # prints from start index to end of list
print(list[2:8]) # prints from start index to end index
print(list[:])   # prints from beginning to end of list

#reverse() - reverse the elements of a list
print(list[::-1])  # does not modify the original list
# list.reverse()  # modifies the original list

#len() - returns length of a list
print(len(list))

#min() & max() - returns min and max element from a list
print(min(list))
print(max(list))

#count() - returns the number of occurrences of a given element in the list
print(list.count(3))

#sort() - sorts the list of homogeneous elements in ascending order
list.sort()
print(list)

#clear() - erases all the elements from the list
print(list.clear())