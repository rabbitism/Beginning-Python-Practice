#Parameter Practice
def story(**kwds):
    return 'Once upon a time, there was a {job} called {name}.'.format_map(kwds)

print(story(job = 'king', name = 'Gummy'))
print(story(name = 'Robin', job='brave knight'))
params = {'job':'language', 'name':'Python'}
print(story(**params))
print(story(name = 'Robin', job='brave knight', gender = 'Male'))

def power(x,y, *others):
    if others:
        print('Received redundant parameters: ', others)
    return pow(x,y)

print(power(2,3))
print(power(3,2))
print(power(2,3,4))
params = (2,5,5,5,5,5,5,5)
print(power(*params))

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start
    result=[]

    i = start
    while i<stop:
        result.append(i)
        i+=step
    return result

print(interval(5,20,2))