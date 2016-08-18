#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Teacher(object):
    pass

t = Teacher()
t.name = 'einstein'
print(t.name)

def set_age(self, age):
    self.age = age

from types import MethodType
t.set_age = MethodType(set_age, t)
t.set_age(16)
print(t.age)

Teacher.dds = 17
print(t.dds)

def set_sex(self, sex):
    self.sex = sex

Teacher.set_sex = set_sex

t.set_sex('man')
print(t.sex)

class Stupid(object):
    __slots__ = ('name', 'why')

s = Stupid()
s.name = 'alpha'
print(s.name)

class Stupid486(Stupid):
    __slots__ = ('age',)

ss = Stupid486()
ss.why = 'no why'
print(ss.why)
ss.age =13
print(ss.age)
