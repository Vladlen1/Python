__author__ = 'vladbirukov'
import types


class log_meta(type):
    def __init__(cls, classname, supers, classdict):
        for attr, value in cls.__dict__.items():
            if type(value) == types.FunctionType:
                setattr(cls, attr, cls.log(value))

        def meta_init(self):
            self.log = []

        def meta_get_log(self):
            return '\n\n'.join(self.log)

        setattr(cls, '__init__', meta_init)
        setattr(cls, 'get_log', meta_get_log)

    def log(cls, func):
        def decorated_func(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            self.log.append('function:\t{0}\nargs:\t\t{1}\nkwargs:\t\t{2}\nresult:\t\t{3}'.format(func, args, kwargs, result))
            return result
        return decorated_func


class logger(metaclass=log_meta):
    pass


class testclass(logger):
    def test(self, first, second):
        return first + 2 * second

    def my(self, first, second):
        return second - first

    def __str__(self):
        return 'test'


def main():
    x = testclass()
    print(x.test(1, 2))
    print(x.test(3, 1))
    print(x.test(4, 2))
    print(x.test(2, 8))
    print(x)
    print(x.my(3,2))

    print(x.get_log())

    with open('log.txt', 'w') as f:
        f.write(x.get_log())

if __name__ == '__main__':
    main()
