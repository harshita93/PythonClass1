import math

print(math.cos(3.5))


def cube(x):
    'Return the cube of numbers'
    return x ** 3

print(cube(3))

print(__name__)
print(cube.__name__)
print(cube.__doc__)


print([cube(0), cube(1), cube(2),cube(3),cube(4),cube(5),cube(6),cube(7)])

#list comprehension
# [ <exp> for <var> in iterable>]

print([cube(n) for n in range(21)])

#map (<func> , <iterable>) --> iterator
print(list(map(cube,range(21))))
#list(<iterator>) --->list

age = 56
A = 'A'
print(str(age))

print(hex(age))
print(oct(age))
print(bin(age))


print(ord(A))
print(list(map(ord,'Raymodn')))
print(list(map(hex,map(ord, 'raymond'))))


def ho(c):
    return hex(ord(c))

print(list(map(ho, 'raymond')))


print(chr(0x52))
print(chr(0x65))

def myfunc(func):
    print("My custon help")
    print('__________')
    print("function anme :" , func.__name__)
    print("Created in :", func.__module__)
    print(func.__doc__)


myfunc(ord)



### function Lambda
lambda x: x**2

print(list(map(lambda x: x**3 ,range(21))))







