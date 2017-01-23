__author__ = 'vladbirukov'


class NumberField:
    def __init__(self, value):
        if str(value).isnumeric():
            self.data = value
        else:
            raise TypeError('Incorrect number')

    def __str__(self):
        return str(self.data)


class AlphaField:
    def __init__(self, value):
        if value.isalpha():
            self.data = value
        else:
            raise TypeError('Incorrect alpha')

    def __str__(self):
        return self.data


class ModelCreater(type):
    def __call__(self, *args, **kwargs):
        obj = type.__call__(self, *args)
        for kwarg in kwargs:
            if type(kwargs[kwarg]) == tuple and type(kwargs[kwarg][0] == type):
                setattr(obj, kwarg, kwargs[kwarg][0](kwargs[kwarg][1]))
            else:
                setattr(obj, kwarg, kwargs[kwarg])
        return obj


class DataModel(metaclass=ModelCreater):
    def __init__(self, version):
        self.version = version

    def __str__(self):
        args = self.__dict__
        line = 'DataModel\n'
        for arg in args:
            if not (arg.startswith('_')):
                line += (arg + '\t:' + str(args[arg]) + '\n')
        return line

def main():
    student = DataModel(1, name = (AlphaField, 'Vlad'),
                        surname = (AlphaField, 'Birukov'),
                        age = (NumberField, 18))
    print(student)

if __name__ == '__main__':
    main()