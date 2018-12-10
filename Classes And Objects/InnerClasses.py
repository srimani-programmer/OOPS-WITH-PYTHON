# Classes within the classes

class Student:

    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def getStudentInfo(self):
        print('Name:{}\nAge:{}\nRollNo:{}\n'.format(self.name,self.age,self.rollno))
        self.LaptopObject()

    class Laptop:
        def __init__(self,brandname,config,ram):
            self.Brand = brandname
            self.config = config
            self.ram = ram

        def getLaptopInfo(self):
            print('CompanyName:{}\nConfiguration:{}\nRam:{}\n'.format(self.Brand,self.config,self.ram))

        # We can create object for inner class in two ways either in a outer class or 
        # outside of the complete class section.

    def LaptopObject(self):
        self.l1 = self.Laptop('Mac Book Air','i5 - 7th Gen',8)
        self.l2 = self.Laptop('Mac Book Pro','i7 - 8th Gen',16)
        self.l3 = self.Laptop('Asus VivoBook','i7 - 7th Gen',16)

        self.l1.getLaptopInfo()
        self.l2.getLaptopInfo()
        self.l3.getLaptopInfo()

s1 =  Student('Sri Manikanta',18,'16D41A05F0')

print(s1.getStudentInfo())

lappy = Student.Laptop('Mac Book Air','i5 7th Gen',8)

print(lappy.getLaptopInfo())

