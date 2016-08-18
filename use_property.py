#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer')
        if score>100 or score<0:
            raise ValueError('score must between 0 and 100')

        self._score = score

s = Student()
s.score = 99
print(s.score)

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height

screen = Screen()
screen.width=1920
screen.height=1080
print(screen.resolution)

sc = Screen()
# print(sc.resolution)
