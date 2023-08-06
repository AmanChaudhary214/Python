# Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def div(a,b) :
  try :
    ans = a/b
    return ans
  except ZeroDivisionError :
    return "Cannot divide by zero."

print(div(num1, num2))
