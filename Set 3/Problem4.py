# Write a Python function that checks whether a given word or phrase is a palindrome.

string = "madam"

revStr = ""

for i in range(len(string)) :
  revStr = string[i] + revStr

if string == revStr :
  print("palindrome")
else :
  print("not palindrome")
