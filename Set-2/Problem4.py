# Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

string = input("Enter the string: ")

str1 = ""
str2 = ""

for i in string :
  if i.islower() == True :
    str1 = str1 + i
  else :
    str2 = str2 + i

print(str1+str2)