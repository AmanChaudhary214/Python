# Functions in Python

def greet():
    print("Hello")
    print("Good Morning")

greet()



def add_sub(a,b):       #a and b are arguments
    c = a+b
    d = a-b
    return c,d

result1,result2 = add_sub(4,3)     #2 and 3 are parameters

print(result1, result2)
