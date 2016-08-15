#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module'

__author__ = 'forDawn'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('hello module')
    elif len(args)==2:
        print('hello %s'% args[1])
    else:
        print('i don\'t know what you said')

if __name__=='__main__':
    test()

def _sayHello(name):
    return 'hello %s'% name

def _sayHi(name):
    return 'hi %s'% name

def greeting(name):
    if len(name)<5:
        return _sayHello(name)
    else:
        return _sayHi(name)
