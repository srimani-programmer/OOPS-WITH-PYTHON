# Simple blue print of a class
class Student:

    # Defining a method about my details.
    def details(self):
        print('Name: Sri Manikanta')
        print('Age:',19)
        print('DOB: 18/05/1999')
        print('Carrer Option: B.TECH')

manikanta = Student()

# Determinig the object type.
print('Type of the class object is:',type(manikanta))

# Accessing the class methods with objects

manikanta.details()

# we can also access methods of a class with an another way also.

Student.details(manikanta) 

    
