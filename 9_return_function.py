# function as return value
def lazy_sum(*args):
    def sum():
        s = 0
        for n in args:
            s = s + n
        return s
    return sum

L = [1, 2, 3, 4, 5]
f = lazy_sum(*L)
L = [2, 4, 5]
print(f)
print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())

def count():
    i = 1
    def f():
        return i
    i = 4
    return f

f1 = count()
print(f1())

def count():
    fs = []
    for j in range(1, 4):
        def f():
            def g():
                return j * j

            return g
        fs.append(f)
    return fs

f1, f2, f3=count()
print(f1()(), f2, f2(), f2()())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 3):
        fs.append(f(i))
    return fs

f1, f2 = count()
print(f1(), f2())
