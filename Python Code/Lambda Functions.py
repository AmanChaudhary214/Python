# Anonymous Function | Lambda Function  -   these are functions without name

f = lambda a,b : a+b

res = f(5,6)
print(res)



# Filter function

nums = [3,2,5,6,6,1,7,5,9,4,8,4,3,9]

evens = list(filter(lambda n :n%2==0 , nums))
print(evens)



# Map function

doubles = list(map(lambda n : n*2, evens))
print(doubles)



# Reduce function

from functools import reduce

sum = reduce(lambda a,b : a+b, doubles)

print(sum)




# Decorators    -   they are used to overwrite existing functions to change their behaviour without changing the original function

def div(a,b):
    print(a/b)

def dec_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner

div = dec_div(div)

div(2,4)
    

