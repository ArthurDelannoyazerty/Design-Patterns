# `type` let us create a new class dynamically (ex: new_class = type('NewClass', (BaseClass,), {'attr': value})
# So in `SingletonMeta`, we create a new object with `super.__call__()`
# Using that as a metaclass (what actually creates the class) we have a way to control the creation of the class `Singleton`
# So here we will only have one instance of the class `Singleton` thanks to the metaclass `SingletonMeta`


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, a:int):
        self.a = a

    def example_function(self):
        print(f"Here is a : {self.a}")


# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    s1 = Singleton(1)
    s1.example_function()

    s2 = Singleton(2)
    s2.example_function()

    print(f'{id(s1)=}')
    print(f'{id(s2)=}')
    print(f'{s1 is s2 = }')

# ---------------------------------- Output ---------------------------------- #
# Here is a : 1
# Here is a : 1
# id(s1)=2010086161664
# id(s2)=2010086161664
# s1 is s2 = True