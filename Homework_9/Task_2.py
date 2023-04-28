# Реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)
class NewMetaClass(type):
    a = None

    def __call__(cls):
        if cls.a is None:
            cls.a = super().__call__()
            a = cls.a
            return cls.a
        return cls.a


class MyClass(metaclass=NewMetaClass):

    def method_1(self):
        pass

    def method_1(self):
        print("Ошибка")


obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
print(obj_1 is obj_2
      and obj_2 is obj_3
      and obj_1 is obj_3)
