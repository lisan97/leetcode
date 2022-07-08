import copy
def deepcopy(cls):
    if isinstance(cls, dict):
        return {k: deepcopy(v) for k, v in cls.items()}
    elif isinstance(cls, list):
        return [deepcopy(item) for item in cls]
    elif isinstance(cls, tuple):
        return tuple([deepcopy(item) for item in cls])
    else:
        return cls

if __name__ == '__main__':
    lst = [1, 2, 3, 6, 4, ([5, 6, 8, 7, [7, 8, {"acb": 89375, "dxt": "kgfjolij", "v": 222}, 5, 4, 7]], (2,5,{"z":2}))]

    res = deepcopy(lst)
    print(res,'deep',id(res[5][0]))
    print('lst', id(lst[5][0]))
    ls = copy.copy(lst)
    print('ls', id(ls[5][0]))