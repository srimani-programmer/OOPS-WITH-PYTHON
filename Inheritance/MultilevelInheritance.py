class Add:

    def __init__(self,a,b,c):
        self.value1 = a
        self.value2 = b
        self.value3 = c
    
    def sum(self):
        return self.value1 + self.value2 + self.value3

class Sub(Add):
    
    def sub(self):
        return (self.value3 + self.value1) - self.value2

class Mul(Sub):

    def mul(self):
       return self.value1 * self.value2 * self.value3

m = Mul(10,20,30)

print(m.mul())
print(m.sum())
print(m.sub())


