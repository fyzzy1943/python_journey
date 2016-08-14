L = [1, 2, 3, 4, 5]
print(list(map(lambda x: x*x, L)))

def times(x, y):
    return lambda x, y: x*y
f = times(3, 4)
print(f)
print(f(2, 2))
