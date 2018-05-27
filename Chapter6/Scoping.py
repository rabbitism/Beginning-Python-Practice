def foo(): x=42
x=1
foo()
print(x)

def output(x):print(x)

x=1
y=2
output(y)

def combine(parameter):
    print(parameter+globals()['parameter'])

parameter = 'berry'
combine('Shrub')

x=1
def change_global():
    global x
    x = x+1

change_global()
print(x)

#Nested
def foo():
    def bar():
        print("Hello, world!")
    bar()
foo()

def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor

double = multiplier(2)
print(double(5))
triple = multiplier(3)
print(triple(20))