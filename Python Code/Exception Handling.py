# Exception Handling

# Errors  -  Logical Error, Compile Time Error, Runtime Error


a = 5
b = 2

try:
    print("resource opened")
    print(a/b)
    
except ZeroDivisionError as e:
    print("Can't divide a number by zero -", e)
except ValueError as e:
    print("Invalis Input -", e)
except Exception as e:
    print("Something went wrong -", e)
    
finally:
    print("resource closed")
    

print("Bye")
