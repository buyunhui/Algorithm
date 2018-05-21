# -*- coding: utf-8 -*-
import abc

class Operate(metaclass=abc.ABCMeta):
    """
    简单工厂模式实践：通过加减乘除进行演示，创建操作运算基类
    """

    def __init__(self, left, right):
        self._left = left
        self._right = right

    @abc.abstractmethod
    def get_result(self):
        pass

class add(Operate):
    def __init__(self, left, right):
        super(add, self).__init__(left, right)


    def get_result(self):
        return self._left + self._right

class OperateFactory(object):
    def __init__(self, choice):
        self._choice = choice

    def

