#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)

class Dict(dict):
    '''
    Simple dict support access as x.y style

    >>> d = Dict()
    >>> d.x=100
    >>> d.x
    100

    >>> d.empty
    Traceback (most recent call last):
        ...
    AttributeError: no attribute 'empty'
    '''
    def __init__(self, **kwargs):
        super(Dict, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"no attribute '%s'"% key)

    def __setattr__(self, key, value):
        self[key] = value

import doctest
doctest.testmod()

def fact(n):
    '''
    Fact

    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(1)
    1
    >>> fact(3)
    5

    :param n:
    :return:
    '''
    if n<1:
        raise ValueError()
    if n==1:
        return 1
    return n*fact(n-1)

doctest.testmod()
