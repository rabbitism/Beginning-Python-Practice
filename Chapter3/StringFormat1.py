##Note: Strings are immutable
format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(format % values)
## %s are called conversion specifiers. They mark the places where the values are to be inserted. other specifiers also works for other types. 

#template format
from string import Template

temp = Template("Hello, $who! $what enough for ya?")
print(temp.substitute(who="Mars", what = "Dusty")) #keyword arguments. 

#string format method
print("{}, {} and {}".format("first", "second", "third"))
print("{0}, {1} and {2}".format("first", "second", "third"))
print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to"))

#field can be named
from math import pi, e
print("{name} is approximately {value:.2f}.".format(value=pi, name="π"))
print("{name} is approximately {value}.".format(value=pi, name="π"))
print(f"Euler's constant is roughly {e}")