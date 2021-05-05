from abc import ABCMeta, abstractmethod


class Interface:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def post(self): raise NotImplementedError


class InterfaceImpl(Interface):
    def post(self):
        print('Hello, World 2!')
