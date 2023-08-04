# Write a Python function that generates the first n numbers in the Fibonacci sequence.

num = input("Enter the number: ")
num = int(num)

list = [0,1]

for i in range(2,num) :
  temp = list[i-1] + list[i-2]
  list.append(temp)

print(list)