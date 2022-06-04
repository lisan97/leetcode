import threading

def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kwargs):
        with func.__lock__:
            return func(*args,**kwargs)
    return synced_func

def Singleton(cls):
    instances = {}
    @synchronized
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@Singleton
class Cls(object):
    def __init__(self):
        pass

if __name__ == '__main__':
    cls1 = Cls()
    cls2 = Cls()
    print(id(cls1)==id(cls2))