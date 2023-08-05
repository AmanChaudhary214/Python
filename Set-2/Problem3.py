# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "Ault"
s2 = "Kelly"

s3 = ""
n = len(s1)

for i in range(n) :
  if (i==n/2) :
    s3 = s3 + s2 + s1[i]
  else :
    s3 = s3 + s1[i]
  
print(s3)