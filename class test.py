#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        print('%s %s'% (self.name, self.score))

    def getGrade(self):
        if self.score>90:
            print('A')
        elif self.score>60:
            print('C')
        else:
            print('no pass')

lisa = Student('lisa', 75)
print(lisa)
lisa.print()

lisa.weight = 75
print(Student)
print(lisa.weight)
lisa.getGrade()
