__author__ = 'vladbirukov'

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logge(object):
    __metaclass__ = Singleton

    def __init__(self, B):
          print('Created')


def main():
    a = Logge(1)

if __name__ == '__main__':
    main()
