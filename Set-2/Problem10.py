# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

tuple1 = (11, [22, 33], 44, 55)

l1 = list(tuple1)

for elem in l1 :
  if type(elem) is list :
    for i in range(len(elem)) :
      if elem[i]==22 :
        elem[i]=222
  else :
    continue

t1 = tuple(l1)

print(tuple1)