### slice ###
L = ['apple', 'peach', 'pear']

print(L[-10:-2])

L = list(range(100))

print(L[10:20])
print(L[10:20:2])

L = 'hello world'
print(L[2:])
print(L[:5])

### iteration ###
L = {1:'apple',2:'peach',3:'pear'}
for key in L:
    print(key)

for val in L.values():
    print(val)

for k, v in L.items():
    print(k, v)

for n in L.items():
    print(n)

from collections import Iterable
print(isinstance('a', Iterable))
print(isinstance(123, Iterable))
print(isinstance(True, Iterable))
print(isinstance(None, Iterable))
print(isinstance(123, int))

L=['a','b','c']
print(L)
print(enumerate(L))
for i, val in enumerate(L):
    print(L[i], val, i)

### list_comprehensions ###
L = [x*x for x in range(1, 11)]
print(L)

L=[x*x+1 for x in range(10)]
print(L)

L = [m*n for m in range(1, 9) for n in range(1, 9) if n<=m]
# L.sort()
print(L)

L = ['HelLo', 'woRld', 'I', 'lOVe', 'sAbeR!']
print([s.lower() for s in L])

L = ['HelLo', 'woRld', 3, 'I', 'lOVe', 7, 'sABeR!', 21]
print([s.lower() for s in L if isinstance(s, str)])
print(*[s.lower() for s in L if isinstance(s, str)])

### generator ###
G = (s.lower() for s in L if isinstance(s, str))
print(G)
for _ in G:
    print(_, end=' ')
print()

def fib(n):
    a, b = 0, 1
    for i in range(n+1):
        yield b
        a, b = b, a+b
    return 'done.'

G = fib(10)
for _ in G:
    print(_, end=' ')
print()

def triangles():
    line = [1]
    while True:
        yield line
        line = [1]+[line[i]+line[i-1] for i in range(1, len(line))]+[1]

n = 0
for t in triangles():
    print(t)
    n = n+1
    if  n==10:
        break


