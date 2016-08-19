#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Ghost():
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'this is a ghost, and her name is %s'% self._name

    def __getattr__(self, item):
        return item

g = Ghost('einstein')
print(g)
print(g._name)
print(g.killed)

class Sequence():
    def __init__(self):
        self._num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._num==10:
            raise StopIteration()
        self._num = self._num+1
        return self._num

    def __getitem__(self, item):
        if isinstance(item, int):
            return item

        if isinstance(item, slice):
            L = []
            i = item.start
            step = item.step
            if item.step is None:
                step = 1
            while i<item.stop:
                L.append(i)
                i = i+step
            return L

for i in Sequence():
    print(i)

seq = Sequence()
print(seq[100])
print(seq[10:20])
print(list(range(0, 100))[10:20])

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s'% (self._path, item))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().root.admin.user.add)

class GitHub(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        if item=='users':
            return lambda x='': GitHub('%s/users/%s'% (self._path, x))
        else:
            return GitHub('%s/%s'% (self._path, item))

    def __str__(self):
        return self._path

print(GitHub().users('einstein').repos)

class Dell():
    def __call__(self, *args, **kwargs):
        print('hi, I\'m dell')

dell = Dell()
dell()

print(callable(dell))
print(callable(Dell))
print(callable(Dell()))
print(callable(1))
print(callable(Ghost))
print(callable(Ghost('')))

print(GitHub().users('einstein').repos)
