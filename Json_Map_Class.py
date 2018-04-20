# coding: utf-8

import json
import os


class B(object):
    def __init__(self, age):
        self.age = age


class A(object):
    def __init__(self, b):
        self.b = b


# the return cannot include any not parse var; if it has ,
# we will call the function again, and obj is the var, you can parse the var
def parse_b(one):
    return {
        'age': one.age
    }


def parse(a):
    return {
        'b': json.dumps(obj=a.b, default=parse_b),
    }


def load_b(d_one):
    return B(d_one['age'])


def load(d):
    return A(json.loads(d['b'], object_hook=load_b))


a = A(B(12))
dumps_a = json.dumps(obj=a, default=parse)
print('this is dumps data:', dumps_a)
print('type is:', type(dumps_a))
print('=======')
loads_a = json.loads(dumps_a, object_hook=load)
print('this is loads data:', loads_a)
print('type is:', type(loads_a))

#summary: the data of json cannot have dict or other withour cannnot json.dump

