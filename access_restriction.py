#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student():
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def __get(self):
        return self

    def get_score(self):
        return self.__get().__score

lisa = Student('lisa', 80)
# print(lisa.__name)
print(lisa.get_name())
print(lisa.get_score())
# print(lisa._Student__name)
