#print multiple argument together
name = 'Gumby'
salutation = 'Mr.'
greeting = 'Hello, '
print(greeting, salutation, name)

#customize separator
print('I', 'wish', 'to', 'register', 'a', 'compliant', sep = '_')
print('Hello, ',end='')
print('world!')

#Import something as something else
#Several methods:
# import somemodule
# from somemodule import somefunction
# from somemodule import somefunction, anotherfunction, yetanotherfunction
# from somemodule import *
# if two modules have functions with same name, use following calls
# module1.open(...)
# module2.open(...)
# we can use "as" to rename modules
# import math as foobar
# foobar.sqrt(4)
import math as foobar
print(foobar.sqrt(4))
