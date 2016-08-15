#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal():
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

dog = Dog()
dog.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)
run_twice(Animal())

class Timer():
    def run(self):
        print('timer is running...')

run_twice(Timer())
