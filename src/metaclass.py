class PropertyMeta(type):

    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        prop_methods = {}
        for method in new_class.__dict__:
            if callable(new_class.__dict__[method]):
                if "set_" in method:
                    arg = method[4:]
                    arg_in_dict = prop_methods.get(arg, {})
                    arg_in_dict.update(dict(fset=new_class.__dict__[method]))
                    prop_methods.update({arg: arg_in_dict})
                elif "get_" in method:
                    arg = method[4:]
                    arg_in_dict = prop_methods.get(arg, {})
                    arg_in_dict.update(dict(fget=new_class.__dict__[method]))
                    prop_methods.update({arg: arg_in_dict})
                elif "del_" in method:
                    arg = method[4:]
                    arg_in_dict = prop_methods.get(arg, {})
                    arg_in_dict.update(dict(fdel=new_class.__dict__[method]))
                    prop_methods.update({arg: arg_in_dict})
        for prop in prop_methods:
            setattr(new_class, prop, property(**prop_methods[prop]))
        return new_class


if __name__ == "__main__":
    class Example(metaclass=PropertyMeta):
        def __init__(self):
            self._x = None

        def get_x(self):
            return self._x

        def set_x(self, value):
            self._x = value

        def get_y(self):
            return 'y'

    ex = Example()
    ex.x = 255
    print(ex.x)
    print(ex.y)
