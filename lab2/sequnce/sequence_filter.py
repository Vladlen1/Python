__author__ = 'vladbirukov'
import collections


class Sequence(object):

    def __init__(self, source):
        if not isinstance(source, collections.Iterator):
            raise TypeError("No iterator!")
        self.source = source
        self.seq_list = list()
        self.copied = False

    def __next__(self, ind):
        try:
            if not self.copied:
                if ind > len(self.seq_list) - 1:
                    itm = next(self.source)
                    self.seq_list.append(itm)
                else:
                    itm = self.seq_list[ind]
            else:
                if ind >= len(self.seq_list):
                    raise StopIteration()
                itm = self.seq_list[ind]

            return itm
        except StopIteration:
            self.copied = True
            raise StopIteration()

    def __iter__(self):
        i = 0
        while True:
            try:
                yield self.__next__(i)
                i += 1
            except StopIteration:
                break

    def filter(self, func):
        def temp_gen():
            for item in iter(self):
                if func(item):
                    yield item
        return Sequence(temp_gen())

    def __str__(self):
        return "[" + ", ".join([str(x) for x in iter(self)]) + "]"


if __name__ == '__main__':
    s1 = Sequence(iter([1, 2, 3, 15, 21]))
    print(s1)
    s2 = s1.filter(lambda x: x > 5).filter(lambda x: x > 15)
    print(s2)

