#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student():
    name = 'student'

s = Student()
print(s.name)

s.name = 'lisa'
print(s.name)
print(Student.name)

del s.name
print(s.name)

del Student.name
# print(s.name)
