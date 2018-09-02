# -*- coding: utf-8 -*-

class Singleton(type):
    """
    通过元类实现单例
    """

    def __init__(self, *args, **kwargs):
        print("__init__")
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("__call__")
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance


class Foo(metaclass=Singleton):
    def __init__(self):
        pass


foo1 = Foo()
foo2 = Foo()
print(
    Foo.__dict__
)  #_Singleton__instance': <__main__.Foo object at 0x100c52f10> 存在一个私有属性来保存属性，而不会污染Foo类（其实还是会污染，只是无法直接通过__instance属性访问）

print(foo1 is foo2)  # True

# 输出
# __init__
# __call__
# __call__
# {'__module__': '__main__', '__metaclass__': <class '__main__.Singleton'>, '_Singleton__instance': <__main__.Foo object at 0x100c52f10>, '__dict__': <attribute '__dict__' of 'Foo' objects>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None}
# True


# 使用装饰器实现单例
def SingletonC(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton



@SingletonC
class A(object):
    a = 1

    def __init__(self, x=0):
        self._x = x



a1 = A(2)
a2 = A(3)

print(a1 == a2)