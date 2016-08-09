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
