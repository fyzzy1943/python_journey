#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn():
    def run(self):
        print('running...')

class FlyableMinIn():
    def fly(self):
        print('flying...')

class Dog(Mammal, RunnableMixIn):
    pass

dog = Dog()
dog.run()

class C1():
    def foo(self):
        print('foo from C1')

class C2():
    def foo(self):
        print('foo from C2')

class Sub(C1, C2):
    pass

sub = Sub()
sub.foo()
