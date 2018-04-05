#center
print("The Middle by Jimmy Eat World".center(39))
print("The Middle by Jimmy Eat World".center(39, '*'))

#TODO: ljust, rjust, zfill

#find
print("With a moo-moo here, and a moo-moo there".find('moo'))
title = "Monty Python's Flying circus"
print(title.find('Monty'))
print(title.find('Python'))
print(title.find("'"))
print(title.find('Zirquss'))
#TODO: rfind, index, rindex, count, startswith, endswith

#join and split
seq = ['1','2','3','4','5']
sep = '+'
seq_join = sep.join(seq)
print(seq_join)
print(seq_join.split(sep))
dirs = '', 'usr', 'bin', 'env'
print('/'.join(dirs))
print('C:'+'\\'.join(dirs))
#TODO: partition, rpartition, rsplit, splitlines

#lower
print('Trondheim Hammer Dance'.lower())
if 'Gumby' in ['gumby', 'smith', 'jones']: print('Found it!')
if 'Gumby'.lower() in ['gumby', 'smith', 'jones']: print('Found it!')

title = "This is an amazing title with a lot of words!"
print(title.islower())
print(title.istitle())
print(title.isupper())
print(title.capitalize())
print(title.casefold())
print(title.swapcase())
print(title.title())
print(title.upper())
#TODO: islower, istitle, isupper, translate
#TODO: capitalize, casefold, swapcase, title, upper

#replace
a = 'This is a test'
print(a)
a = a.replace('is', 'eez')
print(a) # the original string is modified in this way
#TODO: expandtabs

#strip
a = '      internal whitespace is kept      '
print(a.strip())
a = '*** SPAM ** for * everyone!!! ***'
print(a.strip(' *!'))
#TODO: lstrip, rstrip

#translate
table = str.maketrans('cs', 'kz')
print(table)
print('this is an incredible test'.translate(table))
table2 = str.maketrans('cs', 'kz', ' ')
print('This is an incredible test'.translate(table2))