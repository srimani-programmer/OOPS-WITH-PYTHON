# The methods which are used to perform specific operation in an application 
# without using class or instance variables is called as static methods.

class Factorial:

    @staticmethod
    def fact(n):
        result = 1
        for i in range(n):
            result = result * n
            n = n - 1
        return result

f = Factorial()
value = int(input('Enter a value to find factorial:'))

print('The factorial value for {} is {}'.format(value,f.fact(value)))







