# Declaring dynamic array and taking values from user.

from array import *

arr = array('i', [])
n = int(input("Enter the length of array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)



# Ways to declare dynamic array

arr1 = linspace(0, 15, 16)       #linspace(start, stop, parts)

arr2 = arange(1, 15, 2)          #arange(start, stop, step)

arr3 = logspace(1, 40, 5)        #logspace(10**start, 10**stop, parts)

arr4 = zeroes(5, int)           #zeroes(size, type) otherwise bydefault type will be float.

arr5 = ones(5, int)             #ones(size, type) otherwise bydefault type will be float.




# Search an element in array

k = int(input("Enter the value you want to search: "))
print(arr.index(k))



# Add x to each element in array.

x = int(input("Enter the value you want to search: "))

arr = arr + x
print(arr)



# Add two arrays

arr6 = arr1 + arr2
print(arr6)



# Concatenate two arrays

print(concatenate([arr1,arr2]))



# Copy an array

arr7 = arr1.view()          #shallow copy - change in original will be reflected in copied one

arr8 = arr1.copy()          #deep copy - no change is reflected.






 
