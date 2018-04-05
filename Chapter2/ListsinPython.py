print("Hello")
print(list('Hello'))

#Changing List: Item Assignements
x=[1,1,1]
print(x)
x[1]=2
print(x)

#Deleting Elements
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
print(names)
print("Length: "+str(len(names)))
del names[2]
print(names)
print("Length: "+str(len(names)))

#Assigning to Slices
name = list('Perl')
print(name)
name[2:] = list('ar')
print(name)

name[1:] = list('ython')
print(name)

#Use slice assignment to insert and delete elements
numbers=[1,5]
numbers[1:1]=[2,3,4]
print(numbers)
numbers[1:4]=[]
print(numbers)

