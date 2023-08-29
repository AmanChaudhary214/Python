# Class and Objects

class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is:", self.cpu, self.ram)


com1 = Computer('i5', 16)           #object1
com2 = Computer('Ryzen5', 32)       #object2

com1.config()
com2.config()




class Student:

    #class variable
    school = "Masai School"
    
    #constructor
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    #instance method
    def avg(self):
        return (self.m1 + self.m2)/2

    #class method
    @classmethod                #decorator
    def getSchool(cls):
        return cls.school

    #static method
    @staticmethod               #decorator
    def info():
        print("Inside static method of Student")


s1 = Student(73,87)
s2 = Student(57,55)

print(s1.avg(), s2.avg())
print(Student.getSchool())
Student.info()
