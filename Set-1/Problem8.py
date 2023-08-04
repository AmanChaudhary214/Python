# Write a Python function that calculates the factorial of a number.

num = input("Enter the number: ")
num = int(num)

fact = 1

for i in range(1, num+1) :
  fact = fact*i

print("Factorial of", num, "is",fact)