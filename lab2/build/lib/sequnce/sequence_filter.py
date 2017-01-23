__author__ = 'vladbirukov'


class Sequence_filtration:
    def __init__(self, iterable):
        self.data = [elem for elem in iterable]

    def __iter__(self):
        return iter(self.data)

    def filter(self, function=bool):
        n = len(self.data)
        for i in range(n):
            if function(self.data[i]):
                yield self.data[i]
            else:
                continue

    def __str__(self):
        return str(self.data)


def main():
    a = Sequence_filtration([e for e in range(-9, 10)])
    print(a)
    part = a.filter(lambda x: x > 3)
    print(list(part))

if __name__ == '__main__':
    main()