#clear
d = {} #create an empty dictionary
d['name']='Gumby'
d['age']=42
print(d)
returned_value = d.clear()
print(d)
print(returned_value)

x = {}
y = x
x['key'] = 'value'
print(x)
print(y)
x = {}
print(x)
print(y)

x = {}
y = x
x['key'] = 'value'
print(x)
print(y)
x.clear()
print(x)
print(y) #y is also cleared if using clear() method

sample_dictionary = {
    'Key 1': "Value 1",
    'Key 2': 'Value 2'
}

#copy
x={'username':'admin', 'machines':['foo', 'bar', 'baz']}
y=x.copy()
y['username']='bdong'
y['machines'].remove('bar')
print(x)
print(y)

#deep copy, copy all values
from copy import deepcopy
d={}
d['names']=['Alfred', 'Bertrand']
c=d.copy()
dc=deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)

print(sample_dictionary)
print(sample_dictionary.keys())
print(sample_dictionary.values())
print(sample_dictionary['Key 1'])

#get access to items even for nonexistent key. default values can be customized
d={}
print(d.get('name'))
print(d.get('name','N/A'))

#Listing 4-1: Dictionary Example
# A simple database using get()
# A dictionary with person names as keys. Each person is represented as another dictionary with the keys 'phone' and 'addr' referring to their phone number and address, respectively
people = {
    'Alice':{
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth':{
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil':{
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name: ')
# Are we looking for a phone number or an address?
request = input('Phone number (p) or address (a)? ')

# Use the correct key:
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# Use get to provide default values:
person = people.get(name, {})
label = labels.get(key,key)
result = person.get(key, 'not available')
print(person)
print(label)
print(result)
print("{}'s {} is {}.".format(name, label, result))

#items
print(people.items())

#pop
#pop get the value of corresponding to a given key, and then REMOVE the key-value pair from the dictionary
d ={'x':1,'y':2}
print(d.pop('x'))
print(d)

#popitem will pop an arbitrary item from dictionary. 

#setdefault
d={}
d.setdefault('name','N/A')
print(d)

#update
d={
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}

x={'title': 'Python Language Website'}
d.update(x)
print(d)