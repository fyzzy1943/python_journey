print(max(1, 5, 78, 10.2, 100.11))

print(hex(255))
print(hex(1000))

print(int(0xff))
print(0xff)
print(hex(0xff))

def iabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('错误的参数类型')

    if x>=0:
        return x
    else:
        return -x

print(abs(-1))
print(iabs(-1))

# print(abs('A'))
# print(iabs('A'))

print(isinstance(1, ()))

def doNothing():
    pass

x, y = (1, 2)
print(x, y)

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(50, 30, 60, math.pi/6)
print(x,y)

def quadratic(a, b, c):
    delta = math.pow(b, 2)-4*a*c
    if delta<0:
        return False

    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    return x1, x2

print(quadratic(5, 10, 3))
print(quadratic(4, -4, 1))
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

### magnificent split line ###

def ipow(x, n=2):
    sum = 1
    while n>0:
        n = n-1
        sum = sum * x
    return sum

x = 3
print(ipow(x, 4))
print(x)

def add_end(L=[]):
    L.append('end')
    return L

print(add_end())
print(add_end([1]))
print(add_end())
print(add_end([1]))
print(add_end())

def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L

print(add_end())
print(add_end([1]))
print(add_end())
print(add_end([1]))
print(add_end())

def times_add(*numbers):
    if len(numbers)==0:
        return 0

    sum = 1
    for n in numbers:
        sum = sum*n
    return sum

print(times_add(1, 2, 3, 4))
print(times_add())

fruit = ('apple', 'peach')
print(*fruit)

print(times_add(*(1, 2, 3), *(1, 2, 2)))
print((1, 2)*2+(3, 2)+(1,))

attr = {'height':170,'weight':85}
print(attr)
print(*attr)
# print(**attr)

def person(name, **kw):
    print('name:', name, ';kw:', kw)

person('einstein')
person('einstein', what='fuk', man='mercury')
person('faraday', **attr)

def foo(*, city, job):
    print(city, job)

foo(city='B', job='C')
foo(job='D', city='A')

def foo(*args, job):
    for arg in args:
        print(arg,end=' ')
    print(job)

foo('f', 'u', 'k', job='god')

def foo(*args, job, **kwargs):
    print(args, job, kwargs)

foo(1, 2, job=3321, **attr)

def foo(name, *, city='pk', job='saber'):
    print(name, city, job)

foo('arthur')
foo('x', job='assassin')

def foo(name, city='england', job='archer'):
    print(name, city, job)

foo('666')
foo(666, job='lancer')
foo('saber', 'jp')

def foo(name='joker', *args, job='engineer', **kwargs):
    print(name, args, job, kwargs)

foo()

def foo(*, city='england', **kwargs):
    print(city, kwargs)

foo(sa='assassin', city='haven')

### a split line for Gauss ###


