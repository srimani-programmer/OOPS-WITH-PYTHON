class Student:
    def __init__(self,name,age,dob):
        self.name = name
        self.age = age
        self.dob = dob
    
    def getInfo(self):
        print('Name:{}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('DOB: {}'.format(self.dob))
        
mani = Student('Sri Manikanta',19,'21/10/1999')
mani.dob = '18/05/1999'

vardhan = Student('Sai Vardhan',21,'06/03/1997')
vardhan.age = 19
vardhan.dob = '06/03/1999'

mani.getInfo()
vardhan.getInfo()


