
# 0 : 배경
# 1 : 플레이어
# 2 : 몬스터
objects = [[],[],[]]

UI = [[],[]]

def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l

def get_objects(layer):
    return objects[layer]

def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o


def clear():
    for o in all_objects():
        del o
    for l in objects:
        l.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

