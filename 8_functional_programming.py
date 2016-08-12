### higher-order function ###
f = abs
print(f(-10))

abs(-1)
print(abs)
abs = 1
print(abs)

del abs
print(abs)

import builtins
builtins.abs(-1)
print(builtins.abs)

# builtins.abs = 10
# print(builtins.abs)
#
# del builtins.abs
# print(builtins.abs)

### map and reduce ###
L = ['apple', 'orange', 'banana']
print(L)
print(list(L))
print(list(list(L)))

def char2int(c):
    return ord(c)-48

print(char2int('8'))
print(char2int('.'))

def seq2int(x, y):
    return x*10+y

print(seq2int(1, 7))

from _functools import reduce
def str2int(str):
    return reduce(seq2int, map(char2int, str))

print(str2int('256'))
print(str2int('1567'))


def normalize(name):
    def capitalize(s):
        return s.capitalize()
    return list(map(capitalize, name))
def nor2(name):
    return [s.capitalize() for s in name]

names = normalize(['adam', 'LISA', 'barT'])
print(names)
names = nor2(['adam', 'LISA', 'barT'])
print(names)

def prod(L):
    def times(x, y):
        return x*y
    return reduce(times, L)

print(prod([1, 2, 3 ,4]))
print(prod([3 ,4]))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(str):
    def char2int(c):
        return ord(c) - 48

    def seq2int(x, y):
        return x * 10 + y

    L = list(map(char2int, str))
    dot = L.index(-2)
    L.pop(dot)
    return reduce(seq2int, L)/reduce(seq2int, [1]+[0 for x in range(len(L)-dot)])

print(str2float('123455.1234'))
print('str2float(\'123.456\') =', str2float('123.456'))

### filter ###
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '123', '', None])))

print(5//2)
def is_palindrome(num):
    # num = str(num)
    # for i in range(len(num)//2):
    #     if num[i] != num[-(i+1)]:
    #         return False
    # return True
    return str(num) == str(num)[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))

s = 'ABCD'
print(s == s[::-1])
print(s[::-1])

### sorted ###
L = [-40, 36, 57, -12, 49, 21]
print(sorted(L))
print(sorted(L, key=abs))

L = ['bob', 'einstein', 'Tesla', 'faraday', 'Zoo']
print(sorted(L))
print(sorted(L, key=str.lower))
print(sorted(L, key=str.upper))
print(sorted(L, key=str.upper, reverse=True))

L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
    return t[0].lower()
print(sorted(L, key=by_name))

def by_score(t):
    return t[1]
print(sorted(L, key=by_score, reverse=True))
