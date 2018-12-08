# The variables which are intialized or declared inside constructor are called as instancevariables.

class Student:

    def __init__(self,name,age,rollno,dob):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.dob = dob
    
    def getInfo(self):
        print('Name:{}\nAge:{}\nRollNo:{}\nDOB{}\n'.format(self.name,self.age,self.rollno,self.dob))

    
mani = Student('Manikanta',19,'16D41A05F0','18/05/1999')
vardhan = Student('Sai Vardhan',19,'16D41A05G5','23/03/1999')

mani.getInfo()
vardhan.getInfo()