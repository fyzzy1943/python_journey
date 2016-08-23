#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    print('try...')
    r = 10/int('a')
    print('result: %s'% r)
except ZeroDivisionError as e:
    print('except: ', e)
except ValueError as e:
    print('except: ', e)
finally:
    print('finally...')
print('END')

import logging
def foo():
    return int('a')

def bar():
    return foo()

def main():
    try:
        return bar()
    except BaseException as e:
        # logging.exception(e)
        pass

main()
print('ENDING')

class MyError(ValueError):
    pass

# raise MyError('let\'s rock1')

print('CONTINUE')

def rabbit():
    try:
        0/0
    except Exception as e:
        print('there has a problem: ', e)
        raise

try:
    rabbit()
except Exception as e:
    print('some problem')
    raise
