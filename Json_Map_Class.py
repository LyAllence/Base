# coding: utf-8

import json
import os


class A(object):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return 'age:' + str(self.age)


# the return cannot include any not seriable var;
def parse(a):
    print('start===')
    return {
        'age': a.age,
    }


def load(d):
    return A(d['age'])


list_A = []
if os.path.exists(os.path.join(os.path.abspath('.'), 'data.json')):
    f_load = open(os.path.join(os.path.abspath('.'), 'data.json'), 'r')
    load_A = json.load(fp=f_load)
    f_load.close()
    list_load_A = list(load_A.values())
    list_A = [json.loads(i, object_hook=load) for i in list_load_A]
else:
    list_A = [A(1), A(2), A(3)]
    map_A = {}
    for column, i in enumerate(list_A):
        map_A[column] = json.dumps(obj=i, default=parse)
    f_dump = open(os.path.join(os.path.abspath('.'), 'data.json'), 'w')
    json.dump(obj=map_A, fp=f_dump)
    f_dump.close()
print(list_A)
