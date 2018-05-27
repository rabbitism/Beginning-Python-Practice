def hello(name):
    return 'Hello, ' + name + '!'

print(hello('Tiny'))

def fibs(num):
    'Get the fibs'
    result = [0,1]
    for i in range(0, num-2):
        result.append(result[-2]+result[-1])
    return result

#print(fibs(int(input('How many fib numbers do you want? '))))
#print(fibs.__doc__)

def hello_3(greeting = 'Hello', name='world'):
    print('{}, {}!'.format(greeting, name))

hello_3()
hello_3(greeting="Whasup", name="Bunny!")

#Parameters collection
def printparams(*params):
    print(params)

printparams('Testing', 'Testing2')
def print_params_2(title, *params):
    print(title)
    print(params)

print_params_2('Hello', 1,2,3,4,5)
print_params_2('Hello')

def in_the_middle(x,*y,z):
    print(x,y,z)

#parameters after params collection must be defined. 
in_the_middle(1,2,3,4,5,6, z=7)

def print_params_3(**params):
    print(params)

print_params_3(x=1,y=2,z=3)

def print_params_4(x,y,z=3,*pospar, **keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)

print_params_4(1,2,3,5,6,7,foo=1,bar=2)
print_params_4(1,2)

params = {'name':'Sir Robin', 'greeting':'Well met'}
hello_3(**params)
