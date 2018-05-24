from math import sqrt
for n in range(99,0,-1):
    root = sqrt(n)
    if root == int(root):
        print(n, int(root))
        break


while True:
    word = input('Please enter a word: ')
    if not word: break
    print('The world was ', word)

#loop with else
for n in range(99,11,-1):
    root = sqrt(n)
    if root == int(root):
        print(n, root)
        break
else:
    print("Didn't find it!") #this will only execute when break is not called. 


#List Comprehension
a = [x*x for x in range(10)]
print(a)

#List Comprehension with condition
b = [x*x for x in range(10) if x%3==0]
print(b)

c = [(x,y) for x in range(3) for y in range(3)]
print(c)

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
d = [b+'+'+g for b in boys for g in girls if b[0]==g[0]]
print(d)