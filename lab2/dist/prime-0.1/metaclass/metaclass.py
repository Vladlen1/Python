__author__ = 'vladbirukov'


class mymeta(type):
    def __new__(cls, classname, supers, classdict, filename):
        fields = cls._get_fields(cls, filename)
        print('new')
        return super(mymeta, cls).__new__(cls, classname, supers, fields)

    def __init__(cls, classname, supers, classdict, filename):
        print('init')
        k =super(mymeta, cls).__init__(classname, supers, classdict)
        return k

    def _get_fields(cls, filename):
        fields_file = open(filename, 'r')
        fields = {}
        for field in fields_file:
            sf = field.split(' <- ')
            fields[sf[0]] = eval(sf[1])
        return fields


class myclass(metaclass=mymeta, filename='test1.txt'):
    pass


def main():
    x = mymeta('CustomClass', (), {}, 'test1.txt')
    n = x()
    print(x.c)
    print(x.a)
    print(type(x))
    print(type(n))
    print(myclass().__class__.b)

if __name__ == '__main__':
  main()
