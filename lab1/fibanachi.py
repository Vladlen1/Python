__author__ = 'vladbirukov'
def fibonachi(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
print 'Fibanachi number:'
for n in fibonachi(100):
    print n

