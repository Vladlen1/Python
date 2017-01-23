__author__ = 'vladbirukov'
import unittest

from vector import vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.vect1 = vector.n_vector([1, 2, 3, 4, 5])
        self.vect2 = vector.n_vector([1, 1, 3, 4, 5])

    def test1(self):
        self.assertEqual(self.vect1 + self.vect2, [2, 3, 6, 8, 10])

    def test2(self):
        self.assertEqual(self.vect1 == self.vect2, False)

    def test3(self):
        self.assertEqual(self.vect1.length(), 7.416198487095663)
        with self.assertRaises(TypeError):
            self.vect1 * '4'


if __name__ == '__main__':
    unittest.main()
