#Indexing
greeting = 'Hello'
print(greeting[0])
print(greeting[-1])
#print(greeting[5]) IndexError: string index out of range

#fourth = input('Year: ')[3]
#print(fourth)

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

endings = ['st', 'nd', 'rd']+17*['th']+['st', 'nd', 'rd']+7*['th']+['st']

year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-32): ')

month_number = int(month)
day_number = int(day)

#Remember to substract 1 from month and day to get the correct index as array index start from zero
month_name = months[month_number-1]
ordinal = day+endings[day_number-1]

print(month_name+' '+ordinal+', '+year)

tag = '<a href="http://www.python.org">Python web site</a>'

print(tag[9:30])
print(tag[32:-4])

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[3:6])
print(numbers[0:1])
print(numbers[-3:])
print(numbers[3:])
print(numbers[0:3])
print(numbers[:])
print(numbers[0:10:1])
print(numbers[0:10:2])
print(numbers[3:6:3])
print(numbers[::4])
print(numbers[::-1])

#Adding Sequences
print([1,2,3]+[4,5,6])
#Multiplication
print('python'*5)

