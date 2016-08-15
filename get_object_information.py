#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(type(123))
print(type('123'))
print(type(True))
print(type(None))

print(type(abs))

class A():
    pass

print(type(A))
a = A()
print(type(a))
print(type(type))
print(type(print))

print(type(a)==A)

def foo():
    pass

import types
print(types)
print(types.FunctionType)
print(type(foo)==types.FunctionType)
print(types.BuiltinFunctionType)

class Animal():
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

class Cat():
    def __len__(self):
        return 3

class Beauty(Cat):
    pass

h = Husky()
b = Beauty()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, object))
print(isinstance(h, Cat))

print(isinstance(b, Cat))
print(isinstance(b, Dog))

print(isinstance(foo, types.FunctionType))
print(dir(foo))
print(dir(Cat))

print(len(b))

# hasattr(obj, attr)
# setattr(obj, attr, value)
# getattr(obj, attr, default)
