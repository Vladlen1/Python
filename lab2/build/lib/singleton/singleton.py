__author__ = 'vladbirukov'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logge(object):
      __metaclass__ = Singleton

      def __init__(self, b):
          print('Created')

a = Logge(1)