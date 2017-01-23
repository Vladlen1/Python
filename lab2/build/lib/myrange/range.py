__author__ = 'vladbirukov'


class myError(Exception):
    def __init__(self):
        self.msg = 'Error using object'

    def __str__(self):
        return self.msg


class myTypeError(myError):
    def __init__(self):
        self.msg = 'Incorrect type'


class myValueError(myError):
    def __init__(self):
        self.msg = 'Incorrect Value'


class myIndexError(myError):
    def __init__(self):
        self.msg = 'Incorrect index'


class myrange:
    def __init__(self, start, stop = None, step = None):
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1
        values = [start, stop, step]
        for value in values:
            if not((type(value) == int) or (int in type(value).__bases__)):
                raise myTypeError()
        self.start = start
        self.stop = stop
        if step != 0:
            self.step = step
        else:
            raise myValueError()

    def __iter__(self):
        return myrange(self.start, self.stop, self.step)

    def __next__(self):
        val = self.start
        if(self.step > 0) and (val >= self.stop):
            raise StopIteration
        elif(self.step < 0) and (val <= self.stop):
            raise StopIteration
        self.start += self.step
        return val

    def __str__(self):
        result = 'myrange(' + str(self.start) + ', ' + str(self.stop)
        if self.step != 1:
            result += ', ' + str(self.step)
        result += ')'
        return(result)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return abs(self.start - self.stop) // abs(self.step)

    def __getitem__(self, item):
        if type(item) == int:
            if -len(self) <= item < 0:
                item += len(self)
            if 0 <= item < len(self):
                return self.start + item * self.step
            else:
                raise myIndexError()
        else:
            raise myValueError

    def __reversed__(self):
        if (self.step > 0) and (self.start < self.stop) or \
                    (self.step < 0) and (self.start > self.stop):
            k = abs(self.start - self.stop) // abs(self.step)
            k = k if (abs(self.start - self.stop) % abs(self.step)) != 0 \
                else (k - 1)
            new_start = self.start + k * self.step
            new_stop = (self.start - 1) if self.step > 0 else (self.start + 1)
            self.step *= -1
            self.start = new_start
            self.stop = new_stop
        return self


def main():
    for i in range(1, 5, 3):
        print(i)

    for i in myrange(1, 5):
        print(i)

    x = [i for i in myrange(10)]
    print(x)
    print(x[2])

    for i in range(1, 5, 3):
        print(i)

    for i in myrange(1, 5, 3):
        print(i)
    x = [i for i in myrange(10)]
    print(x)
    for i in reversed(myrange(1, 10)):
        print(i)

if __name__ == '__main__':
    main()
