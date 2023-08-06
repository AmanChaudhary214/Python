# Write a Python program that calculates and prints the sum and average of a list of numbers.

list = [10, 20, 30, 40]

sum = 0
avergae = 0

for elem in list :
  sum = sum + elem

average = sum/len(list)

print("Sum:",sum, "Average:",average)
