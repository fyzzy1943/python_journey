def log(func):
    def wrapper(*args, **kwargs):
        print('call %s();' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    print('22211')

print(now.__name__)
now()
print()

import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s();'% (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log('execute')
def now():
    print('22211')

print(now.__name__)
now()

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('begin call %s();'% func.__name__)
        func(*args, **kwargs)
        print('end call %s();'% func.__name__)
    return wrapper

@log
def date(t):
    print('2013 %s'% t)

date('july')
print()

def log(obj):
    if isinstance(obj, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(obj)
                return func(*args, **kwargs)
            return wrapper
        return decorator
    else:
        @functools.wraps(obj)
        def wrapper(*args, **kwargs):
            print('none arguments')
            return obj(*args, **kwargs)
        return wrapper

@log('log')
def date(t):
    print('2013 %s'% t)
print(date('july'), end='\n\n')

@log
def date(t):
    print('2013 %s'% t)
print(date.__name__)
date('july')
