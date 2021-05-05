from functools import wraps


def debug(func):
    """decorator for debugging passed function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Full name of this method:", func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


# This aspect warps all callable methods in class with debug wrappers defined earlier
# In this example it just logs info, but can change args as well if needed
def debug_aspect(cls):
    """class decorator make use of debug decorator
    to debug class methods """

    for key, val in vars(cls).items():
        print(f'{key} -> {val}')
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


# sample class
@debug_aspect
class Calc:
    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y


mycal = Calc()
print(mycal.add(2, 3))
print(mycal.mul(5, 2))
