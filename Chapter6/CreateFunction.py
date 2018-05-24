def hello(name):
    return 'Hello, ' + name + '!'

print(hello('Tiny'))

def fibs(num):
    'Get the fibs'
    result = [0,1]
    for i in range(0, num-2):
        result.append(result[-2]+result[-1])
    return result

print(fibs(int(input('How many fib numbers do you want? '))))
print(fibs.__doc__)

def hello_3(greeting = 'Hello', name='world'):
    print('{}, {}!'.format(greeting, name))

hello_3()
hello_3(greeting="Whasup", name="Bunny!")