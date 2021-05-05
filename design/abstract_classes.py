from abc import ABC, abstractmethod


class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def abstract_method(self):
        print(f'invoking abstract_method @ {__class__}')
        pass


class ImplementationSubclass(AbstractClassExample):

    def abstract_method(self):
        super().abstract_method()
        print(f'invoking abstract_method @ {__class__}')
        print('chain execution of methods complete')


obj = ImplementationSubclass(value=100)
print(obj.value)
obj.abstract_method()