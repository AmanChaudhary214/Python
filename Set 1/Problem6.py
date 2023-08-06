# Write a Python program that counts the number of vowels in a given string.

string = "Masai School"

count = 0

for elem in string :
  if elem=='a' or elem=='e' or elem=='i' or elem=='o' or elem=='u' :
    count = count + 1

print(count)
