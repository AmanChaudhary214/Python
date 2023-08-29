# File Handling


# read data from file

f = open('MyData', 'r')
f = open('MyData', 'rb')        # rb - read in binary format (used for images)

print(f.read())
print(f.readline())



# write data into file

f1 = open('MyData', 'w')
f = open('MyData', 'wb')        # wb - write in binary format (used for images)

f1.write("Something")



# append data in file

f2 = open('MyData', 'a')
f2.write("Laptop")



# copy data from one file to another

f3 = open('MyData', 'r')
f4 = open('abc', 'w')

for data in f3:
    f4.write(data)
