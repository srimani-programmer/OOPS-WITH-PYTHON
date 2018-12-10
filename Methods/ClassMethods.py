# The methods which works with class level variables is called as class methods.

class Student:

    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    college = 'Sri indu'

# class level methods doesn't deal with self keyword.
    @classmethod # This is a decorator
    def getCollege(cls):
        return cls.college

    def getInfo(self):
        print('Name:{}'.format(self.name))
        print('Age:{}'.format(self.age))
        print('RollNo:{}\n'.format(self.rollno))

    
mani  = Student('SriMani',19,'16D41A05F0')

mani.getInfo()
print(Student.getCollege())
