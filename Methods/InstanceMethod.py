# The method which deal with instance variables is called as instance methods.

class Student:

    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
    
    # This is an instance method.
    def getInfo(self):
        print('Name:{}'.format(self.name))
        print('Age:{}'.format(self.age))
        print('RollNo:{}\n'.format(self.rollno))

mani = Student('Sri Manikanta',19,'16D41A05F0')
vardhan = Student('Sai Vardhan',19,'!6D41A05G5')

mani.getInfo()
vardhan.getInfo()