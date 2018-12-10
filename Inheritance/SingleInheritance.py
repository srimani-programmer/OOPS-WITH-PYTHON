# child class can inherit properties from parent class is called as single level inheritance.

class Parent:

    def fatherProperty(self):
        print('50Cr')
        print('5000 Hectares of land')
        print('12 Duplex')

class Child(Parent):
    def myProperty(self):
        print('50Lakhs')
        print('250 Hectares of land')
        print('1 Bunglow')
        print('Mercedes-Benz')


child1 = Child()
print('My Property:')
child1.myProperty()
print('\nMy Father Property:')
child1.fatherProperty()

parent1 = Parent()
print('\nMy Family property:')
parent1.fatherProperty()