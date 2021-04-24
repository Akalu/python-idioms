# Python uses LEGB rule: Local, Enclosing, Global, Built-in to determine th scope of specific variable/function
def outer():
    test = 1  # outer scope

    def inner():
        test = 2  # inner scope
        print('inner:', test)

    inner()
    print('outer:', test)


test = 0  # global scope
outer()
print('global:', test)
