# -*- coding: utf-8 -*-
import functools

"""
装饰器:

"""

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print("2017年01月14日10:52:02")


# now()
# print(now.__name__)


# 2

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(text)
            return func(*args, *kw)

        return wrapper

    return decorator


@log2('execute')
def now2():
    print('now2() 2017年01月14日11:04:04')


# now2()
# print(now2.__name__)

# 3
def log(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if len(text)>0:
                print(text)
            else:
                print('default')
            return func(*args, *kw)

        return wrapper

    return decorator

@log('log  haha')
def now():
    print("hello decorator!")

@log('dfsdgfdsgfds')
def now2():
    print("now2")


now2()