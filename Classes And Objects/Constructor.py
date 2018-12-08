# Student Class
class Student:

    # __init__() is act like a constructor for initialization of object.
    def __init__(self,name,age,dob,carrer):
        self.name = name
        self.age = age
        self.DOB = dob
        self.carrerOption = carrer

    def getInfo(self):
        print('Name:{}'.format(self.name))
        print('Age:{}'.format(self.age))
        print('Date Of Birth:{}'.format(self.DOB))
        print('Carrer Option:{}'.format(self.carrerOption))


manikanta = Student('Sri Manikanta',19,'18/05/1999','Computer Science')
aravind = Student('Aravind',19,'18/09/1999','Computer Science')
vardhan = Student('Sai Vardhan',19,'15/03/1999','Computer Science')
arun = Student('Arun Sai Reddy',20,'27/05/1998','Computer Science')


manikanta.getInfo()
arun.getInfo()
vardhan.getInfo()
aravind.getInfo()