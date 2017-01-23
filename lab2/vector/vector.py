__author__ = 'vladbirukov'


class n_vector:
    def __init__(self, list):
        self.components = list

    def __add__(self, other):
        res_len = max(len(self), len(other))
        res_list = []
        for i in range(res_len):
            res_list.append(self[i] + other[i])
        return n_vector(res_list)

    def __sub__(self, other):
        res_len = max(len(self), len(other))
        res_list = []
        for i in range(res_len):
            res_list.append(self[i] - other[i])
        return n_vector(res_list)

    def dot_product(self, other):
        res_len = max(len(self), len(other))
        result = 0
        for i in range(res_len):
            result += self[i] * other[i]
        return result

    def const_mul(self, const):
        for i in range(len(self.components)):
            self.components[i] *= const

    def __mul__(self, var):
        if type(var) is n_vector:
            return self.dot_product(var)
        return n_vector([(comp * var) for comp in self.components])

    def length(self):
        result = 0
        for comp in self.components:
            result += comp ** 2
        return result ** 0.5

    def __len__(self):
        return len(self.components)

    def __getitem__(self, key):
        if key < len(self.components):
            return self.components[key]
        return 0

    def __setitem__(self, key, value):
        self.components[key] = value

    def __delitem__(self, key):
        del self.components[key]

    def __str__(self):
        return str(self.components)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __ne__(self, other):
        if len(self) != len(other):
            return True
        for i in range(len(self)):
            if self[i] != other[i]:
                return True
        return False




def main():
    vect = n_vector([1, 2, 3, 4, 5])
    vect2 = n_vector([1, 1, 3, 4, 5])
    new_vect = vect * 3
    print(vect.length())
    print(vect)
    print(new_vect)
    print(vect + vect2)
    print(vect == vect2)
    print(vect != vect2)
    print(vect * 5)

if __name__ == '__main__':
    main()
