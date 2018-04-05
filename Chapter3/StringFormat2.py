#String Format: The long version

##Replacement Field Names
print("{foo} {} {bar} {}".format(1,2,bar=4,foo=3))
print("{foo} {1} {bar} {0}".format(1,2,bar=4,foo=3))
fullname = ["Alfred", "Smoketoomuch"]
print("Mr {name[1]}".format(name=fullname))

import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
print(tmpl.format(mod=math))
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))  #s: str, r: repr, a: ascii

print("The number is {num}".format(num=42))
print("The number is {num:f}".format(num=42))
print("The number is {num:b}".format(num=42))

print("String Formatting Type Specifiers")
print("Type\tMeaning")
table3_1=[
    ["b", "Formats an integer as a binary numberal."],
    ["c", "Interprets an integer as a Unicode code point."],
    ["d", "Formats an integer as a decimal numeral. Default for integers."],
    ["e", "Formats a decimal number in scientific notation with e to indicate the exponent."]
]
for row in table3_1:
    print("{type}\t{meaning}".format(type=row[0], meaning=row[1]))

#Width, Precision, Thousands separators
print("{num:10}".format(num=3))
print("{name:10}".format(name="Bob"))
print("Pi day is {pi:.2f}".format(pi=math.pi))
print("{pi:10.2f}".format(pi=math.pi))
print("{:.5}".format("Guido van Rossum"))
print("One googol is {:,}".format(10**100))

#Signs, Alignement and Zero-Padding
print("{:010.2f}".format(math.pi))
print("{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}".format(math.pi))
print("{0:<010.2f}\n{0:^010.2f}\n{0:>010.2f}".format(math.pi))

print("{:$^15}".format("WIN BIG"))
print("{:$^15}".format(" WIN BIG "))

print("{0:10.2f}\n{1:10.2f}".format(math.pi, -math.pi))
print("{0:10.2f}\n{1:=10.2f}".format(math.pi, -math.pi)) # "="" fill characters between sign and digits

print("{0:-.2}\n{1:-.2}".format(math.pi, -math.pi)) #default
print("{0:+.2}\n{1:+.2}".format(math.pi, -math.pi))
print("{0: .2}\n{1: .2}".format(math.pi, -math.pi))

print("{:b}".format(42))
print("{:#b}".format(42))


#Listing3-1
width = int(input("Please enter width: "))
price_width = 10
item_width = width - price_width
header_fmt = "{{:{}}}{{:>{}}}".format(item_width, price_width)
fmt = "{{:{}}}{{:>{}.2f}}".format(item_width,price_width)
print("="*width)
print(header_fmt.format("Item",'Price'))
print('-'*width)
transaction_list = [
    ["Apple", 0.4],
    ["Pears", 0.5],
    ["Cantaloupes", 1.92],
    ["Dried Apricots (16 oz.)", 8],
    ["Prunes (4 lbs.)", 12]
]
for transaction in transaction_list:
    print(fmt.format(transaction[0], transaction[1]))
print('='*width)
