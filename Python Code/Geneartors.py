# Geneartors

def topten():

    n = 1
    while n<=10:
        yield n*n
        n += 1

values = topten()

for i in values:
    print(i)
