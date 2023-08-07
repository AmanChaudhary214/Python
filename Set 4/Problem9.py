# Given an integer, write a function to determine if it is a power of two.
"""
Input: 16
Output: "True"
"""

num = int(input("Enter a number: "))

i = 0
ans = "False"
val = 1

while val < num :
    i += 1
    val = 2**i
    if val == num :
        ans = "True"
        break

print(ans)
    
