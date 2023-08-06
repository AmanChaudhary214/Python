# Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".

string = ""

for i in range(1, 101) :
  if i%3==0 and i%5==0 :
    string = string + "FizzBuzz"
  elif i%3==0 :
    string = string + "Fizz"
  elif i%5==0 :
    string = string + "Buzz"
  else :
    string = string + str(i)

  if i<100 :
    string = string + ", "
    
print(string)
