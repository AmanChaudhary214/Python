# Write a program to print the following number pattern using a loop.

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

num = input("Enter the number: ")
num = int(num)

for i in range(1,num+1) :
  string = ""
  for j in range(1,i+1) :
    string = string + str(j) + " "
  print(string)
