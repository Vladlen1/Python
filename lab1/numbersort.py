__author__ = 'vladbirukov'
import sys
#name = raw_input('Write name text file:')
name = sys.argv[2]
with open(name) as num_file:
    num_file = num_file.read()
list_number = []
for number in num_file.split():
    list_number.append(int(number))
def qsort(List):
    if (len(List) > 1):
        less = []
        greater = []
        equal = []
        mid = (int)(len(List) / 2)
        block = List[mid]
        for i in List:
            if (i < block):
                less.append(i)
            if (i == block):
                equal.append(i)
            if (i > block):
                greater.append(i)
        less = qsort(less)
        greater = qsort(greater)
        return less + equal + greater
    else:
        return List
quick = qsort(list_number)
print 'Quick sort',quick

def mergesort(List):
    if len(List) > 1:
        mid = int(len(List)/2)
        List = merge(mergesort(List[:mid]), mergesort(List[mid:]))
    return List

def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res
merg = mergesort(list_number)
print 'Merge sort', merg

def radixsort(List):
    length = len(str(max(List)))
    rang = 10
    for i in range(length):
        prime = [[] for k in range(rang)]
        for x in List:
            figure = x // 10**i % 10
            prime[figure].append(x)
        List = []
        for k in range(rang):
            List = List + prime[k]
    return List
radix = radixsort(list_number)
print 'Radix sort', radix


