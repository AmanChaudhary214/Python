# Use list comprehension to create a list of the squares of the numbers from 1 to 10.

list = [1,2,3,4,5,6,7,8,9,10]

squares = []

for i in list :
  temp = i*i
  squares.append(temp)

print(squares)
