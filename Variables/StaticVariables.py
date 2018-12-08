# The variables which are intialized or declared outside constructor and within the class without any self keyword
# are called as static variables or class level variables.

class Student:

    college = 'Sri indu college of engineering and technology'
    def __init__(self,name,age,rollno,dob):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.dob = dob
        
    
    # we can acess class level variables with either a class name or object name.
    
    def getInfo(self):
        print('Name:{}\nAge:{}\nRollNo:{}\nDOB{}\nCollege:{}\n'.format(self.name,self.age,self.rollno,self.dob,Student.college))

    
mani = Student('Manikanta',19,'16D41A05F0','18/05/1999')
vardhan = Student('Sai Vardhan',19,'16D41A05G5','23/03/1999')

mani.getInfo()
vardhan.getInfo()

