print("Hello, world")
print("Let's say")
print('Let\'s go')

# Difference of repr and str
print("repr, generally get a representation of the value")
print(repr("Hello, \n world!"))
print("str, convert to string with fashion")
print(str("Hello, \n world!"))

#print long strings
print('''This is a very long string. It continues here.
And it's not over yet. "Hello world!"
Still here''')
print("""A long string""")


#print raw string 
path='C:\nowhere'

print(path)
print(r'C:\nowhere')
#print(r"C:\nowhere\") #illigal as the last character cannot be backslash in raw string

#Unicode, Byte, bytearray
print("\u00C6")
print("\U0001F60A")
print("This is a cat: \N{Cat}")
print("Hello, world!".encode("ASCII"))
print("Hello, world!".encode("UTF-8"))
print("Hello, world!".encode("UTF-32"))

print(len("How long is this?".encode("ASCII")))
print(len("How long is this?".encode("UTF-8")))
print(len("How long is this?".encode("UTF-32")))

