x, y, z = 1, 2, 3
print(x,y,z)

# use this assignment to switch variables
x, y = y, x
print(x, y, z)

values = 1, 2, 3
print(values)
x, y, z = values
print(x)

#Value Error: too many values to unpack (expected 2)
#a, b = values
#print(a)

values = 1,2,3,4
print(values)
x,y,*rest = values
print(rest)

name = "Albus Percival Wulfric Brian Dumbledore"
first, *middle, last = name.split()
print(middle)

#the starred variable will always be a list
a, *b, c = "abc"
print(a,b,c)

#Augmented Assignment
x=2
x+=1
x*=2
print(x)

s = 'foo'
s += 'bar'
s *= 2
print(s)