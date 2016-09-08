#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = dict(a=1)

class Dict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"no attribute '%s'"% key)

    def __setattr__(self, key, value):
        self[key] = value

import unittest

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
        # self.assertEqual(1, 2)

    def test_key(self):
        d = Dict()
        d['key'] = 'val'
        self.assertEqual(d['key'], 'val')

    def test_attr(self):
        d = Dict()
        d.k = 'val'
        self.assertEqual(d.k, 'val')
        self.assertEqual(d['k'], 'val')
        d[3] = 'id'

unittest.main()
