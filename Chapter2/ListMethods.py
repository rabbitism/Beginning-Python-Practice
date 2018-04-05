
#List Methods
##append
list_a = [1,2,3]
list_a.append(4)
print(list_a)

#clear
list_a = [1,2,3]
list_a.clear()
print(list_a)

#copy
##a normal assignment simply binds another name to the same variable, so copy is a separate list
a = [1,2,3]
b=a
print("a: ")
print(a)
b[1]=4
print("a: ")
print(a)

a=[1,2,3]
b=a.copy()
b[1]=4
print(a)
print(b)

#count
sentense = ['to', 'be', 'or', 'not', 'to', 'be']
print(sentense.count('to'))
print(len(sentense))

#extend
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
##Notice that the orignal list is modified with method extend, this is different from concatenation


#index
#used to find the index of the first occurrence of a value
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'hi']
print(knights.index('who'))


#insert
numbers = [1,2,3,5,6,7]
numbers.insert(3,'four')
print(numbers)

#pop
x=[1,2,3]
print(x)
print(x.pop())
print(x)
print(x.pop(0))
print(x)
#Note: pop is used as in stack, but there is no corresponding method name called push, but append for list. 

x=[1,2,3]
x.append(x.pop())
print(x)
#To use first in, first out queue structure, use insert(0,...) instead of append. A better option is "deque" in collection module.


#sort
x=[4,6,2,1,7,9]
print(x.sort())# x.sort() returns nothing, so this won't print anything.
x.sort()
print(x)
#to store a sorted array elsewhere, copy the list first
x=[4,6,2,1,7,9]
y=x.copy()
y.sort()
print(x)
print(y)

#advanced sorting
x=['aaaaaaaa', 'aaaaaaa', 'a', 'aaa', 'aaaa', 'aa']
x.sort(key=len)
print(x)
x.sort(key=len, reverse=True)
print(x)