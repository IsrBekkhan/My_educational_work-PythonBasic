def singleton(cls):
    """
    Декоратор Синглтон, гарантирующий, что у класса только один экземпляр.
    """
    def wrapped(*args, **kwargs):
        if not wrapped.instance:
            wrapped.instance = cls(*args, **kwargs)
        return wrapped.instance
    wrapped.instance = None
    return wrapped


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
