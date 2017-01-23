__author__ = 'vladbirukov'
import types
class logger(type):
    def __init__(cls, classname, supers, classdict):
        super(logger).__init__()
        for attr, value in cls.__dict__.items():
            if type(value) == types.FunctionType:
                setattr(cls, attr, cls.log(value))

        def get_init(self):
            self.log = []
        def get_met(self):
            return '\n'.join(self.log)
        setattr(cls, '__init__', get_init)
        setattr(cls, 'get_log', get_met)


    def log(cls, func):
        def wraped(self, *args, **kwargs):
            result = func(self,*args, **kwargs)
            self.log.append('function:\t{0}\nargs:\t\t{1}\nkwargs:\t\t{2}\nresult:\t\t{3}'.format(func, args, kwargs, result))
            return result
        return wraped



class logger(metaclass=logger):
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


