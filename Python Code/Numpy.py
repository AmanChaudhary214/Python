# Declaring numpy or multi dimensional array

from numpy import *

arr = array([[1,2,3], [4,5,6]])   #mentioning the type is not mandatory in numpy. If values are of different types then automatic conversion to higher type will occur.

print(arr.dtype)        #gives data type

print(arr.ndim)         #gives the no of dimension in array

print(arr.shape)        #gives a tuple containing the no of rows and column

print(arr.size)         #give the total no of element

print(arr.flatten())    #converts 2D array into 1D

print(arr.reshape(rows,columns))    #converts a lower dimension array to higher dimension array
print(arr.reshape(n,m,p))           #for converting into 3d array



# Declaring a matrix

mat = matrix('1 2 3; 4 5 6; 7 8 9')     
print(mat)

print(diagonal(mat))        #print list of diagonal elements of matrix
#supports functions like max, min, etc.



# Multiply two matrices.
mat1 = matrix('1 2 3; 4 5 6; 7 8 9')
mat2 = matrix('9 8 7; 6 5 4; 3 2 1')

print(mat1 * mat2)


