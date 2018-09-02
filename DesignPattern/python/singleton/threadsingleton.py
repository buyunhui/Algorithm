import time
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)
        self._x = 10

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance
     

def task(arg):
    obj = Singleton.instance()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
time.sleep(20)
obj = Singleton.instance()
print(obj)


class SingletonN(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)  
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(",,,,,,,,,,,,,",obj1,obj2)

def taskN(arg):
    obj = SingletonN()
    print(obj)

for i in range(10):
    t = threading.Thread(target=taskN,args=[i,])
    t.start()