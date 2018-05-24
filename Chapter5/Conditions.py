#values considered as "false"
#False, None, 0, "", (), [], {}
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool('I think, therefore I am'))
print(bool(42))

#Conditional Execution and the if statement
name = input('What is your name? ')
if name.endswith('Gumby'):
    print('Hello, Mr. Gumby')

#else Clauses
name = input('What is your name? ')
if name.endswith('Gumby'):
    print('Hello, Mr. Gumby')
else:
    print('Hello stranger')

status = "friend" if name.endswith("Gumby") else "stranger"
print(status)

#elif Clauses
num = int(input('Enter a number: '))
if num>0:
    print('The number is positive')
elif num<0:
    print('The number is negative')
else:
    print('The number is zero')

#is and ==, is: is test identity, == test equality
x=y=[1,2,3]
z=[1,2,3]
print('Is: The Identity Operator')
print(x==y)
print(x==z)
print(x is y)
print(x is z)

x=[1,2,3]
y=[2,4]
print(x is not y)
del x[2]
y[1]=1
y.reverse()

print(x==y)
print(x is y)

#in: the membership operator
print('in: The Membership Operator')
if 's' in name:
    print('Your name contains the letter "s".')
else:
    print('Your name does not contain the letter "s".')

#Assertions
age = 10
#assert 0<age<100
age = -1
#assert 0<age<100, 'The age must be realistic'



#following parts will be moved to loop file

#Parallel iteration
names = ['anne', 'beth', 'george', 'damon']
ages = [12,45,32,102]
print(zip(names, ages)) #print the location of this zip in memory
print(list(zip(names, ages)))
for name,age in zip(names, ages):
    print(name, 'is', age, 'years old')

#zip will stop when the shortest sequence is used up
print(list(zip(range(5),range(1999))))

#numbered iteration
strings = ['a', 'b', 'c', 'd']
index = 0
for string in strings:
    if 'a' in string:
        strings[index] = '[censored]'
    index+=1

print(strings)

#use built-in enumerate function
for index, string in enumerate(strings):
    if 'c' in string:
        strings[index] = '[censored]'

print(strings)

#revsered and sorted iteration
print(sorted('Hello, world!'))
print(''.join(reversed('Hello, world!')))