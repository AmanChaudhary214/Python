# Write a Python function that checks whether a given number is a prime number.

num = input("Enter the number: ")
num = int(num)

count = 0

for i in range(2,num+1):
  if num%i == 0 :
    count = count+1

if count==1 :
  print("prime")
else :
  print("not prime")
