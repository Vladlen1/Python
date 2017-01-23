__author__ = 'vladbirukov'


def cached(func):
    cached.cache = dict()

    def decorate(*args, **kwargs):
        key = (str(func) + ', ' + str(args) + ', ' + str(kwargs))
        if key not in cached.cache:
            cached.cache[key] = func(*args, **kwargs)
            print('no cash')
        return cached.cache[key]
    return decorate


@cached
def myfunc(a, b):
    return a + b


def main():
    print(myfunc(1, 2))
    print(myfunc(2, 2))
    print(myfunc(1, 2))
    print(myfunc(a=1, b=3))
    print(myfunc(b=3, a=1))

if __name__ == '__main__':
    main()
