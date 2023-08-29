# Inheritence

# Types  -  single, multiple, multi-level

class A:

    def __init__(self):
        print("init of A")

    def fun1(self):
        print("Fun1")

    def fun2(self):
        print("Fun2")


class B(A):

    def __init__(self):
        super().__init__()
        print("init of B")

    def fun3(self):
        print("Fun1")

    def fun4(self):
        print("Fun2")


class C:

    def __init__(self):
        print("init of C")


class D(A,C):

    def __init__(self):
        super().__init__()      #here it will follow MRO i.e., call the method of left parent class
        print("init of D")

    def fun6(self):
        print("Fun5")


a1 = A()
a1.fun1()
a1.fun2()

b1 = B()
b1.fun1()
b1.fun4()

d1 = D()


# if we create object of sub class it will first try to find the init of sub class
# if not found then it will call init of super class
# super() is used to call init method of super class explicitly
