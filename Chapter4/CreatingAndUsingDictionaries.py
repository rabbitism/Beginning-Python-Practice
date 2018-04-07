items = [
    ('name', 'Gumby'),
    ('age', 42)
]

d = dict(items)
print(d)
print(d['name'])

x={}
x[42] = 'Foobar'
print(x)

#Listing 4-1: Dictionary Example
# A simple database
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

# Only try to print information if the name is a valid key in our dictionary
if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))

#string formatting with dictionaries
phonebook = {'Beth': '9102', 'Alice':'2341', 'Cecil':'3258'}
print("Cecil's phone number is {Cecil}".format_map(phonebook))

template = '''<html>
<head><title>{title}</title></head>
<body>
<h1>{title2}</h1>
<p>{text}</p>
</body>'''

data = {'title': 'My Home Page', 'text': 'Welcome to my home page!', 'title2':'This is title 2'}
print(template.format_map(data))
