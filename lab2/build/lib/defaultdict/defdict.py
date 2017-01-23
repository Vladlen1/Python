__author__ = 'vladbirukov'


class mydefaultdict(dict):
    def __getitem__(self, key):
        try:
            return super(mydefaultdict, self).__getitem__(key)
        except KeyError:
            self[key] = mydefaultdict()
            return self[key]


def main():
    x = mydefaultdict()
    x["a"][2][1][1][1][1][1] = 5
    x[2][1] = 8
    print(x)
    print(x[2][1])

if __name__ == '__main__':
    main()